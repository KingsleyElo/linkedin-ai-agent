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
    step1, step2, final = run_agent(user_input, model)

    st.write("### Step 1")
    st.write(step1)

    st.write("### Step 2")
    st.write(step2)

    st.write("### Final Post")
    st.write(final)