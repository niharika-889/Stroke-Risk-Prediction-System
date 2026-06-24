import streamlit as st
import pandas as pd
import joblib

# ==========================
# LOAD MODEL
# ==========================

model = joblib.load("stroke_prediction_model.pkl")

# ==========================
# TITLE
# ==========================

st.set_page_config(
    page_title="Stroke Risk Predictor",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Stroke Risk Prediction System")
st.write(
    "Enter patient information below to predict stroke risk."
)

# ==========================
# USER INPUTS
# ==========================

gender = st.selectbox(
    "Gender",
    ["Female", "Male", "Other"]
)

age = st.number_input(
    "Age",
    min_value=0,
    max_value=120,
    value=30
)

hypertension = st.selectbox(
    "Hypertension",
    [0, 1]
)

heart_disease = st.selectbox(
    "Heart Disease",
    [0, 1]
)

ever_married = st.selectbox(
    "Ever Married",
    ["No", "Yes"]
)

work_type = st.selectbox(
    "Work Type",
    [
        "Govt_job",
        "Never_worked",
        "Private",
        "Self-employed",
        "children"
    ]
)

Residence_type = st.selectbox(
    "Residence Type",
    ["Rural", "Urban"]
)

avg_glucose_level = st.number_input(
    "Average Glucose Level",
    value=100.0
)

bmi = st.number_input(
    "BMI",
    value=25.0
)

smoking_status = st.selectbox(
    "Smoking Status",
    [
        "Unknown",
        "formerly smoked",
        "never smoked",
        "smokes"
    ]
)

# ==========================
# ENCODING
# ==========================

gender_map = {
    "Female": 0,
    "Male": 1,
    "Other": 2
}

ever_married_map = {
    "No": 0,
    "Yes": 1
}

work_type_map = {
    "Govt_job": 0,
    "Never_worked": 1,
    "Private": 2,
    "Self-employed": 3,
    "children": 4
}

residence_map = {
    "Rural": 0,
    "Urban": 1
}

smoking_map = {
    "Unknown": 0,
    "formerly smoked": 1,
    "never smoked": 2,
    "smokes": 3
}

# ==========================
# PREDICTION
# ==========================

if st.button("Predict Stroke Risk"):

    input_data = pd.DataFrame([[
        gender_map[gender],
        age,
        hypertension,
        heart_disease,
        ever_married_map[ever_married],
        work_type_map[work_type],
        residence_map[Residence_type],
        avg_glucose_level,
        bmi,
        smoking_map[smoking_status]
    ]],
    columns=[
        "gender",
        "age",
        "hypertension",
        "heart_disease",
        "ever_married",
        "work_type",
        "Residence_type",
        "avg_glucose_level",
        "bmi",
        "smoking_status"
    ])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if probability < 0.30:
       st.success(
          f"🟢 Low Stroke Risk\n\nProbability: {probability:.2%}"
    )

    elif probability < 0.60:
        st.warning(
           f"🟡 Moderate Stroke Risk\n\nProbability: {probability:.2%}"
    )

    else:
        st.error(
           f"🔴 High Stroke Risk\n\nProbability: {probability:.2%}"
    )