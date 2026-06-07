import pandas as pd

# Load dataset
df = pd.read_csv("../Dataset/yield_df.csv")

# Remove unwanted column
df.drop(columns=["Unnamed: 0"], inplace=True)

# Display first 5 rows
print(df.head())

# Display summary statistics
print(df.describe())

# Show actual Area and Crop names before encoding
print("\n===== AREA NAMES =====")
print(df['Area'].unique())

print("\n===== CROP NAMES =====")
print(df['Item'].unique())

# Encode text columns into numbers
from sklearn.preprocessing import LabelEncoder

le_area = LabelEncoder()
le_item = LabelEncoder()

df['Area'] = le_area.fit_transform(df['Area'])
df['Item'] = le_item.fit_transform(df['Item'])

print("\n===== ENCODED DATA =====")
print(df.head())

# Features (input columns)
X = df.drop("hg/ha_yield", axis=1)

# Target column
y = df["hg/ha_yield"]

# Split dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Train model
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    n_estimators=20,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Check accuracy
score = model.score(X_test, y_test)
print("Model Accuracy:", score)

# Save model
import pickle

with open("../Model/crop_yield_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")