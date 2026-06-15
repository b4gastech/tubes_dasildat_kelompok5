import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# ======================================
# PAGE CONFIG — harus baris pertama Streamlit
# ======================================
st.set_page_config(
    page_title="SmartGrid AI — Stability Prediction",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils.style import load_css
from utils.model_loader import load_models, load_scaler, FITUR_12, FITUR_KNN

load_css()

# ======================================
# LOAD MODELS
# ======================================
@st.cache_resource
def get_all():
    dt, knn, svm = load_models()
    scaler = load_scaler()
    return dt, knn, svm, scaler

dt, knn, svm, scaler = get_all()

if not dt:
    st.error("❌ Gagal load model Decision Tree. Pastikan file models/decision_tree_model.pkl ada.")
    st.stop()

MODEL_ACC = {"Decision Tree": "74.0%", "KNN": "79.0%", "SVM": "98.0%"}

# ======================================
# PREDICTION HELPER
# ======================================
def predict(input_df, model_name):
    """
    input_df: DataFrame dengan kolom FITUR_12 (12 kolom)
    Handles perbedaan fitur antar model secara otomatis.
    """
    if model_name == "Decision Tree":
        return dt.predict(input_df[FITUR_12])[0]
    elif model_name == "KNN":
        if not knn:
            return dt.predict(input_df[FITUR_12])[0]
        scaled = pd.DataFrame(scaler.transform(input_df[FITUR_12]), columns=FITUR_12)
        return knn.predict(scaled[FITUR_KNN])[0]
    elif model_name == "SVM":
        if not svm:
            return dt.predict(input_df[FITUR_12])[0]
        scaled = scaler.transform(input_df[FITUR_12])
        return svm.predict(scaled)[0]

def is_stable(pred):
    return str(pred).strip().lower() in ["stable", "1", "1.0"] or pred == 1

# ======================================
# SIDEBAR
# ======================================
with st.sidebar:
    st.markdown('<p class="section-label">⚡ SmartGrid AI</p>', unsafe_allow_html=True)
    st.markdown("## Control Panel")
    st.markdown("---")

    menu = st.radio(
        "Navigasi",
        ["🏠 Home", "🔍 Prediksi Manual", "📁 Analisis CSV"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown('<p class="section-label">Pilih Model</p>', unsafe_allow_html=True)

    model_options = []
    if dt:  model_options.append("Decision Tree")
    if knn: model_options.append("KNN")
    if svm: model_options.append("SVM")
    if not model_options: model_options = ["Decision Tree"]

    selected_model = st.selectbox("Algoritma", model_options, label_visibility="collapsed")
    st.caption(f"Akurasi: **{MODEL_ACC[selected_model]}**")

    st.markdown("---")
    st.markdown('<p class="section-label">Tim Pengembang</p>', unsafe_allow_html=True)
    for name in ["Dista", "Piqi", "Tora"]:
        st.markdown(f'<div class="team-card">👤 {name}</div>', unsafe_allow_html=True)

# ======================================
# HOME
# ======================================
if menu == "🏠 Home":
    st.markdown('<p class="section-label">Dashboard Utama</p>', unsafe_allow_html=True)
    st.title("⚡ Smart Grid Stability Analysis")
    st.markdown(
        "Platform prediksi stabilitas jaringan listrik berbasis Machine Learning. "
        "Masukkan parameter jaringan untuk mengetahui kondisi **STABLE** atau **UNSTABLE** secara real-time."
    )
    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Model Tersedia", str(len(model_options)), " · ".join(model_options))
    c2.metric("Fitur Input", "12", "Parameter Jaringan")
    c3.metric("Akurasi Terbaik", "98.0%", "SVM Model")
    c4.metric("Status", "Online ✓", "Ready")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="section-label">Tentang Dataset</p>', unsafe_allow_html=True)
        st.markdown("### Smart Grid Stability Dataset")
        st.write(
            "Dataset berisi **60.000 sampel** dengan 12 fitur parameter jaringan listrik. "
            "Target prediksi adalah label `stabf`: apakah sistem dalam kondisi stabil atau tidak."
        )
        st.info("**12 Fitur:** tau1–tau4 (waktu reaksi), p1–p4 (daya), g1–g4 (konduktansi)")

    with col2:
        st.markdown('<p class="section-label">Model yang Digunakan</p>', unsafe_allow_html=True)
        st.markdown("### Algoritma ML")
        for model_name, acc, status in [
            ("Decision Tree", "74.0%", "✅" if dt else "❌"),
            ("K-Nearest Neighbor", "79.0%", "✅" if knn else "❌"),
            ("Support Vector Machine", "98.0%", "✅" if svm else "❌"),
        ]:
            st.markdown(
                f'<div style="display:flex;justify-content:space-between;align-items:center;'
                f'background:rgba(15,23,42,0.6);border:1px solid rgba(148,163,184,0.12);'
                f'border-radius:8px;padding:10px 14px;margin:6px 0;">'
                f'<span style="color:#f1f5f9;font-weight:500">{status} {model_name}</span>'
                f'<span style="color:#06b6d4;font-weight:700;font-family:monospace">{acc}</span>'
                f'</div>',
                unsafe_allow_html=True
            )

    st.markdown("---")
    st.caption("⚡ SmartGrid AI Platform — Tubes Dasildat Kelompok 5 | Dista · Piqi · Tora")

# ======================================
# PREDIKSI MANUAL
# ======================================
elif menu == "🔍 Prediksi Manual":
    st.markdown('<p class="section-label">Input Parameter</p>', unsafe_allow_html=True)
    st.title("🔍 Prediksi Manual")
    st.info(f"Model aktif: **{selected_model}** — Akurasi: **{MODEL_ACC[selected_model]}**")
    st.markdown("---")

    st.markdown("##### Parameter Waktu Reaksi (tau)")
    c1, c2, c3, c4 = st.columns(4)
    tau1 = c1.number_input("TAU1", value=0.0, format="%.4f")
    tau2 = c2.number_input("TAU2", value=0.0, format="%.4f")
    tau3 = c3.number_input("TAU3", value=0.0, format="%.4f")
    tau4 = c4.number_input("TAU4", value=0.0, format="%.4f")

    st.markdown("##### Parameter Daya (p)")
    c1, c2, c3, c4 = st.columns(4)
    p1 = c1.number_input("P1", value=0.0, format="%.4f")
    p2 = c2.number_input("P2", value=0.0, format="%.4f")
    p3 = c3.number_input("P3", value=0.0, format="%.4f")
    p4 = c4.number_input("P4", value=0.0, format="%.4f")

    st.markdown("##### Parameter Konduktansi (g)")
    c1, c2, c3, c4 = st.columns(4)
    g1 = c1.number_input("G1", value=0.0, format="%.4f")
    g2 = c2.number_input("G2", value=0.0, format="%.4f")
    g3 = c3.number_input("G3", value=0.0, format="%.4f")
    g4 = c4.number_input("G4", value=0.0, format="%.4f")

    st.markdown("---")

    if st.button("🚀 Jalankan Prediksi", use_container_width=True):
        input_df = pd.DataFrame([[tau1,tau2,tau3,tau4,p1,p2,p3,p4,g1,g2,g3,g4]], columns=FITUR_12)
        hasil = predict(input_df, selected_model)

        if is_stable(hasil):
            st.markdown(
                '<div class="result-card-stable">'
                '<p style="color:#94a3b8;margin:0 0 8px;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.1em">Hasil Prediksi</p>'
                '<h2>✅ STABLE</h2>'
                '<p style="color:#6ee7b7;margin:8px 0 0;font-size:0.9rem">Jaringan listrik dalam kondisi stabil</p>'
                '</div>', unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="result-card-unstable">'
                '<p style="color:#94a3b8;margin:0 0 8px;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.1em">Hasil Prediksi</p>'
                '<h2>⚠️ UNSTABLE</h2>'
                '<p style="color:#fca5a5;margin:8px 0 0;font-size:0.9rem">Jaringan listrik dalam kondisi tidak stabil!</p>'
                '</div>', unsafe_allow_html=True
            )
        st.caption(f"Raw output: `{hasil}` | Model: {selected_model}")

    st.markdown("---")
    st.caption("⚡ SmartGrid AI Platform — Tubes Dasildat Kelompok 5")

# ======================================
# ANALISIS CSV
# ======================================
elif menu == "📁 Analisis CSV":
    st.markdown('<p class="section-label">Batch Analysis</p>', unsafe_allow_html=True)
    st.title("📁 Analisis CSV")
    st.info(f"Model aktif: **{selected_model}** — Akurasi: **{MODEL_ACC[selected_model]}**")

    with st.expander("ℹ️ Panduan Format Data & Download Template"):
        st.write("Pastikan file CSV memiliki kolom berikut:")
        st.code(", ".join(FITUR_12))
        template_df = pd.DataFrame(columns=FITUR_12)
        st.download_button(
            "📥 Download Template CSV",
            template_df.to_csv(index=False).encode('utf-8'),
            "template_smartgrid.csv", "text/csv"
        )

    uploaded = st.file_uploader("Upload file dataset CSV", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        df.columns = df.columns.str.strip()

        st.markdown("##### Preview Dataset")
        st.dataframe(df.head(), use_container_width=True)

        missing = [c for c in FITUR_12 if c not in df.columns]
        if missing:
            st.error(f"❌ Kolom tidak lengkap! Yang hilang: {missing}")
        else:
            if st.button("🚀 Jalankan Prediksi Batch", use_container_width=True):
                with st.spinner("Memproses data..."):
                    results = []
                    for i in range(len(df)):
                        row = df[FITUR_12].iloc[[i]]
                        pred = predict(row, selected_model)
                        results.append("STABLE" if is_stable(pred) else "UNSTABLE")
                    df["Prediksi"] = results

                stable_n   = results.count("STABLE")
                unstable_n = results.count("UNSTABLE")
                total      = len(results)

                st.markdown("---")
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Total Data", total)
                c2.metric("Stable ✅", stable_n)
                c3.metric("Unstable ⚠️", unstable_n)
                c4.metric("Stable %", f"{stable_n/total*100:.1f}%")

                import matplotlib
                import matplotlib.pyplot as plt
                matplotlib.rcParams.update({
                    'figure.facecolor': '#0f172a', 'axes.facecolor': '#1e293b',
                    'text.color': '#f1f5f9', 'axes.labelcolor': '#94a3b8',
                    'xtick.color': '#94a3b8', 'ytick.color': '#94a3b8',
                })

                cc1, cc2 = st.columns(2)
                with cc1:
                    fig, ax = plt.subplots(figsize=(4, 4))
                    ax.pie([stable_n, unstable_n], labels=["Stable","Unstable"],
                           autopct="%1.1f%%", colors=['#06b6d4','#ef4444'],
                           startangle=90, textprops={'color':'#f1f5f9','fontsize':10},
                           wedgeprops={'edgecolor':'#0f172a','linewidth':2})
                    ax.set_title("Distribusi Prediksi", color='#f1f5f9', pad=10)
                    fig.patch.set_facecolor('#0f172a')
                    st.pyplot(fig)

                with cc2:
                    fig2, ax2 = plt.subplots(figsize=(5, 4))
                    bars = ax2.bar(["Stable","Unstable"], [stable_n, unstable_n],
                                   color=['#06b6d4','#ef4444'], width=0.45, edgecolor='none')
                    for bar, val in zip(bars, [stable_n, unstable_n]):
                        ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
                                 str(val), ha='center', color='#f1f5f9', fontweight='bold')
                    ax2.spines['top'].set_visible(False); ax2.spines['right'].set_visible(False)
                    ax2.spines['left'].set_color('#334155'); ax2.spines['bottom'].set_color('#334155')
                    ax2.set_title("Jumlah per Kelas", color='#f1f5f9', pad=10)
                    fig2.patch.set_facecolor('#0f172a')
                    st.pyplot(fig2)

                st.markdown("##### Hasil Prediksi Lengkap")
                st.dataframe(df, use_container_width=True)
                st.download_button(
                    "📥 Download Hasil Prediksi",
                    df.to_csv(index=False).encode('utf-8'),
                    "hasil_prediksi.csv", "text/csv", use_container_width=True
                )

    st.markdown("---")
    st.caption("⚡ SmartGrid AI Platform — Tubes Dasildat Kelompok 5")
