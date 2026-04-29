import streamlit as st
from agent import run_agent

st.title("LinkedIn AI Agent")

model = st.selectbox(
    "Choose Model",
    [
        "llama-3.3-70b-versatile",
        "mistral-7b-instruct",
        "gemma-7b-it"
    ]
)

user_input = st.text_area("What did you learn today?")

if st.button("Generate"):
    if not user_input.strip():
        st.warning("Please enter something first.")
    else:
        with st.spinner("Thinking... 🤖"):
            step1, final = run_agent(user_input, model)

        st.subheader("Step 1: Extracted Insights")
        st.write(step1)

        st.subheader("Final LinkedIn Post")
        st.write(final)