import streamlit as st

st.title("Welcome to estimating Snowflake consumption")

st.header("EStimate hourly compute and WH size")
workload_ingest = st.input("Ingest")
wh_ingest = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"))
