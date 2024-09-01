import streamlit as st
import pandas as pd
import joblib

# Load the model and feature names
model = joblib.load(r"C:\Users\syama\Desktop\cardekho project\EDA\random_forest_model.pkl")
feature_names = joblib.load(r"C:\Users\syama\Desktop\cardekho project\EDA\feature_names.pkl")

# Streamlit user input
st.title("Car Price Prediction App")

car_age = st.number_input("Car Age (years)", min_value=0, max_value=30, value=5)
mileage = st.number_input("Mileage (in km)", min_value=0.0, max_value=1000000.0, value=15000.0)
engine = st.number_input("Engine Size (in cc)", min_value=500, max_value=10000, value=1500)
max_power = st.number_input("Max Power (in bhp)", min_value=20.0, max_value=1000.0, value=100.0)
seats = st.number_input("Number of Seats", min_value=2, max_value=10, value=5)

fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Electric', 'LPG'])
transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])
body_type = st.selectbox("Body Type", ['Hatchback', 'Sedan', 'SUV', 'Coupe', 'Minivan', 'Pickup Truck'])

# Prepare the input data
input_data = pd.DataFrame({
    'Car_Age': [car_age],
    'Mileage': [mileage],
    'Engine': [engine],
    'Max Power': [max_power],
    'Seats': [seats],
    'Fuel Type_Diesel': [1 if fuel_type == 'Diesel' else 0],
    'Fuel Type_Electric': [1 if fuel_type == 'Electric' else 0],
    'Fuel Type_LPG': [1 if fuel_type == 'LPG' else 0],
    'Fuel Type_Petrol': [1 if fuel_type == 'Petrol' else 0],
    'Transmission_Manual': [1 if transmission == 'Manual' else 0],
    'Body type_Coupe': [1 if body_type == 'Coupe' else 0],
    'Body type_Hatchback': [1 if body_type == 'Hatchback' else 0],
    'Body type_SUV': [1 if body_type == 'SUV' else 0],
    'Body type_Sedan': [1 if body_type == 'Sedan' else 0],
    'Body type_Minivans': [1 if body_type == 'Minivan' else 0],
    'Body type_Pickup Truck': [1 if body_type == 'Pickup Truck' else 0]
})

# Ensure the input data has all the required columns
input_data = input_data.reindex(columns=feature_names, fill_value=0)

# Make predictions
if st.button('Predict Price'):
    predicted_price = model.predict(input_data)
    st.write(f"The predicted price of the car is: ₹ {predicted_price[0]:,.2f}")


