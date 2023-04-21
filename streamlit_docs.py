# streamlit_app.py
import streamlit as st
import sklearn

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

st.title("I'm doing this.")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st_name = st.sidebar.text_input('What is your name?', 'Ranya')
st.write(f"Hello {st_name}!")

st.header("Iris Classification")

# Load dataset
data = load_iris()
X, y = data.data, data.target
st.write(data.data)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and fit the decision tree classifier model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluate the model on the testing set
accuracy = model.score(X_test, y_test)
st.write(f"Accuracy: {accuracy}")
