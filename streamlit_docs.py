# streamlit_app.py
import streamlit as st
import sklearn
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

st.set_page_config(
    page_title="Animal Identification ML App",
    page_icon="🦍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Animal Identification ML App")

st.header("This is the data we are working with.")

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

#Convert the dictionary to a Pandas dataframe
data = pd.DataFrame(animal_data)
st.write(data)

#Input widgets
st.sidebar.subheader("Input features")
body_covering = st.sidebar.selectbox("What covers the animal's body?", ("Feathers", "Hair", "Scales"))
warm_blooded = st.sidebar.selectbox("Is the animal warm-blooded?", ("Yes", "No"))
feathers = st.sidebar.selectbox("Does the animla have feathers?", ("Yes", "No"))
lays_eggs = st.sidebar.selectbox("Does the animal lay eggs?", ("Yes", "No"))
can_fly = st.sidebar.selectbox("Can the animal fly?", ("Yes", "No"))



# Encode the categorical target variable as integer labels
le = LabelEncoder()
y = le.fit_transform(data['Class'])
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [0])], remainder='passthrough')
X = ct.fit_transform(data.drop(columns=['Class', 'Animal']))

st.write(y)
st.write(X)
#Data splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Create a random forest classifier with 100 trees and a maximum depth of 3
clf = RandomForestClassifier(n_estimators=100, max_depth=3)

# Train the classifier on the training set
clf.fit(X_train, y_train)

# Use the trained classifier to predict the class labels of the test set
y_pred = clf.predict(X_test)

# Decode the predicted integer labels back to their original string values
y_pred = le.inverse_transform(y_pred)

# Compute the accuracy of the classifier
accuracy = accuracy_score(data.loc[y_test.index, 'Class'], y_pred)

print("Accuracy:", accuracy)
