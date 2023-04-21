# streamlit_app.py
import streamlit as st
import sklearn
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


st.title("I'm doing this.")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st_name = st.sidebar.text_input('What is your name?', 'Ranya')
st.write(f"Hello {st_name}!")

st.header("Iris Classification")

# Load dataset
# data = load_iris()
animal_data = {'Animal': ['Dog', 'Cat', 'Horse', 'Bat', 'Cow', 'Eagle', 'Penguin', 'Crocodile', 'Snake', 'Lizard', 'Fish', 'Shark'],
        'Body temperature': ['Warm-blooded', 'Warm-blooded', 'Warm-blooded', 'Warm-blooded', 'Warm-blooded', 'Warm-blooded', 'Warm-blooded', 'Cold-blooded', 'Cold-blooded', 'Cold-blooded', 'Cold-blooded', 'Cold-blooded'],
        'Skin type': ['Fur', 'Fur', 'Hair', 'Fur', 'Hair', 'Feathers', 'Feathers', 'Scales', 'Scales', 'Scales', 'Scales', 'Scales'],
        'Habitat': ['Land', 'Land', 'Land', 'Air', 'Land', 'Air', 'Water', 'Water', 'Land', 'Land', 'Water', 'Water'],
        'Type of reproduction': ['Viviparous', 'Viviparous', 'Viviparous', 'Viviparous', 'Viviparous', 'Oviparous', 'Oviparous', 'Oviparous', 'Oviparous', 'Oviparous', 'Oviparous', 'Oviparous'],
        'Class': ['Mammal', 'Mammal', 'Mammal', 'Mammal', 'Mammal', 'Bird', 'Bird', 'Reptile', 'Reptile', 'Reptile', 'Fish', 'Fish']}

data = pd.DataFrame(animal_data)

le = LabelEncoder()
y = le.fit_transform(data['Class'])

# Split the dataset into features and target variable
X = data.drop('Class', axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier with a maximum depth of 3
clf = DecisionTreeClassifier(max_depth=3)

# Train the classifier on the training set
clf.fit(X_train, y_train)

# Use the trained classifier to predict the class labels of the test set
y_pred = clf.predict(X_test)

# Decode the predicted integer labels back to their original string values
y_pred = le.inverse_transform(y_pred)

# Compute the accuracy of the classifier
accuracy = accuracy_score(data.loc[y_test.index, 'Class'], y_pred)

st.write("Accuracy:", accuracy)

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
