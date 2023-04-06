import streamlit as st
import pandas
import requests
import snowflake.connector


st.title('Welcome to your Clash Royale Stats')

st.header('👍 Your Clash Wins 👍')

st.header('👎 Your Clash Losses 👎')

st.header('🏆 Total Trophies Since April 1st, 2023 🏆')

def get_battlelog():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM BATTLELOG_FLAT")
    return my_cur.fetchall()


