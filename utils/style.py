import streamlit as st

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;700&display=swap');

    /* ===== ROOT ===== */
    :root {
        --bg-primary: #020617;
        --bg-card: rgba(15, 23, 42, 0.8);
        --bg-card-hover: rgba(30, 41, 59, 0.9);
        --accent-cyan: #06b6d4;
        --accent-blue: #3b82f6;
        --accent-violet: #8b5cf6;
        --accent-green: #10b981;
        --accent-red: #ef4444;
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
        --border: rgba(148, 163, 184, 0.12);
        --glow-cyan: 0 0 20px rgba(6, 182, 212, 0.25);
        --glow-blue: 0 0 20px rgba(59, 130, 246, 0.25);
    }

    /* ===== GLOBAL ===== */
    .stApp {
        background: radial-gradient(ellipse at top, #0f1e3d 0%, #020617 50%);
        font-family: 'Inter', sans-serif;
        color: var(--text-primary);
    }

    #MainMenu, footer, header { visibility: hidden; }

    /* ===== SIDEBAR ===== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1b2a 0%, #050d1a 100%);
        border-right: 1px solid var(--border);
    }

    section[data-testid="stSidebar"] .stRadio label {
        color: var(--text-secondary) !important;
        font-size: 0.875rem;
        padding: 6px 0;
        transition: color 0.2s;
    }

    /* ===== HEADINGS ===== */
    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: var(--text-primary) !important;
        letter-spacing: -0.02em;
    }

    /* ===== METRIC CARDS ===== */
    [data-testid="metric-container"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
        padding: 16px !important;
        backdrop-filter: blur(12px);
        transition: border-color 0.2s, box-shadow 0.2s;
    }
    [data-testid="metric-container"]:hover {
        border-color: var(--accent-cyan) !important;
        box-shadow: var(--glow-cyan);
    }
    [data-testid="stMetricValue"] {
        color: var(--accent-cyan) !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
    }
    [data-testid="stMetricLabel"] {
        color: var(--text-secondary) !important;
        font-size: 0.75rem !important;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    /* ===== BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, var(--accent-blue), var(--accent-cyan)) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        padding: 10px 24px !important;
        transition: opacity 0.2s, transform 0.2s !important;
        letter-spacing: 0.02em;
    }
    .stButton > button:hover {
        opacity: 0.9 !important;
        transform: translateY(-1px) !important;
        box-shadow: var(--glow-blue) !important;
    }

    /* ===== INPUTS ===== */
    .stNumberInput input, .stTextInput input {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid var(--border) !important;
        color: var(--text-primary) !important;
        border-radius: 8px !important;
        transition: border-color 0.2s;
    }
    .stNumberInput input:focus, .stTextInput input:focus {
        border-color: var(--accent-cyan) !important;
        box-shadow: 0 0 0 2px rgba(6, 182, 212, 0.15) !important;
    }

    /* ===== DATAFRAME ===== */
    .stDataFrame {
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        overflow: hidden;
    }

    /* ===== ALERTS ===== */
    .stSuccess {
        background: rgba(16, 185, 129, 0.1) !important;
        border: 1px solid rgba(16, 185, 129, 0.3) !important;
        border-radius: 10px !important;
        color: #6ee7b7 !important;
    }
    .stError {
        background: rgba(239, 68, 68, 0.1) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
        border-radius: 10px !important;
    }
    .stInfo {
        background: rgba(59, 130, 246, 0.1) !important;
        border: 1px solid rgba(59, 130, 246, 0.3) !important;
        border-radius: 10px !important;
        color: #93c5fd !important;
    }
    .stWarning {
        background: rgba(245, 158, 11, 0.1) !important;
        border: 1px solid rgba(245, 158, 11, 0.3) !important;
        border-radius: 10px !important;
    }

    /* ===== EXPANDER ===== */
    .streamlit-expanderHeader {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        color: var(--text-secondary) !important;
    }

    /* ===== DIVIDER ===== */
    hr {
        border-color: var(--border) !important;
        margin: 1.5rem 0 !important;
    }

    /* ===== CAPTION ===== */
    .stCaption {
        color: var(--text-secondary) !important;
        font-size: 0.75rem;
    }

    /* ===== SELECTBOX ===== */
    .stSelectbox > div > div {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
    }

    /* ===== FILE UPLOADER ===== */
    [data-testid="stFileUploader"] {
        background: rgba(15, 23, 42, 0.5) !important;
        border: 1.5px dashed var(--border) !important;
        border-radius: 10px !important;
        transition: border-color 0.2s;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: var(--accent-cyan) !important;
    }

    /* ===== CUSTOM COMPONENTS ===== */
    .stat-badge {
        display: inline-block;
        background: linear-gradient(135deg, rgba(6,182,212,0.15), rgba(59,130,246,0.15));
        border: 1px solid rgba(6,182,212,0.3);
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.75rem;
        font-weight: 600;
        color: var(--accent-cyan);
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }

    .result-card-stable {
        background: linear-gradient(135deg, rgba(16,185,129,0.12), rgba(6,182,212,0.08));
        border: 1.5px solid rgba(16,185,129,0.35);
        border-radius: 16px;
        padding: 24px 28px;
        text-align: center;
        margin-top: 16px;
    }
    .result-card-stable h2 {
        color: #6ee7b7 !important;
        font-size: 2rem !important;
        margin: 0 !important;
    }

    .result-card-unstable {
        background: linear-gradient(135deg, rgba(239,68,68,0.12), rgba(245,158,11,0.08));
        border: 1.5px solid rgba(239,68,68,0.35);
        border-radius: 16px;
        padding: 24px 28px;
        text-align: center;
        margin-top: 16px;
    }
    .result-card-unstable h2 {
        color: #fca5a5 !important;
        font-size: 2rem !important;
        margin: 0 !important;
    }

    .section-label {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--accent-cyan);
        font-weight: 600;
        margin-bottom: 4px;
    }

    .team-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 12px 16px;
        margin: 6px 0;
        color: var(--text-secondary);
        font-size: 0.85rem;
        transition: border-color 0.2s;
    }
    .team-card:hover {
        border-color: rgba(6,182,212,0.4);
    }
    </style>
    """, unsafe_allow_html=True)
