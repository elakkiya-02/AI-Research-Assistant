import requests
import streamlit as st

st.title("AI Research Assistant")
st.markdown("""SUPPORTED QUERIES
            
            1. Knowledge questions 
                What is the capital of India?
            2. Calculation
                10+3
                40/5
            3. Text stat
                count words <<sentence>>"""
            )

question = st.text_input("Ask a question:")

if st.button("Submit"):
    response = requests.post( "http://127.0.0.1:8000/ask",
                              json={'question':question})
    #st.write(response.json())
    answer = response.json()['answer']
    st.success(answer)
