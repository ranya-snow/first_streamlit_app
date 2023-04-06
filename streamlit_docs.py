# streamlit_app.py

import streamlit
import snowflake.connector

# Initialize connection.
# Uses st.cache_resource to only run once.
# @st.cache_resource
# def init_connection():
#     return snowflake.connector.connect(
#         **st.secrets["snowflake"], client_session_keep_alive=True
#     )

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

