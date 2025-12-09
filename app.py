import streamlit as st
from openai import OpenAI

st.title("ChatGPT API Demo (Very Basic)")

api_key = st.text_input("Enter your OpenAI API Key:", type="password")
prompt = st.text_area("Ask something:")

if st.button("Generate"):
    if not api_key:
        st.error("Please enter your API key!")
    else:
        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        text = response.output_text
        st.success(text)
