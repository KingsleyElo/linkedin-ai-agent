import streamlit as st
from agent import run_agent

st.title("LinkedIn AI Agent v4")

model = st.selectbox(
    "Choose Model",
    [
        "llama-3.3-70b-versatile",
        "llama-4-scout",
        "qwen-3-32b",
        "gpt-oss-120b"
    ]
)

user_input = st.text_area("What did you learn today?")

if st.button("Generate Post"):

    if not user_input.strip():
        st.warning("Please enter something first.")
    else:
        with st.spinner("Generating... 🤖"):
            extracted, critique, final_post = run_agent(user_input, model)

        st.subheader("🧠 Extracted Insights")
        st.write(extracted)

        st.subheader("🎯 Writing Guidance (Critic)")
        st.write(critique)

        st.subheader("📝 Final LinkedIn Post")
        st.write(final_post)