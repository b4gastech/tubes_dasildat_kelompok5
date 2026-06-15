import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from utils.style import load_css

load_css()

matplotlib.rcParams['figure.facecolor'] = '#0f172a'
matplotlib.rcParams['axes.facecolor'] = '#1e293b'
matplotlib.rcParams['text.color'] = '#f1f5f9'
matplotlib.rcParams['axes.labelcolor'] = '#94a3b8'
matplotlib.rcParams['xtick.color'] = '#94a3b8'
matplotlib.rcParams['ytick.color'] = '#94a3b8'
matplotlib.rcParams['axes.spines.top'] = False
matplotlib.rcParams['axes.spines.right'] = False

st.markdown('<p class="section-label">Evaluasi Model</p>', unsafe_allow_html=True)
st.title("📊 Model Performance Comparison")

# Data
data = {
    "Model": ["Decision Tree", "KNN", "SVM"],
    "Accuracy": [0.74, 0.79, 0.98],
    "Precision": [0.72, 0.77, 0.97],
    "Recall": [0.70, 0.75, 0.99],
    "F1-Score": [0.71, 0.76, 0.98],
}
df = pd.DataFrame(data)

# Summary metrics
best_idx = df["Accuracy"].idxmax()
best_model = df.loc[best_idx, "Model"]

st.markdown("---")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Best Model", best_model)
c2.metric("Best Accuracy", f"{df['Accuracy'].max()*100:.1f}%")
c3.metric("Best Precision", f"{df['Precision'].max()*100:.1f}%")
c4.metric("Best Recall", f"{df['Recall'].max()*100:.1f}%")

st.markdown("---")

# Table
st.markdown('<p class="section-label">Tabel Perbandingan</p>', unsafe_allow_html=True)
st.markdown("### Performance Metrics")

display_df = df.copy()
for col in ["Accuracy", "Precision", "Recall", "F1-Score"]:
    display_df[col] = display_df[col].apply(lambda x: f"{x*100:.1f}%")

st.dataframe(display_df, use_container_width=True, hide_index=True)

st.markdown("---")

# Charts
st.markdown('<p class="section-label">Visualisasi</p>', unsafe_allow_html=True)
st.markdown("### Perbandingan Visual")

COLORS = ['#f59e0b', '#3b82f6', '#06b6d4']
metrics = ["Accuracy", "Precision", "Recall", "F1-Score"]

ch1, ch2 = st.columns(2)

with ch1:
    # Grouped Bar Chart
    fig, ax = plt.subplots(figsize=(7, 4))
    x = np.arange(len(metrics))
    w = 0.25
    for i, (model, color) in enumerate(zip(df["Model"], COLORS)):
        vals = [df.loc[i, m] for m in metrics]
        bars = ax.bar(x + i*w, vals, w, label=model, color=color, alpha=0.9, edgecolor='none')

    ax.set_xticks(x + w)
    ax.set_xticklabels(metrics, fontsize=10)
    ax.set_ylim(0, 1.15)
    ax.set_ylabel("Score")
    ax.legend(frameon=False, fontsize=9, labelcolor='#f1f5f9')
    ax.spines['left'].set_color('#334155')
    ax.spines['bottom'].set_color('#334155')
    ax.set_title("All Metrics Comparison", color='#f1f5f9', fontsize=11, pad=10)
    fig.patch.set_facecolor('#0f172a')
    st.pyplot(fig)

with ch2:
    # Accuracy bar (highlight SVM)
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    bar_colors = ['#f59e0b' if m != best_model else '#06b6d4' for m in df["Model"]]
    bars = ax2.bar(df["Model"], df["Accuracy"], color=bar_colors, width=0.5, edgecolor='none')
    for bar, val in zip(bars, df["Accuracy"]):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, f"{val*100:.1f}%",
                 ha='center', va='bottom', color='#f1f5f9', fontweight='bold', fontsize=10)
    ax2.set_ylim(0, 1.15)
    ax2.set_ylabel("Accuracy Score")
    ax2.spines['left'].set_color('#334155')
    ax2.spines['bottom'].set_color('#334155')
    ax2.set_title("Accuracy by Model", color='#f1f5f9', fontsize=11, pad=10)
    fig2.patch.set_facecolor('#0f172a')
    st.pyplot(fig2)

# Radar chart
st.markdown("##### Radar Chart — Multi-metric Comparison")
angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False).tolist()
angles += angles[:1]

fig3, ax3 = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
ax3.set_facecolor('#1e293b')
for i, (_, row) in enumerate(df.iterrows()):
    vals = [row[m] for m in metrics] + [row[metrics[0]]]
    ax3.plot(angles, vals, 'o-', linewidth=2, color=COLORS[i], label=row["Model"])
    ax3.fill(angles, vals, alpha=0.1, color=COLORS[i])

ax3.set_thetagrids(np.degrees(angles[:-1]), metrics, color='#94a3b8', fontsize=9)
ax3.set_ylim(0, 1)
ax3.tick_params(colors='#64748b')
ax3.spines['polar'].set_color('#334155')
ax3.yaxis.set_tick_params(labelsize=7, labelcolor='#64748b')
ax3.legend(loc='upper right', bbox_to_anchor=(1.35, 1.15), frameon=False, fontsize=9, labelcolor='#f1f5f9')
fig3.patch.set_facecolor('#0f172a')
col_r = st.columns([1, 2, 1])[1]
col_r.pyplot(fig3)

st.markdown("---")

# Conclusion
st.markdown('<p class="section-label">Kesimpulan</p>', unsafe_allow_html=True)
st.markdown("### Conclusion")
st.success(
    f"**Model Terbaik: {best_model}** — Akurasi {df['Accuracy'].max()*100:.1f}%\n\n"
    f"SVM menunjukkan performa paling unggul dalam semua metrik evaluasi, "
    f"dengan kemampuan memisahkan kelas data secara lebih efektif melalui hyperplane optimal. "
    f"SVM sangat cocok untuk dataset Smart Grid yang memiliki separabilitas tinggi antar kelas."
)

st.markdown("---")
st.caption("⚡ SmartGrid AI Platform — Tubes Dasildat Kelompok 5")
