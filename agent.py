from log_parser import extract_error
from fixer import apply_fix
from runner import rerun_pipeline

def agent_think(log_text):
    print("🧠 Agent analyzing logs...")
    error_type = extract_error(log_text)
    print(f"🧩 Detected issue: {error_type}")

    apply_fix(error_type)
    rerun_pipeline()


if __name__ == "__main__":
    with open("sample_logs.txt") as f:
        logs = f.read()

    agent_think(logs)
