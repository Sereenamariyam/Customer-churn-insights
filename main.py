import streamlit as st
import pandas as pd
from os import path
import joblib

# -----------------------------
# App Title
# -----------------------------
st.title("Customer Churn Predictor")


st.set_page_config(page_title="Customer Churn Predictor", page_icon="📉")
# -----------------------------
# App Logo
# -----------------------------
st.sidebar.image("images/Network.png", width=300)
st.sidebar.write("Predict churn. Reduce losses. Enhance customer loyalty.")


# -----------------------------
# Load the Trained Model
# -----------------------------
model_path = path.join("Model", "customer_churn_pipeline.pkl")

try:
    churn_predictor = joblib.load(model_path)
except FileNotFoundError:
    st.error(f"❌ Model not found in `{model_path}`. Please check the file path.")
    st.stop()

# -----------------------------
# Input Sections
# -----------------------------
st.subheader("Fill in the customer details")

# --- Personal Details ---
with st.expander("👤 Personal Details"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.radio("Senior Citizen", ["Yes", "No"])
    Partner = st.radio("Has a Partner", ["Yes", "No"])
    Dependents = st.radio("Has Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (Months)", 0, 100, step=1)

# --- Services Used ---
with st.expander("🌐 Services Subscribed"):
    PhoneService = st.radio("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

# --- Billing Information ---
with st.expander("💰 Billing & Payment"):
    Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.radio("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    MonthlyCharges = st.slider("Monthly Charges ($)", 0, 150, step=1, value=50)
    TotalCharges = st.slider("Total Charges ($)", 0, 10000, step=50, value=1000)

# -----------------------------
# Prepare Data for Prediction
# -----------------------------
SeniorCitizen_val = 1 if SeniorCitizen == "Yes" else 0

user_input = pd.DataFrame([{
    "gender": gender,
    "SeniorCitizen": SeniorCitizen_val,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}])

st.write("### Preview of Entered Data")
st.dataframe(user_input)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Check Churn Status"):
    try:
        prediction = churn_predictor.predict(user_input)[0]
        probability = churn_predictor.predict_proba(user_input)[0][1]

        if prediction == 1:
            st.error(f"⚠️ High risk: Customer likely to **churn**.\n\nProbability: **{probability:.2%}**")
        else:
            st.success(f"✅ Low risk: Customer likely to **stay**.\n\nChurn Probability: **{probability:.2%}**")
    except Exception as e:
        st.error(f"Prediction error: {e}")

