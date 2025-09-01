# Customer Churn Predictor - Streamlit App

A user-friendly web application built with Streamlit to predict customer churn probability in real-time. This interactive tool allows business users to input customer details and instantly receive churn risk assessments to support retention strategies.

##  Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://churn-insights.streamlit.app/)

Try the application directly without any setup required!

##  Features

- **Interactive Web Interface**: Easy-to-use Streamlit dashboard
- **Real-time Predictions**: Instant churn probability calculations
- **Comprehensive Input Forms**: Organized sections for customer data entry
- **Data Preview**: Review entered customer information before prediction


### Using the Application

#### 1. Personal Details Section
- **Gender**: Select Male or Female
- **Senior Citizen**: Choose Yes or No
- **Partner**: Indicate if customer has a partner
- **Dependents**: Indicate if customer has dependents
- **Tenure**: Set customer tenure in months (0-100)

#### 2. Services Subscribed Section
- **Phone Service**: Yes/No
- **Multiple Lines**: Yes/No/No phone service
- **Internet Service**: DSL/Fiber optic/No
- **Online Security**: Yes/No/No internet service
- **Online Backup**: Yes/No/No internet service
- **Device Protection**: Yes/No/No internet service
- **Tech Support**: Yes/No/No internet service
- **Streaming TV**: Yes/No/No internet service
- **Streaming Movies**: Yes/No/No internet service

#### 3. Billing & Payment Section
- **Contract Type**: Month-to-month/One year/Two year
- **Paperless Billing**: Yes/No
- **Payment Method**: Electronic check/Mailed check/Bank transfer/Credit card
- **Monthly Charges**: Set amount in dollars (0-150)
- **Total Charges**: Set total amount in dollars (0-10000)

#### 4. Get Prediction
1. Review the entered data in the preview section
2. Click the " Check Churn Status" button
3. View the risk assessment:
   - **High Risk**: Red warning with churn probability
   - **Low Risk**: Green success message with retention probability


## License

This project is licensed under the MIT License - see the LICENSE file for details.
