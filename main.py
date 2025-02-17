import pickle
import streamlit as st
import pandas as pd

# Load the model
model = pickle.load(open('heart_disease_prediction_model.sav', 'rb'))

st.title('Heart Disease Prediction System')

# Get user input
st.subheader('🧑‍⚕️ Enter Patient Data')

def get_user_input():

     # Divide into columns
    col1, _, col2 = st.columns([1, 0.3, 1])

    with col1:
        age = st.number_input('Age', 20, 80, 50)
        sex = st.selectbox('Sex', ('Male', 'Female'))
        cp = st.slider('Chest Pain Type', 0, 3, 1)
        trestbps = st.number_input('Resting Blood Pressure(in mm Hg)', 80, 200, 120)
        chol = st.number_input('Serum Cholesterol(in mg/dl)', 120, 400, 200)
     
    with col2:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', (0, 1))
        thalach = st.number_input('Max Heart Rate Achieved', 60, 200, 150)
        restecg = st.slider('Resting ECG', 0, 2, 1)
        exang = st.selectbox('Exercise Induced Angina', ('Yes', 'No'))
        oldpeak = st.number_input('ST Depression', 0.0, 5.0, 2.0, step=0.1)
        oldpeak = round(oldpeak, 2) 
        
    # Add another row for remaining inputs
    slope = st.slider('Slope of the peak exercise ST segment', 0, 2, 0)
    ca = st.slider('Number of major vessels colored by flourosopy', 0, 4, 0)
    thal = st.slider('Thalassemia', 0, 3, 0)

    # Create a dataframe for the input
    user_data = {
        'age': age,
        'sex': 1 if sex == 'Male' else 0,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'thalach': thalach,
        'restecg': restecg,
        'exang': 1 if exang == 'Yes' else 0,
        'oldpeak': f"{oldpeak:.2f}",
        'slope': slope,
        'ca': ca,
        'thal': thal
    }

    features = pd.DataFrame(user_data, index=[0])
    return features

# Display user input
user_input = get_user_input()
st.subheader('📊 Patient Data Overview')
st.write(user_input)

if st.button("🔍 Predict"):
 
    # Predict using the model
    prediction = model.predict(user_input)

    # Display Prediction Results
    st.subheader('🧑‍⚕️ Prediction Result')

    if prediction[0] == 0:
        st.markdown('<p style="color:green; font-size: 24px; font-weight:bold; "> The Person do not have a heart disease 😊💚 </p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="color:red; font-size: 24px; font-weight:bold;"> The Person have a heart disease ☹️❤️ </p>', unsafe_allow_html=True)
