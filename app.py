import streamlit as st
import numpy as np
import pickle

# Page config
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="wide")

# Load model
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏠 House Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Predict house prices using Machine Learning</h4>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("📝 Enter House Details")

longitude = st.sidebar.slider("Longitude", -125.0, -113.0, -120.0)
latitude = st.sidebar.slider("Latitude", 32.0, 42.0, 37.0)
housing_median_age = st.sidebar.slider("House Age", 1, 50, 10)
total_rooms = st.sidebar.slider("Total Rooms", 1, 10000, 1000)
total_bedrooms = st.sidebar.slider("Total Bedrooms", 1, 5000, 300)
population = st.sidebar.slider("Population", 1, 50000, 2000)
households = st.sidebar.slider("Households", 1, 5000, 500)
median_income = st.sidebar.slider("Median Income", 1.0, 15.0, 5.0)

ocean = st.sidebar.selectbox("Ocean Proximity", 
                            ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"])

# Input processing
input_data = [longitude, latitude, housing_median_age,
              total_rooms, total_bedrooms, population,
              households, median_income]

ocean_cols = ['ocean_proximity_<1H OCEAN',
              'ocean_proximity_INLAND',
              'ocean_proximity_ISLAND',
              'ocean_proximity_NEAR BAY',
              'ocean_proximity_NEAR OCEAN']

for col in ocean_cols:
    if col == f"ocean_proximity_{ocean}":
        input_data.append(1)
    else:
        input_data.append(0)

# Prediction button
st.markdown("---")
if st.button("🚀 Predict Price"):
    prediction = model.predict([input_data])

    st.markdown(
        f"""
        <div style='background-color:#e8f5e9;padding:30px;border-radius:10px;text-align:center;'>
            <h2 style='color:#2e7d32;'>💰 Estimated House Price</h2>
            <h1 style='color:#1b5e20;'>${prediction[0]:,.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ by chandana</center>", unsafe_allow_html=True)