from llm import call_model
from memory import save_example


# 1. Extractor
def extract_insights(user_input, model):
    messages = [
        {
            "role": "system",
            "content": (
                "Extract ONLY explicit information.\n"
                "Do NOT assume structure.\n"
                "Preserve:\n"
                "- numbers\n"
                "- names (datasets, tools, concepts)\n"
                "- specific examples\n\n"
                "Output:\n"
                "FACTS:\n- ...\n"
                "CONCEPTS:\n- ..."
            )
        },
        {"role": "user", "content": user_input}
    ]

    return call_model(messages, model)


# 2. Critic (NOW produces writing guidance)
def critique_extraction(original_input, extracted_output, model):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a linked content improvement advisor.\n\n"
                "Your job is to guide writing, not evaluate.\n\n"
                "OUTPUT:\n"
                "POST GUIDANCE:\n- what to emphasize\n- what to clarify\n\n"
                "EMPHASIS POINTS:\n- key ideas that should be highlighted\n\n"
                "TONE ADVICE:\n- how the post should feel (e.g. technical, storytelling, concise)\n"
            )
        },
        {
            "role": "user",
            "content": f"""
            ORIGINAL INPUT:
            {original_input}

            EXTRACTED OUTPUT:
            {extracted_output}
            """
        }
    ]

    return call_model(messages, model)


# 3. Generator (uses BOTH signals)
def generate_linkedin_post(extracted, critique, model):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a LinkedIn content writer.\n"
                "Write a high-quality post.\n\n"
                "RULES:\n"
                "- Strong hook\n"
                "- No headers\n"
                "- Short paragraphs\n"
                "- Keep technical accuracy\n"
                "- Do NOT invent facts\n"
                "- Avoid repeating the same idea\n"
                "- Keep the post under 200 words\n"
                "- Focus on ONE core insight\n"
                "- Write in first person\n"
                "- Lead with the most surprising or specific number\n"
                "- Make it feel like a personal lesson, not a report\n"
            )
        },
        {
            "role": "user",
            "content": f"""
            EXTRACTED INSIGHTS:
            {extracted}

            WRITING GUIDANCE:
            {critique}
            """
        }
    ]

    return call_model(messages, model)


# 4. Full pipeline
def run_agent(user_input, model):
    extracted = extract_insights(user_input, model)
    critique = critique_extraction(user_input, extracted, model)
    final_post = generate_linkedin_post(extracted, critique, model)

    save_example(user_input, extracted, critique, final_post, model)

    return extracted, critique, final_post