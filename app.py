import streamlit as st
from agent import run_agent

st.title("LinkedIn AI Agent v5")

model = st.selectbox(
    "Choose Model",
    [
        "llama-3.3-70b-versatile",
        "openrouter/nvidia/nemotron-3-super-120b-a12b:free",
        "openrouter/openai/gpt-oss-120b:free",
    ]
)

user_input = st.text_area("What did you learn today?")

if st.button("Generate Post"):

    if not user_input.strip():
        st.warning("Please enter something first.")
    else:
        with st.spinner("Running ReAct loop... 🤖"):
            observation, thought, post = run_agent(user_input, model)

        st.subheader("👁️ Observation")
        st.write(observation)

        st.subheader("🧠 Reasoning")
        st.write(thought)

        st.subheader("📝 Final LinkedIn Post")
        st.write(post)