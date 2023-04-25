# streamlit_app.py
import streamlit as st
import sklearn
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


st.title("I'm doing this.")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st_name = st.sidebar.text_input('What is your name?', 'Ranya')
st.write(f"Hello {st_name}!")
    
st.header("Animal Family Classification")

# Load dataset
animal_data = {
    "Animal": ["Human", "Kangaroo", "Tuna", "Python", "Eagle", "Penguin", "Elephant", "Chameleon", "Goldfish", "Ostrich", "Lion", "Tortoise", "Shark", "Crocodile", "Sparrow"],
    "Body Covering": ["Hair", "Hair", "Scales", "Scales", "Feathers", "Feathers", "Hair", "Scales", "Scales", "Feathers", "Hair", "Scales", "Scales", "Scales", "Feathers"],
    "Warm-blooded": ["Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "No", "No", "Yes", "Yes"],
    "Feathers": ["No", "No", "No", "No", "Yes", "Yes", "No", "No", "No", "Yes", "No", "No", "No", "No", "Yes"],
    "Lays Eggs": ["No", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes"],
    "Can Fly": ["No", "No", "No", "No", "Yes", "No", "No", "No", "No", "No", "No", "No", "No", "No", "Yes"],
    "Class": ["Mammal", "Mammal", "Fish", "Reptile", "Bird", "Bird", "Mammal", "Reptile", "Fish", "Bird", "Mammal", "Reptile", "Fish", "Reptile", "Bird"]
}

data = pd.DataFrame(animal_data)

#Input widgets
st.sidebar.subheader("Input features")
body_covering = st.sidebar.selectbox("What covers the animal's body?", ("Feathers", "Hair", "Scales"))
warm_blooded = st.sidebar.selectbox("Is the animal warm-blooded?", ("Yes", "No"))
feathers = st.sidebar.selectbox("Does the animla have feathers?", ("Yes", "No"))
lays_eggs = st.sidebar.selectbox("Does the animal lay eggs?", ("Yes", "No"))
can_fly = st.sidebar.selectbox("Can the animal fly?", ("Yes", "No"))


le = LabelEncoder()
y = le.fit_transform(data['Class'])

st.write(y)
#st.stop()

# Split the dataset into features and target variable
X_string = data.drop(columns=['Class','Animal'])
X = le.fit_transform(X_string)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Model building
rf = RandomForestClassifier(max_depth = 2, max_features = 4, n_estimators = 200, random_state = 42)
rf.fit(X_train, y_train)

#Apply model to make predictions
y_pred = rf.predict([[body_covering,warm_blooded,feathers,lays_eggs,can_fly]])


# Use the trained classifier to predict the class labels of the test set
y_pred = clf.predict(X_test)

# Decode the predicted integer labels back to their original string values
y_pred = le.inverse_transform(y_pred)

# Compute the accuracy of the classifier
accuracy = accuracy_score(data.loc[y_test.index, 'Class'], y_pred)

st.write("Accuracy:", accuracy)
st.write(y_pred)

# X, y = data.data, data.target
# st.write(data)

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Define and fit the decision tree classifier model
# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)

# # Evaluate the model on the testing set
# accuracy = model.score(X_test, y_test)
# st.write(f"Accuracy: {accuracy}")
