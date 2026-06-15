import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Fitur lengkap (12) - untuk DT dan SVM
FITUR_12 = ['tau1','tau2','tau3','tau4','p1','p2','p3','p4','g1','g2','g3','g4']

# Fitur KNN (11) - tau1 tidak dipakai saat training KNN
FITUR_KNN = ['tau2','tau3','tau4','p1','p2','p3','p4','g1','g2','g3','g4']

def safe_load(filename):
    path = os.path.join(MODEL_DIR, filename)
    if os.path.exists(path):
        try:
            return joblib.load(path)
        except Exception as e:
            print(f"Warning: failed to load {filename}: {e}")
            return None
    return None

def load_models():
    dt  = safe_load("decision_tree_model.pkl")
    knn = safe_load("knn_model.pkl")
    svm = safe_load("svm_model.pkl")
    return dt, knn, svm

def load_scaler():
    return safe_load("scaler.pkl")
