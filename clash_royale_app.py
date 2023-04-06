import streamlit as st
import pandas
import requests
import snowflake.connector


st.title('Welcome to your Clash Royale Stats')

st.header('👍 Your Clash Wins 👍')

st.header('👎 Your Clash Losses 👎')

st.header('🏆 Total Trophies Since April 1st, 2023 🏆')

@st.cache_resource
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

st.stop()

def get_battlelog():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM BATTLELOG_FLAT")
    return my_cur.fetchall()
  
if st.button('Get Battlelog List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_battlelog()
  my_cnx.close()
  st.dataframe(my_data_rows)


