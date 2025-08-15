import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load("heart_disease_model.pkl")

# Model accuracy (set from your training results)
MODEL_ACCURACY = 0.90  # change to your best score

# App title
st.set_page_config(page_title="Heart Disease Prediction", layout="centered")
st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient details below to check the risk of heart disease.")

# User inputs with explanations
age = st.slider("Age", 18, 100, 45, help="Patient's age in years.")
sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male", help="0 = Female, 1 = Male")
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3], 
                  format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"][x],
                  help="Chest pain type experienced by the patient.")
trtbps = st.slider("Resting Blood Pressure (trtbps)", 80, 200, 120, help="Resting blood pressure in mm Hg.")
chol = st.slider("Cholesterol (chol)", 100, 600, 200, help="Serum cholesterol in mg/dl.")
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2], 
                       format_func=lambda x: ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"][x])
thalachh = st.slider("Max Heart Rate Achieved (thalachh)", 60, 220, 150)
exng = st.selectbox("Exercise Induced Angina (exng)", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
oldpeak = st.slider("ST Depression (oldpeak)", 0.0, 6.0, 1.0, 0.1, help="ST depression induced by exercise relative to rest.")
slp = st.selectbox("Slope of Peak Exercise ST Segment (slp)", [0, 1, 2], 
                   format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x])
caa = st.slider("Number of Major Vessels Colored by Fluoroscopy (caa)", 0, 4, 0)
thall = st.selectbox("Thalassemia (thall)", [0, 1, 2, 3], 
                     format_func=lambda x: ["Unknown", "Normal", "Fixed Defect", "Reversible Defect"][x])

# Convert inputs to array
input_data = np.array([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh,
                        exng, oldpeak, slp, caa, thall]])

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)

    st.subheader("📊 Prediction Result")
    if prediction[0] == 1:
        st.error(f"High risk of heart disease with probability {proba[0][1]*100:.2f}%")
    else:
        st.success(f"Low risk of heart disease with probability {proba[0][0]*100:.2f}%")

    st.info(f"🔍 Model Accuracy: {MODEL_ACCURACY*100:.2f}% (based on training data)")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and XGBoost")
