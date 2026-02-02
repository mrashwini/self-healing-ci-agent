import json
import os
from llm_reasoner import reason_from_logs
from log_parser import extract_error
from fixer import apply_fix

CONFIDENCE_THRESHOLD = 0.7

def agent_think(log_text):
    print("🧠 Agent started")

    # ---- Try LLM reasoning ----
    try:
        reasoning = reason_from_logs(log_text)
        decision = json.loads(reasoning)

        confidence = decision.get("confidence", 0)
        fix_cmd = decision.get("fix_command")
        explanation = decision.get("explanation", "")

        print(f"🤖 LLM confidence: {confidence}")
        print(f"📝 Explanation: {explanation}")

        if fix_cmd and confidence >= CONFIDENCE_THRESHOLD:
            print(f"🔧 Applying LLM fix: {fix_cmd}")
            os.system(fix_cmd)
            return

        print("⚠️ Confidence too low or no fix provided")

    except Exception as e:
        print("⚠️ LLM failed:", e)

    # ---- Fallback ----
    print("🛟 Falling back to rule-based fix")
    error_type = extract_error(log_text)
    apply_fix(error_type)


if __name__ == "__main__":
    with open("sample_logs.txt") as f:
        logs = f.read()

    agent_think(logs)
