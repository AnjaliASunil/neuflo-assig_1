import streamlit as st
import pickle


# Load the model
model = pickle.load(open("C:/Users/anjal/Downloads/savedmodel_logistic.sav", 'rb'))

# Streamlit app
st.title("Iris Flower Prediction")

# Input form
sepal_length = st.number_input("Enter Sepal Length:")
sepal_width = st.number_input("Enter Sepal Width:")
petal_length = st.number_input("Enter Petal Length:")
petal_width = st.number_input("Enter Petal Width:")

# Predict button
if st.button("Predict"):
    # Make prediction
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    result = model.predict(features)[0]

    # Display result
    st.success(f"Predicted Class: {result}")