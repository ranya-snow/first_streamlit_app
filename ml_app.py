#ml_app
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

#Page configuration
st.set_page_config(
  page_title = 'Simple Prediction App',
  layout = 'wide',
  initial_sidebar_state = 'expanded')

#Title of the app
st.title('Simple Prediction App')

#Load dataset
data = pd.read_csv('http://raw.github.com/dataprofessor/data/master/iris.csv')
df = pd.DataFrame(data)
st.write(df)
