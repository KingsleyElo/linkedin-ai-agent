# LinkedIn AI Agent v5

A ReAct-based AI agent that transforms your daily learning into professional LinkedIn posts targeting recruiters and ML/data peers.

## How It Works

The agent follows a strict **Observe → Reason → Act** loop:

1. **Observe** — Analyzes your input to extract intent, key insight, audience hook, and tone
2. **Reason** — Plans the post structure and hook before writing, constrained by post rules
3. **Act** — Generates the LinkedIn post based on the reasoning
4. **Observe Output** — A Python rule checker validates the post against defined rules, triggering a retry loop if any rule fails (max 3 attempts)

## Post Rules

- Leads with the most specific number or surprising fact
- Written in first person
- No headers or bullet points
- Under 200 words
- Focuses on one core insight
- Ends with a call to action or thought-provoking question
- Includes 3-5 relevant hashtags

## Models Supported

| Model | Provider | Notes |
|---|---|---|
| llama-3.3-70b-versatile | Groq | Fastest response |
| nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | Best quality (recommended) |
| openai/gpt-oss-120b:free | OpenRouter | Strong writing, occasional hallucinations |

## Setup

1. Clone the repo
2. Install dependencies

```bash
pip install -r requirements.txt
```
3. Add your API keys to `.env`
```env
API_KEY=your_groq_api_key
BASE_URL=https://api.groq.com/openai/v1

OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```
4. Run the app

```bash
streamlit run app.py
```

## Streamlit Cloud Deployment

Add your API keys under **Manage App → Secrets** in the Streamlit Cloud dashboard.