import streamlit as st
from pymongo import MongoClient

st.title("Hello World")
if st.button("Magic"):
    st.text("Hello World")

value = st.text_input("Enter Your Name Here")

message = "No Name"
if st.button("submit"):
    message = f"Hello {value}"
st.text(message)