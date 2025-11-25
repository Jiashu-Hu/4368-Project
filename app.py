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

# Test Mode Sidebar
st.sidebar.title("🧪 Testing Tools")
test_mode = st.sidebar.checkbox("Enable Test Mode")

if test_mode:
    test_ingredients = st.sidebar.text_input(
        "Test Input (comma-separated)", "rice,eggs"
    )
    test_preference = st.sidebar.selectbox("Test Preference", ["None", "Vegetarian"])

    if st.sidebar.button("Quick Test Generate"):
        with st.sidebar:
            with st.spinner("Testing AI generation..."):
                client = OpenAI(api_key=api_key, base_url=api_base)
                ingredients_list = [
                    ing.strip() for ing in test_ingredients.split(",") if ing.strip()
                ]
                prompt = f"""
                You are an eco-friendly chef focused on zero waste. Based on leftover ingredients: {", ".join(ingredients_list)}
                and preference: {test_preference}, generate 1-2 simple recipes.
                Requirements:
                - Each recipe limited to 5 steps, suitable for low-income families (using common tools, no special equipment required).
                - Include nutritional tips (e.g., calories, protein).
                - Add zero-waste tips (e.g., how to use scraps).
                - Output should be culturally neutral and safe (add disclaimer: consult a doctor).
                - **only use the provided ingredients; do not add new ones.**
                Format: **Recipe Name** \n Ingredients \n Steps \n Nutrition \n Tip
                """
                try:
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=300,
                    )
                    recipe = response.choices[0].message.content
                    st.success("Test recipe generated!")
                    st.write("**Test Output:**")
                    st.markdown(recipe)

                    # Manual rating
                    score = st.slider("Manual Rating (1-5)", 1, 5, 3)
                    st.write(f"📝 Test Record: {test_ingredients} | Score: {score}")

                except Exception as e:
                    st.error(f"Test AI error: {e}")

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
        - **only use the provided ingredients; do not add new ones.**
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
