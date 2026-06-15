import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

from utils.style import load_css
from utils.model_loader import load_models, load_scaler, FITUR_12, FITUR_KNN

load_css()

@st.cache_resource
def get_models():
    dt, knn, svm = load_models()
    scaler = load_scaler()
    return dt, knn, svm, scaler

dt, knn, svm, scaler = get_models()

def predict(input_df, model_name):
    if model_name == "Decision Tree":
        return dt.predict(input_df[FITUR_12])[0]
    elif model_name == "KNN":
        m = knn if knn else dt
        if knn:
            scaled = pd.DataFrame(scaler.transform(input_df[FITUR_12]), columns=FITUR_12)
            return knn.predict(scaled[FITUR_KNN])[0]
        return dt.predict(input_df[FITUR_12])[0]
    elif model_name == "SVM":
        if svm:
            return svm.predict(scaler.transform(input_df[FITUR_12]))[0]
        return dt.predict(input_df[FITUR_12])[0]

def is_stable(pred):
    return str(pred).strip().lower() in ["stable","1","1.0"] or pred == 1

MODEL_ACC = {"Decision Tree": "74.0%", "KNN": "79.0%", "SVM": "98.0%"}

st.markdown('<p class="section-label">Prediksi Manual</p>', unsafe_allow_html=True)
st.title("🔍 Manual Prediction")

st.sidebar.markdown('<p class="section-label">Model</p>', unsafe_allow_html=True)
opts = []
if dt:  opts.append("Decision Tree")
if knn: opts.append("KNN")
if svm: opts.append("SVM")
model_name = st.sidebar.radio("Pilih Model", opts or ["Decision Tree"], label_visibility="collapsed")
st.info(f"Model aktif: **{model_name}** — Akurasi: **{MODEL_ACC[model_name]}**")

st.markdown("---")
st.markdown("##### Parameter Waktu Reaksi (tau)")
c1,c2,c3,c4 = st.columns(4)
tau1=c1.number_input("TAU1",value=0.0,format="%.4f")
tau2=c2.number_input("TAU2",value=0.0,format="%.4f")
tau3=c3.number_input("TAU3",value=0.0,format="%.4f")
tau4=c4.number_input("TAU4",value=0.0,format="%.4f")

st.markdown("##### Parameter Daya (p)")
c1,c2,c3,c4 = st.columns(4)
p1=c1.number_input("P1",value=0.0,format="%.4f")
p2=c2.number_input("P2",value=0.0,format="%.4f")
p3=c3.number_input("P3",value=0.0,format="%.4f")
p4=c4.number_input("P4",value=0.0,format="%.4f")

st.markdown("##### Parameter Konduktansi (g)")
c1,c2,c3,c4 = st.columns(4)
g1=c1.number_input("G1",value=0.0,format="%.4f")
g2=c2.number_input("G2",value=0.0,format="%.4f")
g3=c3.number_input("G3",value=0.0,format="%.4f")
g4=c4.number_input("G4",value=0.0,format="%.4f")

st.markdown("---")
if st.button("🚀 Prediksi Sekarang", use_container_width=True):
    input_df = pd.DataFrame([[tau1,tau2,tau3,tau4,p1,p2,p3,p4,g1,g2,g3,g4]], columns=FITUR_12)
    hasil = predict(input_df, model_name)
    if is_stable(hasil):
        st.markdown(
            '<div class="result-card-stable">'
            '<p style="color:#94a3b8;margin:0 0 8px;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.1em">Hasil Prediksi</p>'
            '<h2>✅ STABLE</h2>'
            '<p style="color:#6ee7b7;margin:8px 0 0">Jaringan listrik dalam kondisi stabil</p>'
            '</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div class="result-card-unstable">'
            '<p style="color:#94a3b8;margin:0 0 8px;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.1em">Hasil Prediksi</p>'
            '<h2>⚠️ UNSTABLE</h2>'
            '<p style="color:#fca5a5;margin:8px 0 0">Jaringan listrik dalam kondisi tidak stabil!</p>'
            '</div>', unsafe_allow_html=True)
    st.caption(f"Raw output: `{hasil}` | Model: {model_name}")

st.markdown("---")
st.caption("⚡ SmartGrid AI Platform — Tubes Dasildat Kelompok 5")
