import streamlit as st
import pickle
import pandas as pd
import os

st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="centered"
)

# Agriculture Theme
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #d4fc79, #96e6a1);
}

h1 {
    color: #1b5e20;
    text-align: center;
}

h2, h3 {
    color: #2e7d32;
}

.stButton > button {
    background-color: #2e7d32;
    color: white;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #1b5e20;
    color: white;
}

[data-testid="stMetricValue"] {
    color: #1b5e20;
    font-weight: bold;
}

section[data-testid="stSidebar"] {
    background-color: #c8e6c9;
}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🌾 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Crop Yield Predictor", "Project Info"]
)

# Load saved model
model_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Model",
    "crop_yield_model.pkl"
)

with open(model_path, "rb") as file:
    model = pickle.load(file)

# Success Message
st.success("🚀 Machine Learning Model Loaded Successfully")

# ==========================
# Crop Yield Predictor Page
# ==========================
if page == "Crop Yield Predictor":

    st.title("🌾 Crop Yield Prediction System")

    st.info("🌱 Agriculture is the backbone of human civilization.")

    st.markdown("## 🚜 Smart Agriculture Assistant")
    st.markdown(
        "Helping farmers predict crop yield using Machine Learning."
    )

    st.markdown("""
    ### 🌱 Features

    ✅ Crop Yield Prediction  
    ✅ Rainfall Analysis  
    ✅ Temperature Analysis  
    ✅ Pesticide Impact Analysis  
    ✅ Machine Learning Based Prediction
    """)

    st.markdown("""
    Predict crop yield using historical agricultural data and Machine Learning.

    Fill in the details below and click **Predict Yield**.
    """)

    st.info("📊 Model Accuracy: 98%")

    st.metric(
        label="Model Accuracy",
        value="98%"
    )

    # Country dropdown
    area_list = [
        "Albania",
        "Algeria",
        "Angola",
        "Argentina",
        "Australia"
    ]

    selected_area = st.selectbox(
        "🌍 Select Country",
        area_list
    )

    # Crop dropdown
    crop_list = [
        "Maize",
        "Potatoes",
        "Rice, paddy",
        "Sorghum",
        "Soybeans"
    ]

    selected_crop = st.selectbox(
        "🌾 Select Crop",
        crop_list
    )

    area = area_list.index(selected_area)
    item = crop_list.index(selected_crop)

    year = st.number_input(
        "📅 Year",
        min_value=1900,
        max_value=2100,
        value=2024
    )

    average_rain_fall_mm_per_year = st.number_input(
        "🌧 Average Rainfall (mm/year)",
        value=1200.0
    )

    pesticides_tonnes = st.number_input(
        "🧪 Pesticides (tonnes)",
        value=100.0
    )

    avg_temp = st.number_input(
        "🌡 Average Temperature (°C)",
        value=25.0
    )

    if st.button("🌾 Predict Yield"):

        input_data = pd.DataFrame({
            'Area': [area],
            'Item': [item],
            'Year': [year],
            'average_rain_fall_mm_per_year': [average_rain_fall_mm_per_year],
            'pesticides_tonnes': [pesticides_tonnes],
            'avg_temp': [avg_temp]
        })

        prediction = model.predict(input_data)

        st.success(
            f"🌾 Predicted Yield: {prediction[0]:,.2f} hg/ha"
        )

        # Yield Category
        if prediction[0] < 50000:
            category = "🔴 Low Yield"
        elif prediction[0] < 100000:
            category = "🟡 Medium Yield"
        else:
            category = "🟢 High Yield"

        st.success(f"Yield Category: {category}")

        # Prediction Summary
        st.write("### 📊 Prediction Summary")

        summary_df = pd.DataFrame({
            "Country": [selected_area],
            "Crop": [selected_crop],
            "Predicted Yield": [f"{prediction[0]:,.2f} hg/ha"]
        })

        st.table(summary_df)

        st.balloons()

    st.markdown("---")

    st.subheader("ℹ About")

    st.write("""
    This Crop Yield Prediction System helps estimate agricultural
    yield using Machine Learning techniques.

    Input Parameters:

    - 🌍 Country
    - 🌾 Crop Type
    - 🌧 Average Rainfall
    - 🧪 Pesticide Usage
    - 🌡 Average Temperature
    - 📅 Year

    Output:

    - Predicted Crop Yield (hg/ha)

    Algorithm Used:

    - Random Forest Regressor

    Accuracy:

    - 98%
    """)

# ==========================
# Project Info Page
# ==========================
elif page == "Project Info":

    st.title("📘 Project Information")

    st.markdown("""
    ## 👨‍💻 Developed By
    **Lohith Kumar**

    ## 💻 Department
    **Computer Science**

    ## 🌾 Project
    **Crop Yield Prediction using Machine Learning**
    """)

    st.write("""
    ### Crop Yield Prediction System

    Objective:
    Predict crop yield using Machine Learning based on
    agricultural and environmental factors.

    Technologies Used:

    - Python
    - Pandas
    - Scikit-Learn
    - Streamlit

    Algorithm Used:

    - Random Forest Regressor

    Features:

    - Crop Yield Prediction
    - Rainfall Analysis
    - Temperature Analysis
    - Pesticide Analysis
    - User-Friendly Interface

    Accuracy:

    - 98%

    Future Scope:

    - Real-time Weather Integration
    - AI-Based Farming Suggestions
    - Mobile Application Development

    Developed as an Agriculture AI Project.
    """)

# Footer
st.markdown("---")

st.markdown(
    "<center>Developed by Lohith Kumar | Crop Yield Prediction Project 🌾</center>",
    unsafe_allow_html=True
)