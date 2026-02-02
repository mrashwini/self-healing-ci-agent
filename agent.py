import json
import os
from llm_reasoner import reason_from_logs
from log_parser import extract_error
from fixer import apply_fix

def agent_think(log_text):
    print("🧠 Agent started")

    # ---- 1️⃣ Try LLM first ----
    try:
        print("🤖 Trying LLM reasoning...")
        reasoning = reason_from_logs(log_text)
        decision = json.loads(reasoning)

        fix_cmd = decision.get("fix_command")
        if fix_cmd:
            print(f"🔧 LLM suggested fix: {fix_cmd}")
            os.system(fix_cmd)
            return
        else:
            print("⚠️ LLM gave no fix")

    except Exception as e:
        print("⚠️ LLM failed, falling back to rules:", e)

    # ---- 2️⃣ Fallback: rule-based fix ----
    print("🛟 Using rule-based fallback")
    error_type = extract_error(log_text)
    apply_fix(error_type)


if __name__ == "__main__":
    with open("sample_logs.txt") as f:
        logs = f.read()

    agent_think(logs)
