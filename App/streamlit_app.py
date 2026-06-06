import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="centered"
)

# Sidebar Navigation
st.sidebar.title("🌾 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Crop Yield Predictor", "Project Info"]
)

# Load saved model
with open("../Model/crop_yield_model.pkl", "rb") as file:
    model = pickle.load(file)

# ==========================
# Crop Yield Predictor Page
# ==========================
if page == "Crop Yield Predictor":

    st.title("🌾 Crop Yield Prediction System")

    st.markdown("""
    ### 🌱 Smart Agriculture Assistant

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
        "Country",
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
        "Crop",
        crop_list
    )

    # Convert selections to encoded values
    area = area_list.index(selected_area)
    item = crop_list.index(selected_crop)

    # Other inputs
    year = st.number_input(
        "Year",
        min_value=1900,
        max_value=2100,
        value=2024
    )

    average_rain_fall_mm_per_year = st.number_input(
        "Average Rainfall (mm/year)",
        value=1200.0
    )

    pesticides_tonnes = st.number_input(
        "Pesticides (tonnes)",
        value=100.0
    )

    avg_temp = st.number_input(
        "Average Temperature (°C)",
        value=25.0
    )

    # Prediction button
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

        st.balloons()

    st.markdown("---")

    st.subheader("ℹ About")

    st.write("""
    This Crop Yield Prediction System uses Machine Learning
    to estimate agricultural yield based on:

    - Country
    - Crop Type
    - Rainfall
    - Temperature
    - Pesticide Usage
    - Year

    Built using Python, Scikit-Learn and Streamlit.
    """)

    st.markdown("---")

    st.markdown(
        """
        <center>
        Developed by Lohith Kumar 🚀<br>
        Crop Yield Prediction System using Machine Learning
        </center>
        """,
        unsafe_allow_html=True
    )

# ==========================
# Project Info Page
# ==========================
elif page == "Project Info":

    st.title("📘 Project Information")

    st.write("""
    ### Crop Yield Prediction System

    This project predicts crop yield using Machine Learning.

    Technologies Used:

    - Python
    - Pandas
    - Scikit-Learn
    - Streamlit

    Developed as an Agriculture AI Project.
    """)

    st.markdown("---")

    st.markdown(
        """
        <center>
        Developed by Lohith Kumar 🚀<br>
        Crop Yield Prediction System using Machine Learning
        </center>
        """,
        unsafe_allow_html=True
    )