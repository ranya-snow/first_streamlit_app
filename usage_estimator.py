import streamlit as st

st.title("Welcome to estimating consumption :snowflake:")

st.header("Estimate hourly compute and WH size")

#cloud region variables

aws_regions = ["US West (Oregon) (us-west-2)", "US East (Ohio) (us-east-2)", "US East (N. Virginia) (us-east-1)", "Canada Central (Montreal) (ca-central-1)", "US Gov West 1 (us-gov-west-1)", "US East (Commercial Gov – N Virginia) (us-gov-east-1)", "EU (Ireland) (eu-west-1)", "Europe (London) (eu-west-2)", "EU (Paris) (eu-west-3)", "EU (Frankfurt) (eu-central-1)", "EU (Stockholm) (eu-north-1)", "Asia Pacific (Tokyo) (ap-northeast-1)", "Asia Pacific (Osaka) (ap-northeast-3)", "Asia Pacific (Seoul) (ap-northeast-2)", "AWS Pacific (Mumbai) (ap-south-1)", "Asia Pacific (Singapore) (ap-southeast-1)", "Asia Pacific (Sydney) (ap-southeast-2)", "Asia Pacific (Jakarta) (ap-southeast-3)", "South American (Sao Paulo) (sa-east-1)"]
azure_regions = ["West US 2 (Washington) (westus2)", "Central US (Iowa) (centralus)", "South Central US (Texas) (southcentralus)", "East US 2 (Virginia) (eastus2)", "Canada Central (Toronto) (canadacentral)", "US Gov (Virginia) (usgovvirginia)", "UK South (London) (uksouth)", "North Europe (Ireland) (northeurope)", "West Europe (Netherlands) (westeurope)", "Switzerland North (Zurich) (switzerlandnorth)", "UAE North (Dubai) (uaenorth)", "Central India (Pune) (centralindia)", "Japan East (Tokyo) (japaneast)", "Southeast Asia (Singapore) (southeastasia)", "Australia East (New South Wales) (australiaeast)"]
gcp_regions = ["US Central 1 (Iowa) (us-central1)", "US East 4 (N. Virginia) (us-east4)", "Europe West 2 (London) (europe-west2)", "Europe West 4 (Netherlands) (europe-west4)"]

#credit prices dictionary
credit_prices_aws = {
    "US West (Oregon) (us-west-2)": {
        "Standard": 2.00,
        "Enterprise": 3.00,
        "Business Critical": 4.00,
        "Storage": 23.00
    },
    "US East (Ohio) (us-east-2)": {
        "Standard": 2.00,
        "Enterprise": 3.00,
        "Business Critical": 4.00,
        "Storage": 23.00
    },
    "US East (N. Virginia) (us-east-1)": {
        "Standard": 2.00,
        "Enterprise": 3.00,
        "Business Critical": 4.00,
        "Storage": 23.00
    },
    "Canada Central (Montreal) (ca-central-1)": {
        "Standard": 2.25,
        "Enterprise": 3.50,
        "Business Critical": 4.50,
        "Storage": 23.00
    },
    "US Gov West 1 (us-gov-west-1)": {
        "Storage": 39.00
    },
    "US East (Commercial Gov – N Virginia) (us-gov-east-1)": {
        "Storage": 39.00
    },
    "EU (Ireland) (eu-west-1)": {
        "Standard": 2.60,
        "Enterprise": 3.90,
        "Business Critical": 5.20,
        "Storage": 23.00
    },
    "Europe (London) (eu-west-2)": {
        "Standard": 2.70,
        "Enterprise": 4.00,
        "Business Critical": 5.40,
        "Storage": 24.00
    },
    "EU (Paris) (eu-west-3)": {
        "Standard": 2.60,
        "Enterprise": 3.90,
        "Business Critical": 5.20,
        "Storage": 24.00
    },
    "EU (Frankfurt) (eu-central-1)": {
        "Standard": 2.60,
        "Enterprise": 3.90,
        "Business Critical": 5.20,
        "Storage": 24.50
    },
    "EU (Stockholm) (eu-north-1)": {
        "Standard": 2.60,
        "Enterprise": 3.90,
        "Business Critical": 5.20,
        "Storage": 23.00
    },
    "Asia Pacific (Tokyo) (ap-northeast-1)": {
        "Standard": 2.85,
        "Enterprise": 4.30,
        "Business Critical": 5.70,
        "Storage": 25.00
    },
    "Asia Pacific (Osaka) (ap-northeast-3)": {
        "Standard": 2.85,
        "Enterprise": 4.30,
        "Business Critical": 5.70,
        "Storage": 25.00
    },
    "Asia Pacific (Seoul) (ap-northeast-2)": {
        "Standard": 2.75,
        "Enterprise": 4.05,
        "Business Critical": 5.50,
        "Storage": 25.00
    },
    "AWS Pacific (Mumbai) (ap-south-1)": {
        "Standard": 2.20,
        "Enterprise": 3.30,
        "Business Critical": 4.40,
        "Storage": 25.00
    },
    "Asia Pacific (Singapore) (ap-southeast-1)": {
        "Standard": 2.50,
        "Enterprise": 3.70,
        "Business Critical": 5.00,
        "Storage": 25.00
    },
    "Asia Pacific (Sydney) (ap-southeast-2)": {
        "Standard": 2.75,
        "Enterprise": 4.05,
        "Business Critical": 5.50,
        "Storage": 25.00
    },
    "Asia Pacific (Jakarta) (ap-southeast-3)": {
        "Standard": 2.50,
        "Enterprise": 3.70,
        "Business Critical": 5.00,
        "Storage": 25.00
    },
    "South American (Sao Paulo) (sa-east-1)": {
        "Standard": 3.10,
        "Enterprise": 4.65,
        "Business Critical": 6.20,
        "Storage": 40.50
    }
}

credit_prices_azure = {
    "West US 2 (Washington) (westus2)": {
        "Standard": 2.00,
        "Enterprise": 3.00,
        "Business Critical": 4.00,
        "Storage": 23.00
    },
    "Central US (Iowa) (centralus)": {
        "Standard": 2.00,
        "Enterprise": 3.00,
        "Business Critical": 4.00,
        "Storage": 23.00
    },
    "South Central US (Texas) (southcentralus)": {
        "Standard": 2.00,
        "Enterprise": 3.00,
        "Business Critical": 4.00,
        "Storage": 23.00
    },
    "East US 2 (Virginia) (eastus2)": {
        "Standard": 2.00,
        "Enterprise": 3.00,
        "Business Critical": 4.00,
        "Storage": 23.00
    },
    "Canada Central (Toronto) (canadacentral)": {
        "Standard": 2.25,
        "Enterprise": 3.50,
        "Business Critical": 4.50,
        "Storage": 25.00
    },
    "US Gov (Virginia) (usgovvirginia)": {
        "Storage": 39.00
    },
    "UK South (London) (uksouth)": {
        "Standard": 2.70,
        "Enterprise": 4.00,
        "Business Critical": 5.40,
        "Storage": 24.00
    },
    "North Europe (Ireland) (northeurope)": {
        "Standard": 2.60,
        "Enterprise": 3.90,
        "Business Critical": 5.20,
        "Storage": 23.00
    },
    "West Europe (Netherlands) (westeurope)": {
        "Standard": 2.60,
        "Enterprise": 3.90,
        "Business Critical": 5.20,
        "Storage": 23.00
    },
    "Switzerland North (Zurich) (switzerlandnorth)": {
        "Standard": 3.10,
        "Enterprise": 4.65,
        "Business Critical": 6.20,
        "Storage": 28.80
    },
    "UAE North (Dubai) (uaenorth)": {
        "Standard": 2.70,
        "Enterprise": 4.40,
        "Business Critical": 5.40,
        "Storage": 25.40
    },
    "Central India (Pune) (centralindia)": {
        "Standard": 2.20,
        "Enterprise": 3.30,
        "Business Critical": 4.40,
        "Storage": 25.00
    },
    "Japan East (Tokyo) (japaneast)": {
        "Standard": 2.85,
        "Enterprise": 4.30,
        "Business Critical": 5.70,
        "Storage": 25.00
    },
    "Southeast Asia (Singapore) (southeastasia)": {
        "Standard": 2.50,
        "Enterprise": 3.70,
        "Business Critical": 5.00,
        "Storage": 25.00
    },
    "Australia East (New South Wales) (australiaeast)": {
        "Standard": 2.75,
        "Enterprise": 4.05,
        "Business Critical": 5.50,
        "Storage": 25.00
    }
}

cloud = st.selectbox("What cloud provider is your customer on?", ("Amazon Web Services", "Google Cloud Platform", "Microsoft Azure"))

if cloud == "Amazon Web Services":
    region = st.selectbox("Select a region", list(credit_prices_aws.keys()))
    plan = st.selectbox("Select a plan", list(credit_prices_aws.get(region, {}).keys()))
    value = credit_prices_aws.get(region, {}).get(plan)
    if value is not None:
        st.success(f"The credit price for {region} - {plan} is ${value:.2f}")
    else:
        st.error("Invalid selection")

elif cloud == "Microsoft Azure":
    region = st.selectbox("Select a region", list(credit_prices_azure.keys()))
    plan = st.selectbox("Select a plan", list(credit_prices_azure.get(region, {}).keys()))
    value = credit_prices_azure.get(region, {}).get(plan)
    if value is not None:
        st.success(f"The credit price for {region} - {plan} is ${value:.2f}")
    else:
        st.error("Invalid selection")

st.stop()

# elif cloud == "Google Cloud Platform":
#   region = st.selectbox("What region would you like to deploy your Snowflake instance?", azure_regions)


region = st.selectbox("Select a region", list(credit_prices_aws.keys()))
plan = st.selectbox("Select a plan", list(credit_prices_aws.get(region, {}).keys()))
value = credit_prices_aws.get(region, {}).get(plan)
if value is not None:
    st.success(f"The credit price for {region} - {plan} is ${value:.2f}")
else:
    st.error("Invalid selection")



edition = st.selectbox("What Snowflake Edition does your customer need?", ("Standard", "Enterprise", "Business Critical", "Virtual Private Snowflake"))
cloud = st.selectbox("What cloud provider is your customer on?", ("Amazon Web Services", "Google Cloud Platform", "Microsoft Azure"))

if cloud == "Amazon Web Services":
  region = st.selectbox("What region would you like to deploy your Snowflake instance?", aws_regions)
elif cloud == "Google Cloud Platform":
  region = st.selectbox("What region would you like to deploy your Snowflake instance?", gcp_regions)
elif cloud == "Microsoft Azure":
  region = st.selectbox("What region would you like to deploy your Snowflake instance?", azure_regions)



st.write(credit_price)
st.divider()

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
