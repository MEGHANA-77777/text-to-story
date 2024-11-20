import streamlit as st
import requests

# Cohere API Configuration
API_KEY ="w8k3tijbongU51RwyJw35RkQs4KCIoLIBbzvyLbO"
API_URL = "https://api.cohere.ai/generate"

# Streamlit UI
st.title("Story Generation with Cohere")

prompt = st.text_area("Enter a prompt to generate a story:")

# Generate story on button click
if st.button("Generate Story"):
    if prompt:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "command",  # Select a model
            "prompt": prompt,
            "max_tokens": 500  # Control the length of the output
        }
        
        # Make a POST request to Cohere API
        response = requests.post(API_URL, json=data, headers=headers)
        
        if response.status_code == 200:
            story = response.json().get("text")
            st.write(story)  # Display the generated story
        else:
            st.error(f"Error generating story: {response.text}")
