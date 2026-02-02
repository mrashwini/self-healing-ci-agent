import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def reason_from_logs(log_text):
    prompt = f"""
You are a senior DevOps engineer.

Analyze the CI/CD error logs below and respond ONLY in valid JSON.

Logs:
{log_text}

Return JSON in this format:
{{
  "error": "short root cause",
  "fix_command": "shell command to fix the issue",
  "confidence": 0.0,
  "explanation": "why this fix will work"
}}

Confidence must be between 0 and 1.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
