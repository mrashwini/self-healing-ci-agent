import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def reason_from_logs(log_text):
    prompt = f"""
You are a DevOps engineer.
Analyze the CI/CD error logs below and tell:
1. Root cause
2. Exact fix command to run

Logs:
{log_text}

Respond in JSON like:
{{
  "error": "...",
  "fix_command": "..."
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
