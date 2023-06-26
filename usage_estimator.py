import streamlit as st

st.title("Welcome to estimating Snowflake consumption :snowflake:")

st.header("EStimate hourly compute and WH size")

col1, col2, col3 = st.columns(3)
with col1:
  st.subheader("Workload: Ingest")
  wh_ingest = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="ingest")
  wh_ingest_hours = st.number_input("How many hours a day will the WH be running?", key="ingest_h", step=0.25)
  wh_ingest_days = st.number_input("How many days a week will the WH be running?",  key="ingest_d", step=1)

with col2:
  st.subheader("Workload: Transformations")
  wh_transform = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="transform")
  wh_transform_hours = st.number_input("How many hours a day will the WH be running?", key="transform_h", step=0.25)
  wh_transform_days = st.number_input("How many days a week will the WH be running?", key="transform_d", step=1)

with col3:
  st.subheader("Workload: Internal BI")
  wh_internal = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="internal")
  wh_internal_hours = st.number_input("How many hours a day will the WH be running?", key="internal_h", step=0.25)
  wh_internal_days = st.number_input("How many days a week will the WH be running?", key="internal_d", step=1)

st.divider()
col4, col5, col6 = st.columns(3)
with col4:
  st.subheader("Workload: Ad-hoc Analysis")
  wh_adhoc = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="adhoc")
  wh_adhoc_hours = st.number_input("How many hours a day will the WH be running?", key="adhoc_h", step=0.25)
  wh_adhoc_days = st.number_input("How many days a week will the WH be running?",  key="adhoc_d", step=1)

with col5:
  st.subheader("Workload: Development work")
  wh_dev = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="dev")
  wh_dev_hours = st.number_input("How many hours a day will the WH be running?", key="dev_h", step=0.25)
  wh_dev_days = st.number_input("How many days a week will the WH be running?", key="dev_d", step=1)

with col6:
  st.subheader("Workload: Extermal BI")
  wh_external = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL"), key="external")
  wh_external_hours = st.number_input("How many hours a day will the WH be running?", key="external_h", step=0.25)
  wh_external_days = st.number_input("How many days a week will the WH be running?", key="external_d", step=1)
