from llm import call_model

def run_agent(user_input, model):
    step1 = call_model([
        {"role": "system", "content": "Extract the main concept, why it matters, and when it is used, Strictly preserve all important technical terms and metrics exactly as written (e.g., metrics, cross-validation). Do not replace or simplify them."},
        {"role": "user", "content": user_input}
    ], model)

    step2 = call_model([
        {"role": "system", "content": "Explain this clearly in simple terms, but preserve all important technical concepts and wording (e.g., metrics, cross-validation). Do not oversimplify."},
        {"role": "user", "content": step1}
    ], model)

    final = call_model([
        {"role": "system", "content": "Write a clean LinkedIn post: - Start with a strong hook, - No section headers, - Use short paragraphs, - Make it easy to read, - Maintain technical accuracy (preserve key terms like 'metrics', 'cross-validation')"},
        {"role": "user", "content": step2}
    ], model)

    return step1, step2, final