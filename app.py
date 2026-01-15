import streamlit as st
import json
import os
from difflib import get_close_matches

# Load travel database from JSON
with open("travel_data.json", "r", encoding="utf-8") as f:
    travel_info = json.load(f)

# Custom CSS for header and info box
st.markdown(
    """
    <style>
    .header {
        background: linear-gradient(90deg, #008080, #20B2AA);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
    }
    .header h1 {
        color: white;
        font-size: 48px;
        margin: 0;
    }
    .header p {
        color: #f0f8ff;
        font-size: 18px;
        margin: 5px 0 0 0;
    }
    .info-box {
        background: #f0f8ff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    .info-title {
        font-weight: bold;
        text-decoration: underline;
        font-size: 18px;
        color: #000;
    }
    .best-time {
        color: #e74c3c;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown(
    """
    <div class="header">
        <h1>✈️ AI Travel Buddy 🌍</h1>
        <p>Your smart travel assistant. Ask about any city and discover its highlights!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# User input
user_input = st.text_input("Ask me about your trip:")

if user_input:
    city = user_input.strip().lower()
    st.write("🤖 Travel Buddy says:")

    if city in travel_info:
        col1, col2 = st.columns([1, 1.2])  # Info on left, image on right

        with col1:
            st.markdown(
                f"""
                <div class='info-box'>
                    <div class='info-title'>Info:</div>
                    {travel_info[city]['info']}
                    <br><br>
                    <div class='best-time'>Best time to visit: {travel_info[city].get('best_time','Anytime')}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            image_path = os.path.join("images", travel_info[city]["image"])
            st.image(image_path, width=400)  # Limit width for consistency

    else:
        suggestions = get_close_matches(city, travel_info.keys(), n=3, cutoff=0.6)
        if suggestions:
            st.write(f"Did you mean: {', '.join(suggestions)}?")
        else:
            st.write(f"Sorry, I don't have info for {user_input.strip()} yet. Try another city!")
