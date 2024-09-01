import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load(r"C:\Users\syama\Desktop\cardekho project\EDA\random_forest_model.pkl")

# Set page configuration
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")

# Set custom background color
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Improved header presentation
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🚗 Car Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>This app predicts the price of a used car based on its features.</p>", unsafe_allow_html=True)

# Organize input fields into two columns
col1, col2 = st.columns(2)

with col1:
    car_age = st.number_input("Car Age (years)", min_value=0, max_value=30, value=5)
    mileage = st.number_input("Mileage (in km)", min_value=0.0, max_value=1000000.0, value=15000.0)
    engine = st.number_input("Engine Size (in cc)", min_value=500, max_value=10000, value=1500)
    st.markdown(" ")

with col2:
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

# Load feature names and ensure the input data has all necessary columns
feature_names = joblib.load(r"C:\Users\syama\Desktop\cardekho project\EDA\feature_names.pkl")
input_data = input_data.reindex(columns=feature_names, fill_value=0)

# Custom button styles
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Prediction
if st.button('Predict Price'):
    with st.spinner('Calculating...'):
        predicted_price = model.predict(input_data)
    st.success('Prediction Complete!')
    st.markdown(f"<h2 style='color: #4CAF50;'>Predicted Price: ₹ {predicted_price[0]:,.2f}</h2>", unsafe_allow_html=True)
