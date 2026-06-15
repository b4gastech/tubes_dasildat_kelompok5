import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

from utils.style import load_css
from utils.model_loader import load_models, load_scaler, FITUR_12, FITUR_KNN

load_css()
matplotlib.rcParams.update({
    'figure.facecolor':'#0f172a','axes.facecolor':'#1e293b',
    'text.color':'#f1f5f9','axes.labelcolor':'#94a3b8',
    'xtick.color':'#94a3b8','ytick.color':'#94a3b8',
})

@st.cache_resource
def get_models():
    dt, knn, svm = load_models()
    scaler = load_scaler()
    return dt, knn, svm, scaler

dt, knn, svm, scaler = get_models()

def predict_batch(df, model_name):
    if model_name == "Decision Tree":
        return dt.predict(df[FITUR_12])
    elif model_name == "KNN" and knn:
        scaled = pd.DataFrame(scaler.transform(df[FITUR_12]), columns=FITUR_12)
        return knn.predict(scaled[FITUR_KNN])
    elif model_name == "SVM" and svm:
        return svm.predict(scaler.transform(df[FITUR_12]))
    return dt.predict(df[FITUR_12])

def is_stable(pred):
    return str(pred).strip().lower() in ["stable","1","1.0"] or pred == 1

MODEL_ACC = {"Decision Tree":"74.0%","KNN":"79.0%","SVM":"98.0%"}

st.markdown('<p class="section-label">Batch Analysis</p>', unsafe_allow_html=True)
st.title("📁 CSV Batch Prediction")

st.sidebar.markdown('<p class="section-label">Model</p>', unsafe_allow_html=True)
opts = []
if dt: opts.append("Decision Tree")
if knn: opts.append("KNN")
if svm: opts.append("SVM")
model_name = st.sidebar.radio("Pilih Model", opts or ["Decision Tree"], label_visibility="collapsed")
st.info(f"Model aktif: **{model_name}** — Akurasi: **{MODEL_ACC[model_name]}**")

with st.expander("ℹ️ Panduan Format & Template CSV"):
    st.write("Pastikan file CSV memiliki kolom berikut:")
    st.code(", ".join(FITUR_12))
    st.download_button("📥 Download Template CSV",
        pd.DataFrame(columns=FITUR_12).to_csv(index=False).encode('utf-8'),
        "template_smartgrid.csv","text/csv")

file = st.file_uploader("Upload file dataset CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip()
    st.markdown("##### Preview Dataset")
    st.dataframe(df.head(), use_container_width=True)

    missing = [c for c in FITUR_12 if c not in df.columns]
    if missing:
        st.error(f"❌ Kolom tidak lengkap! Yang hilang: {missing}")
    else:
        if st.button("🚀 Jalankan Prediksi Batch", use_container_width=True):
            with st.spinner("Memproses data..."):
                preds = predict_batch(df, model_name)
                labels = ["STABLE" if is_stable(p) else "UNSTABLE" for p in preds]
                df["Prediksi"] = labels

            stable_n   = labels.count("STABLE")
            unstable_n = labels.count("UNSTABLE")
            total      = len(labels)

            st.markdown("---")
            c1,c2,c3,c4 = st.columns(4)
            c1.metric("Total Data", total)
            c2.metric("Stable ✅", stable_n)
            c3.metric("Unstable ⚠️", unstable_n)
            c4.metric("Stable %", f"{stable_n/total*100:.1f}%")

            cc1,cc2 = st.columns(2)
            with cc1:
                fig,ax = plt.subplots(figsize=(4,4))
                ax.pie([stable_n,unstable_n],labels=["Stable","Unstable"],
                       autopct="%1.1f%%",colors=['#06b6d4','#ef4444'],
                       startangle=90,textprops={'color':'#f1f5f9','fontsize':10},
                       wedgeprops={'edgecolor':'#0f172a','linewidth':2})
                ax.set_title("Distribusi Prediksi",color='#f1f5f9',pad=10)
                fig.patch.set_facecolor('#0f172a')
                st.pyplot(fig)
            with cc2:
                fig2,ax2 = plt.subplots(figsize=(5,4))
                bars = ax2.bar(["Stable","Unstable"],[stable_n,unstable_n],
                               color=['#06b6d4','#ef4444'],width=0.45,edgecolor='none')
                for bar,val in zip(bars,[stable_n,unstable_n]):
                    ax2.text(bar.get_x()+bar.get_width()/2,bar.get_height()+0.5,
                             str(val),ha='center',color='#f1f5f9',fontweight='bold')
                ax2.spines['top'].set_visible(False);ax2.spines['right'].set_visible(False)
                ax2.spines['left'].set_color('#334155');ax2.spines['bottom'].set_color('#334155')
                ax2.set_title("Jumlah per Kelas",color='#f1f5f9',pad=10)
                fig2.patch.set_facecolor('#0f172a')
                st.pyplot(fig2)

            st.markdown("##### Hasil Prediksi Lengkap")
            st.dataframe(df, use_container_width=True)
            st.download_button("📥 Download Hasil Prediksi",
                df.to_csv(index=False).encode('utf-8'),
                "hasil_prediksi.csv","text/csv",use_container_width=True)

st.markdown("---")
st.caption("⚡ SmartGrid AI Platform — Tubes Dasildat Kelompok 5")
