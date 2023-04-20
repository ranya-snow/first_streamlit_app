# streamlit_app.py
import streamlit as st
st.title("I'm doing this.")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st_name = st.text_input('What i your name?', 'Ranya')
st.write(f"Hell {st_name}"!)
