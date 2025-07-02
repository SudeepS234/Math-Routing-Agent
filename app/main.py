import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from agents.router import answer_query
from app.feedback import save_feedback  # <-- Add this import

st.title("🧠 Math Tutor Agent")
query = st.text_input("Ask a math question")

response = ""
if st.button("Submit"):
    if query:
        response = answer_query(query)
        st.markdown(response)
    else:
        st.warning("Please enter a question.")

# Feedback section
if response:
    st.markdown("### Was this answer helpful?")
    feedback = st.radio("Your feedback:", ("👍 Yes", "👎 No"))
    comments = st.text_area("Additional comments (optional):")
    if st.button("Submit Feedback"):
        save_feedback(query, response, feedback, comments)
        st.success("Thank you for your feedback!")