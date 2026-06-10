import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from sklearn import tree

# =========================================
# LOAD TESTING DATASET
# =========================================

data = pd.read_csv("testing_dataset.csv")

print("====================================")
print("TESTING DATASET LOADED SUCCESSFULLY")
print("====================================")
print(data.head())
print("\nTotal testing records:", len(data))

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
        raise ValueError(f"Missing column in testing_dataset.csv: {col}")

# =========================================
# LOAD MODEL AND ENCODERS
# =========================================

model = joblib.load("scholarmatch_model.pkl")
le_income = joblib.load("le_income.pkl")
le_programme = joblib.load("le_programme.pkl")
le_recommend = joblib.load("le_recommend.pkl")

print("\nMODEL TYPE:", type(model))

print("\nRecommendation classes:")
print(list(le_recommend.classes_))

# =========================================
# ENCODE TESTING DATA
# =========================================

data["Income Level"] = le_income.transform(data["Income Level"])
data["Kulliyyah"] = le_programme.transform(data["Kulliyyah"])
data["Recommended"] = le_recommend.transform(data["Recommended"])

# =========================================
# FEATURES AND TARGET
# IMPORTANT: same order as train_model.py and app.py
# =========================================

X_test = data[["GPA", "Income (RM)", "COCU", "Kulliyyah", "Year"]]
y_test = data["Recommended"]

# =========================================
# PREDICTION
# =========================================

y_pred = model.predict(X_test)

# Convert encoded labels back to readable labels
actual_labels = le_recommend.inverse_transform(y_test)
predicted_labels = le_recommend.inverse_transform(y_pred)

result_df = pd.DataFrame({
    "Actual": actual_labels,
    "Predicted": predicted_labels
})

print("\n====================================")
print("ACTUAL VS PREDICTED RESULTS")
print("====================================")
print(result_df)

print("\nPrediction distribution:")
print(result_df["Predicted"].value_counts())

# =========================================
# EVALUATION
# =========================================

accuracy = accuracy_score(y_test, y_pred)

print("\n====================================")
print("MODEL ACCURACY")
print("====================================")
print("Accuracy:", round(accuracy * 100, 2), "%")

print("\n====================================")
print("CLASSIFICATION REPORT")
print("====================================")
print(classification_report(
    y_test,
    y_pred,
    target_names=le_recommend.classes_
))

# =========================================
# 1. CONFUSION MATRIX
# =========================================

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=le_recommend.classes_
)

disp.plot(cmap=plt.cm.Blues, values_format="d")
plt.title("Confusion Matrix - ScholarMatch Model")
plt.show()

# =========================================
# 2. PREDICTION DISTRIBUTION BAR CHART
# =========================================

prediction_counts = result_df["Predicted"].value_counts()

plt.figure(figsize=(7, 5))
plt.bar(prediction_counts.index, prediction_counts.values)

plt.title("Prediction Distribution of Scholarships")
plt.xlabel("Scholarship")
plt.ylabel("Number of Predictions")

for i, value in enumerate(prediction_counts.values):
    plt.text(i, value + 0.2, str(value), ha="center")

plt.show()

# =========================================
# 3. DECISION TREE VISUALIZATION
# =========================================

plt.figure(figsize=(20, 10))

tree.plot_tree(
    model,
    feature_names=X_test.columns,
    class_names=le_recommend.classes_,
    filled=True,
    rounded=True,
    fontsize=9
)

plt.title("ScholarMatch Decision Tree Visualization")
plt.show()

# =========================================
# 4. CLASSIFICATION REPORT VISUALIZATION
# =========================================

report = classification_report(
    y_test,
    y_pred,
    target_names=le_recommend.classes_,
    output_dict=True
)

df_report = pd.DataFrame(report).transpose()

metrics = ["precision", "recall", "f1-score"]
class_report = df_report.loc[le_recommend.classes_, metrics]

plt.figure(figsize=(8, 5))
plt.imshow(class_report, aspect="auto")

plt.xticks(range(len(metrics)), metrics)
plt.yticks(range(len(class_report.index)), class_report.index)

for i in range(len(class_report.index)):
    for j in range(len(metrics)):
        plt.text(j, i, round(class_report.iloc[i, j], 2),
                 ha="center", va="center")

plt.colorbar()
plt.title("Classification Report Heatmap")
plt.show()