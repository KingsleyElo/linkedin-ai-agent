import json
import os
from datetime import datetime, timezone

FILE_NAME = "data/dataset.jsonl"


def save_example(user_input, extracted, critique, final_post, model):
    os.makedirs("data", exist_ok=True)

    data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "input": user_input,
        "extracted": extracted,
        "critique": critique,
        "output": final_post
    }

    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")