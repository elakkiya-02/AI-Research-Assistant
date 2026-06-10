import requests
import streamlit as st

st.title("AI Research Assistant")

question = st.text_input("Ask a question:")

if st.button("Submit"):
    response = requests.post( "http://127.0.0.1:8000/ask",
                              json={'question':question})
    #st.write(response.json())
    answer = response.json()['answer']
    st.success(answer)
