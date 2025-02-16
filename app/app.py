import streamlit as st
import pickle
import os
from PIL import Image

#the two lines below for streamlit online (anyone can access)
model_path = os.path.join('models', 'model.pkl')
model = pickle.load(open(model_path, 'rb'))


st.title("Diabetes Prediction Application")
st.write("""
This application predicts whether a person is likely to have diabetes based on medical information. 
Please fill in the details below and click 'Predict'.
""")

# Define a reset function
def reset_inputs():
    st.session_state.Pregnancies = 0
    st.session_state.Glucose = 0
    st.session_state.BloodPressure = 0
    st.session_state.SkinThickness = 0
    st.session_state.Insulin = 0
    st.session_state.BMI = 0.0
    st.session_state.DiabetesPedigreeFunction = 0.0
    st.session_state.Age = 0

# Initialize session state for input fields
if "Pregnancies" not in st.session_state:
    reset_inputs()

# Input fields with specific valid ranges
Pregnancies = st.number_input('Number of times pregnant', min_value=0, max_value=20, step=1, key='Pregnancies')
Glucose = st.number_input('Plasma glucose concentration', min_value=50, max_value=200, step=1, key='Glucose')
BloodPressure = st.number_input('Diastolic blood pressure (mm Hg)', min_value=50, max_value=130, step=1, key='BloodPressure')
SkinThickness = st.number_input('Triceps skin fold thickness (mm)', min_value=5, max_value=80, step=1, key='SkinThickness')
Insulin = st.number_input('2-Hour serum insulin (mu U/ml)', min_value=0, max_value=400, step=1, key='Insulin')
BMI = st.number_input('Body mass index (weight in kg/(height in m)^2)', min_value=10.0, max_value=50.0, step=0.1, key='BMI')
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
    pred = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    if pred[0] == 1:
        st.error('The prediction indicates that you may have diabetes. Please consult a healthcare professional for further advice.')
    else:
        st.success('The prediction indicates that you do not have diabetes.')



# Symptoms Button with modal popup
if st.button("Symptoms"):
    with st.expander("Diabetes Symptoms"):
        symptoms_image_path = os.path.join('app', 'diabetes_symptoms.jpg')
        st.image(symptoms_image_path, use_container_width =True)

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
- **Skin Thickness**: 5 - 80 mm
- **Insulin**: 0 - 400 mu U/ml
- **BMI**: 10.0 - 50.0
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
