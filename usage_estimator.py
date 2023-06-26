import streamlit as st

st.title("Welcome to estimating Snowflake consumption :snowflake:")

st.header("EStimate hourly compute and WH size")

edition = st.selectbox("What Snowflake Edition does your customer need?", ("Standard", "Enterprise", "Business Critical", "Virtual Private Snowflake"))
cloud = st.selectbox("What cloud provider is your customer on?", ("Amazon Web Services", "Google Cloud Platform", "Microsoft Azure"))

if cloud = "Amazon Web Services":
  region = st.selectbox("What region would youb like to deploy your Snowflake instance?", ("US West (Oregon) (us-west-2)", "US East (Ohio) (us-east-2)", "US East (N. Virginia) (us-east-1)", "Canada Central (Montreal) (ca-central-1)", "US Gov West 1 (us-gov-west-1)", "US East (Commercial Gov – N Virginia) (us-gov-east-1)", "EU (Ireland) (eu-west-1)", "Europe (London) (eu-west-2)", "EU (Paris) (eu-west-3)", "EU (Frankfurt) (eu-central-1)", "EU (Stockholm) (eu-north-1)", "Asia Pacific (Tokyo) (ap-northeast-1)", "Asia Pacific (Osaka) (ap-northeast-3)", "Asia Pacific (Seoul) (ap-northeast-2)", "AWS Pacific (Mumbai) (ap-south-1)", "Asia Pacific (Singapore) (ap-southeast-1)", "Asia Pacific (Sydney) (ap-southeast-2)", "Asia Pacific (Jakarta) (ap-southeast-3)", "South American (Sao Paulo) (sa-east-1)"))

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
