import streamlit as st

st.title("Welcome to estimating Snowflake consumption :snowflake:")

st.header("EStimate hourly compute and WH size")

col1, col2, col3 = st.columns(3)
with col1:
  st.subheader("Workload: Ingest")
  wh_ingest = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="ingest")
  wh_ingest_hours = st.number_input("How many hours a day will the WH be running?", key="ingest_h")
  wh_ingest_days = st.number_input("How many days a week will the WH be running?",  key="ingest_d")

with col2:
  st.subheader("Workload: Transformations")
  wh_transform = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="transform")
  wh_transform_hours = st.number_input("How many hours a day will the WH be running?", key="transform_h", step=1)
  wh_transform_days = st.number_input("How many days a week will the WH be running?", key="transform_d")

with col3:
  st.subheader("Workload: Internal BI")
  wh_internal = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="internal")
  wh_internal_hours = st.number_input("How many hours a day will the WH be running?", key="internal_h")
  wh_internal_days = st.number_input("How many days a week will the WH be running?", key="internal_d")

col4, col5, col6 = st.columns(3)
with col4:
  st.subheader("Workload: Ingest")
  wh_ingest = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="ingest")
  wh_ingest_hours = st.number_input("How many hours a day will the WH be running?", key="ingest_h")
  wh_ingest_days = st.number_input("How many days a week will the WH be running?",  key="ingest_d")

with col5:
  st.subheader("Workload: Transformations")
  wh_transform = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="transform")
  wh_transform_hours = st.number_input("How many hours a day will the WH be running?", key="transform_h")
  wh_transform_days = st.number_input("How many days a week will the WH be running?", key="transform_d")

with col6:
  st.subheader("Workload: Internal BI")
  wh_internal = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="internal")
  wh_internal_hours = st.number_input("How many hours a day will the WH be running?", key="internal_h")
  wh_internal_days = st.number_input("How many days a week will the WH be running?", key="internal_d")
