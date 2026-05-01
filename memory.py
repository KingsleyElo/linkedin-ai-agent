import json
import os
from datetime import datetime, timezone

FILE_NAME = "data/dataset.jsonl"


def save_example(user_input, observation, thought, post, model):
    os.makedirs("data", exist_ok=True)

    data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "input": user_input,
        "observation": observation,
        "thought": thought,
        "output": post
    }

    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")