import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from agents.router import answer_query

st.title("🧠 Math Tutor Agent")
query = st.text_input("Ask a math question")

if st.button("Submit"):
    if query:
        response = answer_query(query)
        st.markdown(response)
    else:
        st.warning("Please enter a question.")
