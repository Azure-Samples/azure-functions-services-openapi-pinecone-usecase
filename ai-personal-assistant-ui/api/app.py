import streamlit as st
import requests as req

def generate_schedule():
  text_input = st.text_input(
    "Ask me any question 👇",
    label_visibility="visible",
    disabled=False,
    placeholder="\"What is an urgent email for Evan?\"",
  )

  if text_input:
    url = "https://ai-personal-assistant-azfs.azurewebsites.net/api/askquestion"
    payload = {
      "question": text_input,
    }

    response = req.post(url, json=payload)

    if response.status_code == 200:
      # st.write(response.text)
      st.markdown(f"<p style='font-size:32px'>{response.text}</p>", unsafe_allow_html=True)
    else:
      st.write("Request failed with status code:", response.status_code)
