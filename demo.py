import streamlit as st
from transformers import pipeline
import os

# Set your Hugging Face API key
os.environ['HF_HOME'] = "ahf_VsWAxfuJvletELYiFqBjOGkgUeHLpdKElA"

# Load pre-trained GPT-2 model for text generation (from Hugging Face API)
generator = pipeline('text-generation', model='gpt2')

# Streamlit app configuration
st.title("Letter Content Generator")
st.markdown("Enter a subject below, and I will generate a letter based on it.")

# User input for subject
subject = st.text_input("Enter the subject of the letter:", "Request for leave")

if st.button("Generate Letter"):
    # Generate letter content based on the subject
    prompt = f"Subject: {subject}\n\nDear [Recipient],\n"
    prompt += "I hope this message finds you well. I am writing to discuss the matter of "

    with st.spinner("Generating letter..."):
        generated_text = generator(
            prompt, 
            max_length=250, 
            num_return_sequences=1, 
            truncation=True,
            temperature=0.7,
            top_k=50
        )

    # Display the generated letter
    st.subheader("Generated Letter")
    st.write(generated_text[0]['generated_text'])
