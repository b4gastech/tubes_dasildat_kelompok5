import streamlit as st
from utils.style import load_css

load_css()

st.markdown('<p class="section-label">Dokumentasi</p>', unsafe_allow_html=True)
st.title("📋 About Project")
st.caption("SmartGrid AI Platform — Machine Learning Classification Project")

st.markdown("---")

# OVERVIEW
st.markdown('<p class="section-label">Gambaran Umum</p>', unsafe_allow_html=True)
st.markdown("### Project Overview")
st.write(
    "**SmartGrid AI Platform** adalah aplikasi Machine Learning berbasis Streamlit "
    "untuk memprediksi stabilitas sistem Smart Grid. Platform ini membantu pengguna "
    "menganalisis kondisi jaringan listrik secara real-time menggunakan algoritma ML."
)

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        '<div style="background:rgba(15,23,42,0.6);border:1px solid rgba(148,163,184,0.12);'
        'border-radius:10px;padding:16px 20px;">'
        '<p style="color:#94a3b8;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.1em;margin:0 0 12px">Fitur Utama</p>'
        '<p style="color:#f1f5f9;margin:6px 0">✅ Manual Prediction</p>'
        '<p style="color:#f1f5f9;margin:6px 0">✅ CSV Batch Prediction</p>'
        '<p style="color:#f1f5f9;margin:6px 0">✅ Model Comparison</p>'
        '<p style="color:#f1f5f9;margin:6px 0">✅ Download Hasil Prediksi</p>'
        '</div>',
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        '<div style="background:rgba(15,23,42,0.6);border:1px solid rgba(148,163,184,0.12);'
        'border-radius:10px;padding:16px 20px;">'
        '<p style="color:#94a3b8;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.1em;margin:0 0 12px">Konteks Proyek</p>'
        '<p style="color:#f1f5f9;margin:6px 0">📚 Mata Kuliah: Dasar Ilmu Data</p>'
        '<p style="color:#f1f5f9;margin:6px 0">🏫 Telkom University</p>'
        '<p style="color:#f1f5f9;margin:6px 0">👥 Kelompok 5</p>'
        '<p style="color:#f1f5f9;margin:6px 0">📅 2026</p>'
        '</div>',
        unsafe_allow_html=True
    )

st.markdown("---")

# DATASET
st.markdown('<p class="section-label">Dataset</p>', unsafe_allow_html=True)
st.markdown("### Dataset Information")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Data", "60,000")
c2.metric("Features", "12")
c3.metric("Target", "stabf")
c4.metric("Classes", "2")

st.write(
    "Dataset yang digunakan adalah **Smart Grid Stability Augmented Dataset**, "
    "berisi simulasi sistem jaringan listrik dengan 4 node. Target prediksi adalah "
    "label `stabf`: kondisi **stable** (stabil) atau **unstable** (tidak stabil)."
)

st.markdown("**12 Fitur Input:**")
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.code("tau1  — Waktu reaksi node 1\ntau2  — Waktu reaksi node 2\ntau3  — Waktu reaksi node 3\ntau4  — Waktu reaksi node 4")
with col_b:
    st.code("p1  — Daya node 1\np2  — Daya node 2\np3  — Daya node 3\np4  — Daya node 4")
with col_c:
    st.code("g1  — Konduktansi node 1\ng2  — Konduktansi node 2\ng3  — Konduktansi node 3\ng4  — Konduktansi node 4")

st.markdown("---")

# ML MODELS
st.markdown('<p class="section-label">Model Machine Learning</p>', unsafe_allow_html=True)
st.markdown("### Algoritma yang Digunakan")

for model, acc, desc, color in [
    ("Decision Tree", "74.0%", "Mudah diinterpretasi, cepat training, cocok untuk klasifikasi dasar.", "#f59e0b"),
    ("K-Nearest Neighbor (KNN)", "79.0%", "Klasifikasi berbasis jarak ke tetangga terdekat.", "#3b82f6"),
    ("Support Vector Machine (SVM)", "98.0%", "Performa terbaik — memisahkan kelas dengan hyperplane optimal.", "#06b6d4"),
]:
    st.markdown(
        f'<div style="background:rgba(15,23,42,0.6);border:1px solid rgba(148,163,184,0.12);'
        f'border-radius:10px;padding:14px 18px;margin:8px 0;display:flex;justify-content:space-between;align-items:center;">'
        f'<div><p style="color:#f1f5f9;font-weight:600;margin:0">{model}</p>'
        f'<p style="color:#94a3b8;font-size:0.82rem;margin:4px 0 0">{desc}</p></div>'
        f'<span style="color:{color};font-weight:700;font-size:1.1rem;font-family:monospace">{acc}</span>'
        f'</div>',
        unsafe_allow_html=True
    )

st.markdown("---")

# WORKFLOW
st.markdown('<p class="section-label">Alur Kerja</p>', unsafe_allow_html=True)
st.markdown("### Workflow")

steps = [
    ("1", "Dataset CSV", "Smart Grid Stability Augmented Dataset"),
    ("2", "Preprocessing", "Normalisasi fitur dengan StandardScaler"),
    ("3", "Train/Test Split", "80% training, 20% testing"),
    ("4", "Model Training", "Training Decision Tree, KNN, SVM"),
    ("5", "Evaluasi", "Pengukuran akurasi, precision, recall"),
    ("6", "Save Model", "Export ke file .pkl menggunakan joblib"),
    ("7", "Deploy Streamlit", "Aplikasi web interaktif siap digunakan"),
]

cols = st.columns(len(steps))
for col, (num, title, desc) in zip(cols, steps):
    col.markdown(
        f'<div style="text-align:center;">'
        f'<div style="width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#3b82f6,#06b6d4);'
        f'display:flex;align-items:center;justify-content:center;margin:0 auto 8px;font-weight:700;color:white;font-size:0.8rem">{num}</div>'
        f'<p style="color:#f1f5f9;font-size:0.8rem;font-weight:600;margin:0">{title}</p>'
        f'<p style="color:#64748b;font-size:0.7rem;margin:2px 0 0">{desc}</p>'
        f'</div>',
        unsafe_allow_html=True
    )

st.markdown("---")

# TECH STACK
st.markdown('<p class="section-label">Teknologi</p>', unsafe_allow_html=True)
st.markdown("### Technology Stack")

tc1, tc2, tc3 = st.columns(3)
with tc1:
    st.success("**Data Science**\n\nPython · Pandas · NumPy")
with tc2:
    st.info("**Machine Learning**\n\nScikit-Learn · Joblib")
with tc3:
    st.warning("**Frontend & Viz**\n\nStreamlit · Matplotlib · Seaborn")

st.markdown("---")

# TEAM
st.markdown('<p class="section-label">Tim</p>', unsafe_allow_html=True)
st.markdown("### Team Kelompok 5")

mc1, mc2, mc3 = st.columns(3)
for col, name, role in [(mc1, "Dista", "Decision Tree"), (mc2, "Piqi", "KNN"), (mc3, "Tora", "SVM")]:
    col.markdown(
        f'<div style="background:rgba(15,23,42,0.6);border:1px solid rgba(148,163,184,0.12);'
        f'border-radius:10px;padding:20px;text-align:center;">'
        f'<div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#3b82f6,#8b5cf6);'
        f'display:flex;align-items:center;justify-content:center;margin:0 auto 10px;font-size:1.2rem">👤</div>'
        f'<p style="color:#f1f5f9;font-weight:600;margin:0">{name}</p>'
        f'<p style="color:#64748b;font-size:0.78rem;margin:4px 0 0">{role}</p>'
        f'</div>',
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("⚡ SmartGrid AI Platform — Built with Streamlit & Scikit-Learn | 2026")
