import streamlit as st

st.title("Welcome to estimating Snowflake consumption")

st.header("EStimate hourly compute and WH size")

col1, col2, col3 = st.columns(3)
with col1:
  st.subheader("Workload: Ingest")
  wh_ingest = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"))
  wh_ingest_hours = st.number_input("How many hours a day will the WH be running?")
  wh_ingest_days = st.number_input("How many days a week will the WH be running?")

with col2:
  st.subheader("Workload: Transformations")
  wh_transform = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"))
  wh_transform_hours = st.number_input("How many hours a day will the WH be running?")
  wh_transform_days = st.number_input("How many days a week will the WH be running?")

with col3:
  st.subheader("Workload: Internal BI")
  wh_internal_ingest = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"))
  wh_internal_hours = st.number_input("How many hours a day will the WH be running?")
  wh_internal_days = st.number_input("How many days a week will the WH be running?")
