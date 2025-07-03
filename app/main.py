# app/main.py

import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.router import answer_query
from app.feedback import save_feedback

st.set_page_config(page_title="Math Tutor Agent", page_icon="🧠")
st.title("🧠 Math Tutor Agent")

# Initialize session state variables
if "query" not in st.session_state:
    st.session_state.query = ""
if "response" not in st.session_state:
    st.session_state.response = ""
if "feedback_submitted" not in st.session_state:
    st.session_state.feedback_submitted = False

# Input form for math query
with st.form("math_form"):
    user_input = st.text_input("Ask a math question", value="", key="input_field")
    submitted = st.form_submit_button("Submit")

    if submitted and user_input.strip():
        st.session_state.query = user_input.strip()
        st.session_state.response = answer_query(st.session_state.query)
        st.session_state.feedback_submitted = False  # Reset feedback status

# Show answer
if st.session_state.response:
    st.markdown("### Answer")
    st.markdown(st.session_state.response)

# Feedback section
if st.session_state.response and not st.session_state.feedback_submitted:
    st.markdown("---")
    st.subheader("📋 Feedback")

    with st.form("feedback_form"):
        feedback = st.radio("Was this answer helpful?", ("👍 Yes", "👎 No"))
        comments = st.text_area("Additional comments (optional):")
        submit_feedback = st.form_submit_button("Submit Feedback")

        if submit_feedback:
            save_feedback(
                st.session_state.query,
                st.session_state.response,
                feedback,
                comments
            )
            st.session_state.feedback_submitted = True
            st.success("✅ Thank you for your feedback!")
