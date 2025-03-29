import streamlit as st
import requests

st.set_page_config(page_title="CareerMentor Chatbot", layout="wide")
st.title("🧠 CareerMentor Chatbot")

query = st.text_input("Enter your query:", placeholder="e.g., What is the average salary for ML engineers?")
if st.button("Send Query"):
    res = requests.post("http://localhost:8000/chat/", json={"query": query})
    st.json(res.json())
