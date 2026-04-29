from llm import call_model


def extract_insights(user_input, model):
    """
    Step 1: Extract only key technical insights.
    Keep it compressed and precise.
    """

    messages = [
        {
            "role": "system",
            "content": (
                "Extract ONLY the key concepts, technical ideas, and important details. "
                "Keep it concise (3–6 bullet-like lines). "
                "Strictly preserve technical terms exactly as written "
                "(e.g., metrics, cross-validation, NaijaSenti). "
                "Do NOT explain or expand."
            )
        },
        {"role": "user", "content": user_input}
    ]

    return call_model(messages, model)


def generate_linkedin_post(extracted_insights, model):
    """
    Step 2: Directly generate final LinkedIn post.
    """

    messages = [
        {
            "role": "system",
            "content": (
                "You are a LinkedIn content writer. "
                "Turn the input into a high-quality post. "
                "Rules: "
                "- Start with a strong hook "
                "- No section headers (no 'Step 1', 'Takeaway', etc.) "
                "- Use short paragraphs "
                "- Make it engaging and natural "
                "- Preserve technical accuracy (do not change terms like metrics, cross-validation) "
                "- Keep it concise but insightful"
            )
        },
        {"role": "user", "content": extracted_insights}
    ]

    return call_model(messages, model)


def run_agent(user_input, model):
    """
    Full pipeline
    """

    step1 = extract_insights(user_input, model)
    final_post = generate_linkedin_post(step1, model)

    return step1, final_post