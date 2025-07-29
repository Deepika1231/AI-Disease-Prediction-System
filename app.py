
import streamlit as st
import joblib
import numpy as np

# Load model and label encoder
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("🧠 AI Disease Prediction System")
st.markdown("Enter your symptoms below to predict the possible disease.")

# Input widgets
fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
fatigue = st.checkbox("Fatigue")
headache = st.checkbox("Headache")
nausea = st.checkbox("Nausea")

if st.button("Predict"):
    input_data = np.array([[fever, cough, fatigue, headache, nausea]], dtype=int)
    prediction = model.predict(input_data)[0]
    disease = label_encoder.inverse_transform([prediction])[0]
    st.success(f"🩺 Predicted Disease: **{disease}**")
