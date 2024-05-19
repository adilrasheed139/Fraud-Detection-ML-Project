import streamlit as st
import pickle
import numpy as np

# Load your trained model
model_path = 'rfc_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_fraud(data):
    prediction = model.predict([data])
    return prediction[0]

# Streamlit app
st.title("Online Bank Payment Fraud Detection")

st.write("""
## Enter transaction details to detect if it is fraudulent or not
""")

# Input fields
step = st.number_input('Step', min_value=0, value=0)
type = st.selectbox('Transaction Type', ['CASH-IN', 'CASH-OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'])
amount = st.number_input('Amount', min_value=0.0, value=0.0)
oldbalanceOrg = st.number_input('Original Balance', min_value=0.0, value=0.0)

# Map transaction type to numerical values
type_mapping = {'CASH-IN': 0, 'CASH-OUT': 1, 'DEBIT': 2, 'PAYMENT': 3, 'TRANSFER': 4}
type = type_mapping[type]

# Prepare input for the model
input_data = [step, type, amount, oldbalanceOrg]

# Predict button
if st.button('Predict'):
    result = predict_fraud(input_data)
    if result == 1:
        st.error("This transaction is predicted to be fraudulent.")
    else:
        st.success("This transaction is predicted to be legitimate.")
