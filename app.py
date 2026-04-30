import streamlit as st
from agent import run_agent

st.title("LinkedIn AI Agent v4")

model = st.selectbox(
    "Choose Model",
    [
        "llama-3.3-70b-versatile",
        "openrouter/nvidia/nemotron-3-super-120b-a12b:free",
        "openrouter/openai/gpt-oss-120b:free",
        "openrouter/google/gemma-4-31b-it:free",
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