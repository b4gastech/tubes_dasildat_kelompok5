# SmartGrid AI Platform
**Tubes Dasildat Kelompok 5** — Telkom University 2026

## Cara Menjalankan

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Struktur Folder

```
tubes_dasildat_kelompok5/
├── app.py                    # Main app (Home, Prediksi Manual, Analisis CSV)
├── requirements.txt
├── pages/
│   ├── about_project.py      # Info proyek
│   ├── manual_prediction.py  # Prediksi satu data
│   ├── batch_prediction.py   # Prediksi CSV batch
│   └── model_comparison.py   # Perbandingan model
├── models/
│   ├── decision_tree_model.pkl
│   ├── knn_model.pkl
│   ├── svm_model.pkl
│   └── scaler.pkl
└── utils/
    ├── style.py              # CSS dark theme
    └── model_loader.py       # Helper load model
```

## Tim
- Dista
- Piqi  
- Tora
