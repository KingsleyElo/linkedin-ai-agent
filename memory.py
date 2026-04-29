import json
import os
from datetime import datetime, timezone

FILE_NAME = "dataset.jsonl"

def save_example(user_input, step1, step2, final_post, model):
    data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "input": user_input,
        "steps": {
            "extract": step1,
            "expand": step2
        },
        "output": final_post
    }

    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

    with open(FILE_NAME, "a") as f:
        f.write(json.dumps(data) + "\n")