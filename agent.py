from llm import call_model

def run_agent(user_input, model):
    step1 = call_model([
        {"role": "system", "content": "Extract key insights."},
        {"role": "user", "content": user_input}
    ], model)

    step2 = call_model([
        {"role": "system", "content": "Expand insight simply."},
        {"role": "user", "content": step1}
    ], model)

    final = call_model([
        {"role": "system", "content": "Write LinkedIn post (hook, body, takeaway)."},
        {"role": "user", "content": step2}
    ], model)

    return step1, step2, final