# 📁 File: ml_pricing_app.py (Updated for Professional UI)

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load trained model
model = joblib.load("linreg_model.pkl")

# Load full product list (same list used in dataset)
product_list = [
    "Smartphone", "Wireless Earbuds", "Bluetooth Speaker", "Gaming Laptop", "Smartwatch",
    "Noise Cancelling Headphones", "Mechanical Keyboard", "4K Monitor", "Portable SSD", "Fitness Tracker",
    "Running Shoes", "Leather Wallet", "Backpack", "Water Bottle", "Sunglasses",
    "Winter Jacket", "Sneakers", "Yoga Mat", "Hiking Boots", "Electric Toothbrush",
    "Air Purifier", "Espresso Machine", "Robot Vacuum", "LED Desk Lamp", "Instant Pot",
    "Hair Dryer", "Standing Desk", "Ergonomic Chair", "Monitor Arm", "Wireless Charger",
    "iPad", "Laptop Stand", "Graphic Tablet", "Tripod", "Camera Drone",
    "Smart Thermostat", "Video Doorbell", "Bluetooth Tracker", "Streaming Stick", "Projector",
    "Camping Tent", "Sleeping Bag", "Power Bank", "Phone Gimbal", "Smart Scale",
    "Microwave", "Dish Rack", "Dehumidifier", "Pet Feeder", "Electric Kettle"
]

# --- Streamlit Config ---
st.set_page_config(page_title="PriceWise AI", page_icon="💡", layout="wide")
st.markdown("""
<style>
    .block-container {
        padding: 2rem 2rem 2rem 2rem;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
    }
    .stSelectbox>div>div {
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("💡 PriceWise – AI-Powered Pricing Advisor")
st.caption("Turn business conditions into smarter pricing decisions")
st.markdown("---")

# --- Layout: Sidebar for Inputs ---
st.sidebar.header("🛠️ Market Conditions")
product = st.sidebar.selectbox("Product", product_list)
competitor_price = st.sidebar.slider("Competitor Price ($)", 10, 500, 250)
inventory = st.sidebar.slider("Current Inventory", 10, 200, 100)
user_type = st.sidebar.selectbox("Customer Type", ["Price-sensitive", "Brand-loyal", "Impulse Buyer", "Average"])
weather = st.sidebar.selectbox("Weather", ["Sunny", "Rainy", "Cloudy", "Snowy"])
day_of_week = st.sidebar.selectbox("Day of the Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

# --- Main Call to Action ---
st.subheader("📈 Price Optimization Simulator")

# --- Optimization Logic ---
def optimize_price(product, competitor_price, inventory, user_type, weather, day_of_week, model, price_range=(10, 500), step=5):
    results = []
    for price in np.arange(price_range[0], price_range[1] + step, step):
        row = pd.DataFrame([{
            "base_price": price,
            "competitor_price": competitor_price,
            "inventory": inventory,
            "user_type": user_type,
            "weather": weather,
            "day_of_week": day_of_week
        }])
        demand = max(0, model.predict(row)[0])
        revenue = price * demand
        results.append((price, demand, revenue))
    df = pd.DataFrame(results, columns=["Price", "Predicted Demand", "Revenue"])
    best = df.loc[df["Revenue"].idxmax()]
    return best, df

# --- Button & Output ---
if st.button("Run Price Simulation 💥"):
    best_price, results_df = optimize_price(product, competitor_price, inventory, user_type, weather, day_of_week, model)

    # KPI Summary
    col1, col2, col3 = st.columns(3)
    col1.metric("Optimal Price", f"${best_price['Price']:.2f}")
    col2.metric("Expected Demand", f"{int(best_price['Predicted Demand'])} units")
    col3.metric("Estimated Revenue", f"${best_price['Revenue']:.2f}")

    # Dual Axis Plot with improved layout
    fig, ax1 = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=results_df, x="Price", y="Revenue", ax=ax1, color="green", label="Revenue")
    ax1.set_ylabel("Revenue ($)", color="green")
    ax1.tick_params(axis='y', labelcolor='green')

    ax2 = ax1.twinx()
    sns.lineplot(data=results_df, x="Price", y="Predicted Demand", ax=ax2, color="blue", linestyle="--", label="Demand")
    ax2.set_ylabel("Demand (units)", color="blue")
    ax2.tick_params(axis='y', labelcolor='blue')

    ax1.axvline(best_price['Price'], color='red', linestyle=':', label='Optimal Price')
    ax1.set_xlabel("Simulated Base Price ($)")
    ax1.set_title("\nRevenue & Demand vs. Price")

    fig.tight_layout(pad=2.0)  # Fix axis label overlap
    st.pyplot(fig)

else:
    st.info("👈 Use the sidebar to enter your product's current market context, then click 'Run Price Simulation 💥'")
