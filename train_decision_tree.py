import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# =====================
# LOAD DATA
# =====================

df = pd.read_csv(
    "data/smart_grid_stability_augmented.csv"
)

print(df.head())

print("\nColumns:")
print(df.columns)

print("\nLabel Distribution:")
print(df["stabf"].value_counts())

# =====================
# FEATURES
# =====================

features = [

    "tau1","tau2","tau3","tau4",

    "p1","p2","p3","p4",

    "g1","g2","g3","g4"

]

X = df[features]

y = df["stabf"].map(

    lambda x: 1 if x=="stable" else 0

)

# =====================
# SPLIT DATA
# =====================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)

# =====================
# TRAIN MODEL
# =====================

model = DecisionTreeClassifier(

    max_depth=10,

    random_state=42

)

model.fit(

    X_train,

    y_train

)

# =====================
# TEST MODEL
# =====================

pred = model.predict(

    X_test

)

acc = accuracy_score(

    y_test,

    pred

)

print("\nAccuracy : ", acc)

print("\nPrediction Distribution:")

print(

    pd.Series(pred).value_counts()

)

# =====================
# SAVE MODEL
# =====================

joblib.dump(

    model,

    "models/decision_tree_model.pkl"

)

print("\nModel saved successfully!")