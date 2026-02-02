def extract_error(log_text):
    if "ModuleNotFoundError" in log_text:
        return "missing_dependency"
    if "command not found" in log_text:
        return "missing_command"
    if "permission denied" in log_text.lower():
        return "permission_issue"
    return "unknown_error"
