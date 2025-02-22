import streamlit as st
import pickle
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from PIL import Image



# Load trained model
model_path = os.path.join('models', 'model.pkl')
model = pickle.load(open(model_path, 'rb'))
scaler_path = os.path.join('models', 'scaler.pkl')
scaler = pickle.load(open(scaler_path, 'rb'))

# Title and description
st.title("Diabetes Prediction Application")

# Banner image
st.subheader("Symptoms")
image_path = os.path.join('app', 'diabetes_banner.jpg')
st.image(image_path, use_container_width=True)

# Define reset function
def reset_inputs():
    st.session_state.Pregnancies = 0
    st.session_state.Glucose = 50
    st.session_state.BloodPressure = 50
    st.session_state.SkinThickness = 5
    st.session_state.Insulin = 0
    st.session_state.BMI = 10.0
    st.session_state.DiabetesPedigreeFunction = 0.0
    st.session_state.Age = 10

# Initialize session state for input fields
if "Pregnancies" not in st.session_state:
    reset_inputs()

# Input fields with valid ranges
Pregnancies = st.number_input('Number of times pregnant', min_value=0, max_value=20, step=1, key='Pregnancies')
Glucose = st.number_input('Plasma glucose concentration', min_value=50, max_value=200, step=1, key='Glucose')
BloodPressure = st.number_input('Diastolic blood pressure (mm Hg)', min_value=50, max_value=130, step=1, key='BloodPressure')
SkinThickness = st.number_input('Triceps skin fold thickness (mm)', min_value=5, max_value=90, step=1, key='SkinThickness')
Insulin = st.number_input('2-Hour serum insulin (mu U/ml)', min_value=0, max_value=400, step=1, key='Insulin')
BMI = st.number_input('Body mass index (weight in kg/(height in m)^2)', min_value=10.0, max_value=70.0, step=0.1, key='BMI')
DiabetesPedigreeFunction = st.number_input('Diabetes pedigree function', min_value=0.0, max_value=2.5, step=0.01, key='DiabetesPedigreeFunction')
Age = st.number_input('Age (years)', min_value=10, max_value=100, step=1, key='Age')

# Buttons for predict and clear
col1, col2 = st.columns(2)
with col1:
    state = st.button('Predict')
with col2:
    clear = st.button('Clear', on_click=reset_inputs)

# Prediction logic
if state:
    # Prepare input data
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    # Apply the same preprocessing (scaling)
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)

    # Display result
    if prediction[0] == 1:
        st.error('The prediction indicates that you may have diabetes. Please consult a healthcare professional for further advice.')
    else:
        st.success('The prediction indicates that you do not have diabetes.')

# Sidebar information
st.sidebar.title("About")
st.sidebar.info("""
This diabetes prediction model uses the Pima [Indians Diabetes dataset](https://www.kaggle.com/datasets/mathchi/diabetes-data-set/data).
""")

st.sidebar.header("How It Works")
st.sidebar.write("""
1. Enter medical data in the input fields.
2. Click the 'Predict' button to get the result.
3. Use the 'Clear' button to reset inputs.
""")

st.sidebar.header("Valid Input Ranges")
st.sidebar.write("""
- **Pregnancies**: 0 - 20
- **Glucose**: 50 - 200
- **Blood Pressure**: 50 - 130 mm Hg
- **Skin Thickness**: 5 - 90 mm
- **Insulin**: 0 - 400 mu U/ml
- **BMI**: 10.0 - 70.0
- **Diabetes Pedigree Function**: 0.0 - 2.5
- **Age**: 10 - 100 years
""")

st.sidebar.header("Developer Notes")
st.sidebar.write("""
- This application is built with Python.
- The machine learning model used was ExtraTreesClassifier.
""")

st.sidebar.header("Contact")
st.sidebar.write("""
For questions or suggestions, reach out to:
- **Email**: ahmed.hamdii.kamal@gmail.com
- **GitHub**: [hamdii10](https://github.com/hamdii10)
""")
