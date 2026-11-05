import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Disease Prediction System", page_icon="🩺", layout="centered")
st.title("🩺 Disease Prediction System")
st.write("Select symptoms to see an educational symptom-match result.")

# Small, transparent demo knowledge base. This is NOT a clinically validated dataset.
DISEASES = {
    "Common cold": {"runny nose", "sneezing", "sore throat", "cough", "mild fever"},
    "Flu (influenza)": {"fever", "cough", "body pain", "headache", "fatigue", "chills"},
    "Allergic rhinitis": {"sneezing", "runny nose", "itchy eyes", "itchy nose"},
    "Migraine": {"headache", "nausea", "sensitivity to light"},
    "Gastroenteritis": {"diarrhea", "vomiting", "stomach pain", "nausea", "fever"},
    "Acid reflux": {"heartburn", "sour taste", "stomach discomfort", "nausea"},
    "Sinusitis": {"headache", "facial pressure", "blocked nose", "runny nose"},
    "Tension headache": {"headache", "neck pain", "stress", "fatigue"},
}
ALL_SYMPTOMS = sorted(set().union(*DISEASES.values()))

st.warning(
    "Educational demo only: this tool cannot diagnose disease or assess your personal risk. "
    "Its results are simple matches against a small example symptom list, not medical predictions."
)
selected = st.multiselect("Choose the symptoms you are experiencing", ALL_SYMPTOMS)

if st.button("Check symptom matches", type="primary"):
    if not selected:
        st.error("Please select at least one symptom.")
    else:
        chosen = set(selected)
        scores = []
        for disease, symptoms in DISEASES.items():
            overlap = chosen & symptoms
            # Jaccard overlap keeps the matching calculation easy to understand.
            score = len(overlap) / len(chosen | symptoms)
            scores.append((disease, score, sorted(overlap)))
        scores.sort(key=lambda x: x[1], reverse=True)

        st.subheader("Possible symptom matches (not a diagnosis)")
        for disease, score, matched in scores[:3]:
            st.markdown(f"**{disease}** — {score*100:.0f}% symptom overlap")
            st.caption("Matching symptoms: " + (", ".join(matched) if matched else "None"))
        st.info(
            "Different conditions can share symptoms, and this demo covers only a few examples. "
            "Please consult a qualified healthcare professional for an accurate assessment."
        )

st.divider()
st.subheader("When to seek urgent help")
st.write(
    "Seek emergency medical care for severe difficulty breathing, chest pain, signs of stroke, "
    "unconsciousness, severe bleeding, or another rapidly worsening or life-threatening symptom."
)
st.caption("This project is for learning Python and Streamlit. It is not a substitute for professional medical advice.")
