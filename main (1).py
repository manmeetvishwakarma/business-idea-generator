import streamlit as st
import requests

# Paste your Groq API key here
api_key = "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"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

st.set_page_config(page_title="Startup Idea Generator", layout="centered")
st.title("🚀 Business Idea Generator")
st.markdown("Give a niche or topic and get a startup idea for India.")

niche = st.text_input("Enter business niche (e.g. fashion, health, food)")

if st.button("Generate Idea"):
    if niche.strip() == "":
        st.warning("Please enter a niche first.")
    else:
        prompt = f"""You are a business idea expert. Give a unique startup idea in the field of '{niche}' that can work in India. 
        Explain the concept, target users, and how it can make money."""

        data = {
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        with st.spinner("Generating your startup idea..."):
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                idea = response.json()["choices"][0]["message"]["content"]
                st.success("✅ Startup Idea:")
                st.markdown(idea)
            else:
                st.error("❌ Error: " + response.text)
# The streamlit app will automatically run after saving