import numpy as np
import pandas as pd
import pickle
import streamlit as st

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Load the model and scaler
loaded_model = pickle.load(open('breastcancer.pkl', 'rb'))
sc = pickle.load(open('sc.pkl', 'rb'))


# Page title and description
st.title("🩺 Breast Cancer Prediction")
st.markdown(
    """
    <div style="text-align: center; font-size: 18px; color: #555;">
        This model predicts whether a patient is affected by breast cancer based on certain input features.<br>
        <b>Note:</b> This is not a medical diagnosis tool. Always consult a medical professional for health concerns.
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar with additional information
with st.sidebar:
    st.markdown(
        """
        ### Dataset Features:
        - **mean_radius**: Average radius of the tumor.
        - **mean_texture**: Average texture of the tumor.
        - **mean_perimeter**: Average perimeter of the tumor.
        - **mean_area**: Average area of the tumor.
        - **mean_smoothness**: Average smoothness of the tumor.
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "<hr style='border: 1px solid #ddd;'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="text-align: center;">
            <b>Project by:</b> <br>
            <span style="font-size: 16px;">M. Manoj Bhaskar</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# User input function
def user_input_features():
    st.markdown("<h3 style='text-align: center; color: #333;'>Enter Patient Details</h3>", unsafe_allow_html=True)
    mean_radius = st.number_input("Mean Radius", min_value=0.0, step=0.01, value=0.0)
    mean_texture = st.number_input("Mean Texture", min_value=0.0, step=0.01, value=0.0)
    mean_perimeter = st.number_input("Mean Perimeter", min_value=0.0, step=0.01, value=0.0)
    mean_area = st.number_input("Mean Area", min_value=0.0, step=1.0, value=0.0)
    mean_smoothness = st.number_input("Mean Smoothness", min_value=0.0, step=0.0001, value=0.0)

    data = {
        "mean_radius": mean_radius,
        "mean_texture": mean_texture,
        "mean_perimeter": mean_perimeter,
        "mean_area": mean_area,
        "mean_smoothness": mean_smoothness,
    }
    return pd.DataFrame(data, index=[0])

# Get user input
input_df = user_input_features()

# Scale the input
scaled_input = sc.transform(input_df)

# Create a button to trigger prediction
if st.button("🔍 Predict"):
    prediction = loaded_model.predict(scaled_input)
    if prediction[0] == 0:
        st.success("✅ YOU ARE NOT AFFECTED BY BREAST CANCER")
        st.balloons()
    else:
        st.error("⚠️ YOU ARE AFFECTED BY BREAST CANCER")
        st.markdown(
            """
            <div style="text-align: center; font-size: 16px; color: red;">
                Consult a doctor immediately. Stay strong 💪.
            </div>
            """,
            unsafe_allow_html=True,
        )
markdown("PROJECT BY : M.MANOJ BHASKAR")

