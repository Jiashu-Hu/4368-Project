import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Load API key and base URL
api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1/")

if not api_key:
    st.error("Please set the OPENAI_API_KEY environment variable!")
    st.stop()

st.title("🛡️ Leftover Zero-Waste Recipe Generator (Week 2 Draft)")

# User input
ingredients = st.text_input(
    "Enter your leftover ingredients (comma-separated, e.g., rice, eggs, carrots)"
).split(",")
preference = st.selectbox(
    "Dietary Preference", ["None", "Vegetarian", "Low-Calorie", "Kid-Friendly"]
)

# Generate button
if st.button("Generate Recipe!"):
    with st.spinner("AI is thinking..."):
        client = OpenAI(api_key=api_key, base_url=api_base)
        prompt = f"""
        You are an eco-friendly chef focused on zero waste. Based on leftover ingredients: {", ".join([ing.strip() for ing in ingredients if ing.strip()])}
        and preference: {preference}, generate 1-2 simple recipes.
        Requirements:
        - Each recipe limited to 5 steps, suitable for low-income families (using common tools, no special equipment required).
        - Include nutritional tips (e.g., calories, protein).
        - Add zero-waste tips (e.g., how to use scraps).
        - Output should be culturally neutral and safe (add disclaimer: consult a doctor).
        Format: **Recipe Name** \n Ingredients \n Steps \n Nutrition \n Tip
        """
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Free model, sufficient
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300,  # Control length to avoid excessive output
            )
            recipe = response.choices[0].message.content
            st.success("Recipe generated successfully!")
            st.markdown(recipe)
        except Exception as e:
            st.error(f"AI error: {e}")

# Simple history (using session state to simulate database)
if "history" not in st.session_state:
    st.session_state.history = []
if st.button("View History"):
    if st.session_state.history:
        for i, entry in enumerate(st.session_state.history[-3:], 1):  # Last 3 entries
            st.write(f"Entry {i}: {entry['input']} → {entry['output'][:100]}...")
    else:
        st.info("No history yet.")

# Run: streamlit run app.py (browser opens at localhost:8501)
