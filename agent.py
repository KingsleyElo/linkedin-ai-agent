from llm import call_model
from memory import save_example


# 1. Observe Input - understand the environment
def observe_input(user_input, model):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a LinkedIn content strategist.\n"
                "Your audience is recruiters and ML/data peers.\n\n"
                "Analyze the user input and extract:\n"
                "INTENT: What is this post trying to communicate?\n"
                "KEY INSIGHT: The single most compelling fact or lesson\n"
                "AUDIENCE HOOK: Why would a recruiter or ML peer care?\n"
                "TONE: technical, storytelling, or reflective?\n"
            )
        },
        {"role": "user", "content": user_input}
    ]
    return call_model(messages, model)


# 2. Reason - think about how to write the post
def reason(observation, failed_rules, model):
    failed_section = (
        f"\nPREVIOUS ATTEMPT FAILED THESE RULES:\n{failed_rules}\n"
        "Think carefully about how to fix each one before writing."
        if failed_rules else
        "This is the first attempt. Plan how to write the best possible post based on the observation."
    )
    messages = [
        {
            "role": "system",
            "content": (
                "You are a LinkedIn writing strategist.\n"
                "Your job is to reason about how to write the post based on the observation BEFORE writing it.\n\n"
                "OUTPUT:\n"
                "THOUGHT: Your step-by-step reasoning about how to approach the post\n"
                "PLAN: Specific decisions — what the hook will be, what to emphasize, tone\n"
            )
        },
        {
            "role": "user",
            "content": f"OBSERVATION:\n{observation}{failed_section}"
        }
    ]
    return call_model(messages, model)


# 3. Act - generate the post based on reasoning
def generate_post(observation, thought, model):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a LinkedIn content writer targeting recruiters and ML peers.\n\n"
                "RULES:\n"
                "- Lead with the most specific number or surprising fact\n"
                "- Write in first person\n"
                "- No headers\n"
                "- Short paragraphs\n"
                "- Under 200 words\n"
                "- Focus on ONE core insight\n"
                "- End with a lesson or question\n"
            )
        },
        {
            "role": "user",
            "content": (
                f"OBSERVATION:\n{observation}\n\n"
                f"REASONING & PLAN:\n{thought}"
            )
        }
    ]
    return call_model(messages, model)


# 4. Observe Output - Python rule checker (no LLM call)
def observe_output(post):
    checks = {
        "under_200_words": len(post.split()) < 200,
        "starts_with_number": post.strip()[0].isdigit(),
        "first_person": "I " in post,
        "no_headers": "#" not in post,
        "no_bullet_points": "- " not in post and "* " not in post,
    }
    passed = all(checks.values())
    failed = [rule for rule, ok in checks.items() if not ok]
    return passed, failed


# 5. Full ReAct loop
def run_agent(user_input, model, max_retries=3):

    # First observation
    observation = observe_input(user_input, model)

    failed_rules = []
    thought = ""
    post = ""

    for attempt in range(max_retries):
        print(f"\n--- Attempt {attempt + 1} ---")

        # Reason about observation and any previous failures
        thought = reason(observation, failed_rules, model)

        # Act - generate post based on reasoning
        post = generate_post(observation, thought, model)

        # Observe output with Python tools
        passed, failed_rules = observe_output(post)

        print(f"Rules passed: {passed}")
        if failed_rules:
            print(f"Failed rules: {failed_rules}")

        if passed:
            print("✅ Post passed all rules.")
            break

    save_example(user_input, observation, thought, post, model)
    return observation, thought, post