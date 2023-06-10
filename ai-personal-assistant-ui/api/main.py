import streamlit as st
from datetime import date
import app

def main():
  st.title("Welcome to AI Personal Assistant!")

  # ask_question_button = st.button("Generate Schedule for Today: " + str(date.today()))
  app.generate_schedule()

if __name__ == '__main__':
  main()