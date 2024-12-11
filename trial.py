import streamlit as st
from transformers import pipeline
import os

# Set your Hugging Face API key
os.environ['HF_HOME'] = "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"

# Load pre-trained GPT-2 model for text generation (from Hugging Face API)
generator = pipeline('text-generation', model='gpt2')

# Streamlit app configuration
st.title("Story Generator")
st.markdown("Enter a prompt below, and I will generate text based on it.")

# User input for prompt
prompt = st.text_input("Enter your prompt:", "Once upon a time, in a land far away, there was a kingdom where")

if st.button("Generate Text"):
    # Generate text based on the prompt
    with st.spinner("Generating text..."):
        generated_text = generator(prompt, max_length=100, num_return_sequences=1, truncation=True)
        
    # Display the generated text
    st.subheader("Generated Text")
    st.write(generated_text[0]['generated_text'])



#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
