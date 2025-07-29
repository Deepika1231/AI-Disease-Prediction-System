
import streamlit as st
import pandas as pd
import pickle

st.title("AI-Based Disease Prediction System")
st.write("Select the symptoms below to predict the disease.")

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Input
fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
fatigue = st.checkbox("Fatigue")
headache = st.checkbox("Headache")

if st.button("Predict"):
    features = [[int(fever), int(cough), int(fatigue), int(headache)]]
    prediction = model.predict(features)
    st.success(f"Predicted Disease: {prediction[0]}")
