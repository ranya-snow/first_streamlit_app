import streamlit as st

st.title("Welcome to estimating your Snowflake consumption :snowflake:")

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

credit_prices_gcp = {
    "US Central 1 (Iowa) (us-central1)": {
        "Standard": 2.0,
        "Enterprise": 3.0,
        "Business Critical": 4.0,
        "Storage": 20.0
    },
    "US East 4 (N. Virginia) (us-east4)": {
        "Standard": 2.0,
        "Enterprise": 3.0,
        "Business Critical": 4.0,
        "Storage": 23.0
    },
    "Europe West 2 (London) (europe-west2)": {
        "Standard": 2.7,
        "Enterprise": 4.0,
        "Business Critical": 5.4,
        "Storage": 23.0
    },
    "Europe West 4 (Netherlands) (europe-west4)": {
        "Standard": 2.6,
        "Enterprise": 3.9,
        "Business Critical": 5.2,
        "Storage": 20.0
    }
}

# AWS storage prices
storage_prices_aws = {region: details["Storage"] for region, details in credit_prices_aws.items() if "Storage" in details}

# Azure storage prices
storage_prices_azure = {region: details["Storage"] for region, details in credit_prices_azure.items() if "Storage" in details}

# GCP storage prices
storage_prices_gcp = {region: details["Storage"] for region, details in credit_prices_gcp.items() if "Storage" in details}

cloud = st.selectbox("What cloud provider is your customer on?", ("Amazon Web Services", "Google Cloud Platform", "Microsoft Azure"))

if cloud == "Amazon Web Services":
    region = st.selectbox("Select a region", list(credit_prices_aws.keys()))
    plans = list(credit_prices_aws.get(region, {}).keys())
    plans_without_storage = [plan for plan in plans if plan != "Storage"]
    plan = st.selectbox("Select a plan", plans_without_storage)

    storage_price = storage_prices_aws.get(region)
    value = credit_prices_aws.get(region, {}).get(plan)
    
    if value is not None:
        st.success(f"The credit price for {region} - {plan} is ${value:.2f}")
    else:
        st.error("Invalid selection")

elif cloud == "Microsoft Azure":
    region = st.selectbox("Select a region", list(credit_prices_azure.keys()))
    plans = list(credit_prices_aws.get(region, {}).keys())
    plans_without_storage = [plan for plan in plans if plan != "Storage"]
    plan = st.selectbox("Select a plan", plans_without_storage)

    storage_price = storage_prices_azure.get(region)
    value = credit_prices_azure.get(region, {}).get(plan)
    if value is not None:
        st.success(f"The credit price for {region} - {plan} is ${value:.2f}")
    else:
        st.error("Invalid selection")

elif cloud == "Google Cloud Platform":
    region = st.selectbox("Select a region", list(credit_prices_gcp.keys()))
    plans = list(credit_prices_aws.get(region, {}).keys())
    plans_without_storage = [plan for plan in plans if plan != "Storage"]
    plan = st.selectbox("Select a plan", plans_without_storage)

    storage_price = storage_prices_gcp.get(region)
    value = credit_prices_gcp.get(region, {}).get(plan)
    if value is not None:
        st.success(f"The credit price for {region} - {plan} is ${value:.2f}")
    else:
        st.error("Invalid selection")

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
  st.subheader("Workload: Data Ingest")
  wh_ingest = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL", "6XL"), key="ingest")
  wh_ingest_hours = st.number_input("How many hours a day will the WH be running?", key="ingest_h", step=0.25)
  wh_ingest_days = st.number_input("How many days a week will the WH be running?",  key="ingest_d", step=1)

with col2:
  st.subheader("Workload: Transformations")
  wh_transform = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL", "6XL"), key="transform")
  wh_transform_hours = st.number_input("How many hours a day will the WH be running?", key="transform_h", step=0.25)
  wh_transform_days = st.number_input("How many days a week will the WH be running?", key="transform_d", step=1)

with col3:
  st.subheader("Workload: Internal BI")
  wh_internal = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL", "6XL"), key="internal")
  wh_internal_hours = st.number_input("How many hours a day will the WH be running?", key="internal_h", step=0.25)
  wh_internal_days = st.number_input("How many days a week will the WH be running?", key="internal_d", step=1)

st.divider()
col4, col5, col6 = st.columns(3)
with col4:
  st.subheader("Workload: Ad-hoc Analysis")
  wh_adhoc = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL", "6XL"), key="adhoc")
  wh_adhoc_hours = st.number_input("How many hours a day will the WH be running?", key="adhoc_h", step=0.25)
  wh_adhoc_days = st.number_input("How many days a week will the WH be running?",  key="adhoc_d", step=1)

with col5:
  st.subheader("Workload: Development work")
  wh_dev = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL", "6XL"), key="dev")
  wh_dev_hours = st.number_input("How many hours a day will the WH be running?", key="dev_h", step=0.25)
  wh_dev_days = st.number_input("How many days a week will the WH be running?", key="dev_d", step=1)

with col6:
  st.subheader("Workload: External BI")
  wh_external = st.selectbox("Pick a warehouse size", ("XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL", "6XL"), key="external")
  wh_external_hours = st.number_input("How many hours a day will the WH be running?", key="external_h", step=0.25)
  wh_external_days = st.number_input("How many days a week will the WH be running?", key="external_d", step=1)

#wh credit cost
xs_price = 1
s_price = 2
m_price = 4
l_price = 8
xl_price = 16
_2xl_price = 32
_3xl_price = 64
_4xl_price = 128
_5xl_price = 256
_6xl_price = 512

#ingest credits
if wh_ingest == "XS":
    credit_ingest = xs_price
elif wh_ingest == "S":
    credit_ingest = s_price
elif wh_ingest == "M":
    credit_ingest = m_price
elif wh_ingest == "L":
    credit_ingest = l_price
elif wh_ingest == "XL":
    credit_ingest = xl_price 
elif wh_ingest == "2XL":
    credit_ingest = _2xl_price
elif wh_ingest == "3XL":
    credit_ingest = _3xl_price
elif wh_ingest == "4XL":
    credit_ingest = _4xl_price
elif wh_ingest == "5XL":
    credit_ingest = _5xl_price
elif wh_ingest == "6XL":
    credit_ingest = _6xl_price

#transform credits
if wh_transform == "XS":
    credit_transform = xs_price
elif wh_transform == "S":
    credit_transform = s_price
elif wh_transform == "M":
    credit_transform = m_price
elif wh_transform == "L":
    credit_transform = l_price
elif wh_transform == "XL":
    credit_transform = xl_price 
elif wh_transform == "2XL":
    credit_transform = _2xl_price
elif wh_transform == "3XL":
    credit_transform = _3xl_price
elif wh_transform == "4XL":
    credit_transform = _4xl_price
elif wh_transform == "5XL":
    credit_transform = _5xl_price
elif wh_transform == "6XL":
    credit_transform = _6xl_price

#internal credits
if wh_internal == "XS":
    credit_internal = xs_price
elif wh_internal == "S":
    credit_internal = s_price
elif wh_internal == "M":
    credit_internal = m_price
elif wh_internal == "L":
    credit_internal = l_price
elif wh_internal == "XL":
    credit_internal = xl_price 
elif wh_internal == "2XL":
    credit_internal = _2xl_price
elif wh_internal == "3XL":
    credit_internal = _3xl_price
elif wh_internal == "4XL":
    credit_internal = _4xl_price
elif wh_internal == "5XL":
    credit_internal = _5xl_price
elif wh_internal == "6XL":
    credit_internal = _6xl_price

#adhoc credits
if wh_adhoc == "XS":
    credit_adhoc = xs_price
elif wh_adhoc == "S":
    credit_adhoc = s_price
elif wh_adhoc == "M":
    credit_adhoc = m_price
elif wh_adhoc == "L":
    credit_adhoc = l_price
elif wh_adhoc == "XL":
    credit_adhoc = xl_price 
elif wh_adhoc == "2XL":
    credit_adhoc = _2xl_price
elif wh_adhoc == "3XL":
    credit_adhoc = _3xl_price
elif wh_adhoc == "4XL":
    credit_adhoc = _4xl_price
elif wh_adhoc == "5XL":
    credit_adhoc = _5xl_price
elif wh_adhoc == "6XL":
    credit_adhoc = _6xl_price

#dev credits
if wh_dev == "XS":
    credit_dev = xs_price
elif wh_dev == "S":
    credit_dev = s_price
elif wh_dev == "M":
    credit_dev = m_price
elif wh_dev == "L":
    credit_dev = l_price
elif wh_dev == "XL":
    credit_dev = xl_price 
elif wh_dev == "2XL":
    credit_dev = _2xl_price
elif wh_dev == "3XL":
    credit_dev = _3xl_price
elif wh_dev == "4XL":
    credit_dev = _4xl_price
elif wh_dev == "5XL":
    credit_dev = _5xl_price
elif wh_dev == "6XL":
    credit_dev = _6xl_price

#external credits
if wh_external == "XS":
    credit_external = xs_price
elif wh_external == "S":
    credit_external = s_price
elif wh_external == "M":
    credit_external = m_price
elif wh_external == "L":
    credit_external = l_price
elif wh_external == "XL":
    credit_external = xl_price 
elif wh_external == "2XL":
    credit_external = _2xl_price
elif wh_external == "3XL":
    credit_external = _3xl_price
elif wh_external == "4XL":
    credit_external = _4xl_price
elif wh_external == "5XL":
    credit_external = _5xl_price
elif wh_external == "6XL":
    credit_external = _6xl_price

total_credits = credit_ingest*wh_ingest_hours*wh_ingest_days*52 + credit_transform*wh_transform_hours*wh_transform_days*52 + credit_internal*wh_internal_hours*wh_internal_days*52 + credit_adhoc*wh_adhoc_hours*wh_adhoc_days*52 + credit_dev*wh_dev_hours*wh_dev_days*52 + credit_external*wh_external_hours*wh_external_days*52
total_cost_compute = total_credits * value

st.divider()

st.subheader("Storage")
storage_tb = st.number_input("How many TBs of data will you be storing each month?")
st.write(f"Your per TB storage cost is ${storage_price}")
storage_cost = storage_tb*storage_price*12

st.divider()

total_cost = storage_cost+total_cost_compute

colx, coly, colz = st.columns(3)
colx.metric(label="Your annual storage cost", value=f"${round(storage_cost,2)}")
coly.metric(label="Annual credits", value=total_credits help="This is the total number of credits you will be using, based on the above provided information :)")
colz.metric(label="Your total compute cost", value=f"${round(total_cost_compute,2)}")

st.header(f"Your total estimated cost will be ${total_cost:.2f}")

st.divider()
st.stop()
st.subheader("Snowpipe")
st.caption("Streaming")
#variables
month_tb = st.number_input("How many TBs are you streaming in a month?")
client_hours = st.number_input("How many hours in a day will your Kafka client be running?")
client_no = st.number_input("How many clients are you ingesting data from?")
client_cost_month = round((client_hours * client_no * 0.01 * 30),2)
st.write(f"Your monthly client cost for Snowpipe Streaming is {client_cost_month}.")

st.caption("File auto-ingest")
hours_ingest = st.number_input("How many hours of the day will you be ingesting files?", step=1)
days_ingest = st.number_input("How many days a week will you be ingesting files?", step=1)
files_ingest = st.number_input("How many files will you be loading in an hour?", step = 10)
snowpipe_cost = hours_ingest * days_ingest * 52 * (1/6000) * files_ingest
st.write(f"Your Snowpipe file ingest cost will be approximately {snowpipe_cost} per year")
