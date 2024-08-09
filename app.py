import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Breast Cancer Prediction")

# Load the model and scaler
loaded_model = pickle.load(open('breastcancer.pkl', 'rb'))
sc = pickle.load(open('sc.pkl', 'rb'))

# Title and Description
st.title('Breast Cancer Prediction')
st.write(
    "This model predicts whether a patient is affected by breast cancer based on certain input features.\n\n"
    "The model was trained with high accuracy, but please note that this should not be used as a medical diagnosis. "
    "Consult a medical professional for any health concerns."
)

# Get user input
def user_input_features():
    mean_radius = st.slider("Enter Mean Radius", min_value=0.0, step=0.01)
    mean_texture = st.slider('Enter Mean Texture', min_value=0.0, step=0.01)
    mean_perimeter = st.slider('Enter Mean Perimeter', min_value=0.0, step=0.01)
    mean_area = st.slider('Enter Mean Area', min_value=0.0, step=1.0)
    mean_smoothness = st.slider('Enter Mean Smoothness', min_value=0.0, step=0.0001)

    data = {
        'mean_radius': mean_radius,
        'mean_texture': mean_texture,
        'mean_perimeter': mean_perimeter,
        'mean_area': mean_area,
        'mean_smoothness': mean_smoothness


    
    }

    input_df = pd.DataFrame(data, index=[0])
    return input_df

# Get user input
input_df = user_input_features()

# Scale the input
scaled_input = sc.transform(input_df)

# Create a button to trigger prediction
if st.button('Predict'):
    prediction = loaded_model.predict(scaled_input)

    if prediction[0] == 0:
        st.write("YOU ARE NOT AFFECTED BY BREAST CANCER")
    else:
        st.write("YOU ARE AFFECTED BY BREAST CANCER")
        st.write("Consult the Doctor! Be Strong 💪")




st.sidebar.markdown(
    "Dataset Features\n\n"
    "- **mean_radius**: The average radius of the tumor.\n"
    "- **mean_texture**: The average texture of the tumor.\n"
    "- **mean_perimeter**: The average perimeter of the tumor.\n"
    "- **mean_area**: The average area of the tumor.\n"
    "- **mean_smoothness**: The average smoothness of the tumor."
)


st.markdown("PROJECT BY : M.MANOJ BHASKAR")

