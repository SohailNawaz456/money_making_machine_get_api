import streamlit as st
import random
import time
import requests

# Set Streamlit page configuration
st.set_page_config(page_title="Money Making Machine", page_icon="💰", layout="centered")

# Custom CSS for better UI
st.markdown(
    """
    <style>
    .stTitle {
        color: #007bff;
        text-align: center;
    }
    .stButton>button {
        background-color: #28a745;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #218838;
    }
    .stSuccess {
        font-size: 20px;
        font-weight: bold;
        color: #d63384;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title of the Streamlit app
st.title("💰 Money Making Machine 💰")

# Function to generate a random amount of money
def generate_money():
    return random.randint(1, 1000)  # Generates a random integer between 1 and 1000

st.subheader("🤑 Instant Cash Generator")

# Button to generate money
if st.button("Generate Money 💸"):
    with st.spinner("Counting your money... 💵"):
        time.sleep(3)  # Simulate processing time
    amount = generate_money()  # Generate a random amount
    st.success(f"You made **${amount}**! 🎉")

# Function to fetch side hustle ideas
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles?api_key=1234567890")
        if response.status_code == 200:
            hustles = response.json()
            return hustles.get("side_hustle", "Freelancing")
        else:
            return "Freelancing"
    except Exception as e:
        return "Something went wrong!"

st.subheader("🚀 Side Hustle Ideas")

# Button to generate hustle ideas
if st.button("Generate Hustle 💼"):
    with st.spinner("Fetching hustle ideas..."):
        time.sleep(2)  # Simulate API call delay
    idea = fetch_side_hustle()
    st.success(f"💡 **{idea}**")

# Function to fetch money quotes
def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes?api_key=1234567890")
        if response.status_code == 200:
            quotes = response.json()
            return quotes.get("money_quote", "Freelancing")
        else:
            return "Freelancing"
    except Exception as e:
        return "Something went wrong!"

st.subheader("💡 Money Quote Ideas")

# Button to generate money quotes
if st.button("Generate Money Quote 🏦"):
    with st.spinner("Fetching money wisdom..."):
        time.sleep(2)  # Simulate API call delay
    idea = fetch_money_quote()
    st.success(f"💰 **{idea}**")
