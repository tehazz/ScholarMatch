import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# =========================================
# LOAD TRAINING DATASET
# =========================================

data = pd.read_csv("dataset.csv")

print("====================================")
print("TRAINING DATASET LOADED SUCCESSFULLY")
print("====================================")
print(data.head())
print("\nTotal training records:", len(data))

# =========================================
# CHECK REQUIRED COLUMNS
# =========================================

required_columns = [
    "ID",
    "GPA",
    "Income (RM)",
    "Income Level",
    "COCU",
    "Kulliyyah",
    "Year",
    "Recommended"
]

for col in required_columns:
    if col not in data.columns:
        raise ValueError(f"Missing column in dataset.csv: {col}")

# =========================================
# SHOW ORIGINAL DISTRIBUTION
# =========================================

print("\nScholarship distribution before encoding:")
print(data["Recommended"].value_counts())

print("\nKulliyyah distribution:")
print(data["Kulliyyah"].value_counts())

# =========================================
# LABEL ENCODING
# =========================================

le_income = LabelEncoder()
le_programme = LabelEncoder()
le_recommend = LabelEncoder()

data["Income Level"] = le_income.fit_transform(data["Income Level"])
data["Kulliyyah"] = le_programme.fit_transform(data["Kulliyyah"])
data["Recommended"] = le_recommend.fit_transform(data["Recommended"])

# =========================================
# FEATURES AND TARGET
# IMPORTANT: this order must match app.py and test_model.py
# =========================================

X = data[["GPA", "Income (RM)", "COCU", "Kulliyyah", "Year"]]
y = data["Recommended"]

# =========================================
# TRAIN DECISION TREE MODEL
# =========================================

model = DecisionTreeClassifier(
    random_state=42,
    class_weight="balanced",
    max_depth=5
)

model.fit(X, y)

# =========================================
# SAVE MODEL AND ENCODERS
# =========================================

joblib.dump(model, "scholarmatch_model.pkl")
joblib.dump(le_income, "le_income.pkl")
joblib.dump(le_programme, "le_programme.pkl")
joblib.dump(le_recommend, "le_recommend.pkl")

# =========================================
# FINAL OUTPUT
# =========================================

print("\n====================================")
print("MODEL TRAINED SUCCESSFULLY")
print("====================================")
print("TOTAL TRAINING DATA:", len(X))

print("\nIncome Level classes:")
print(list(le_income.classes_))

print("\nKulliyyah classes:")
print(list(le_programme.classes_))

print("\nRecommendation classes:")
print(list(le_recommend.classes_))

print("\nModel files saved:")
print("- scholarmatch_model.pkl")
print("- le_income.pkl")
print("- le_programme.pkl")
print("- le_recommend.pkl")