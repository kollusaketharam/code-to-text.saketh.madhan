import re

def estimate_complexity(code: str, language: str) -> str:
    """Very lightweight heuristic for difficulty."""
    text = code.lower()

    loops = len(re.findall(r"\b(for|while)\b", text))
    branches = len(re.findall(r"\b(if|else if|elif|switch)\b", text))
    recursion = len(re.findall(r"\bdef\b|\bfunction\b|\bpublic\s+.*\b", text)) and \
                len(re.findall(r"\b(\w+)\s*\([^)]*\)\s*\{?[^}]*\1\s*\(", text))  # crude self-call

    score = loops*2 + branches + (3 if recursion else 0)

    if score <= 1:
        return "Low"
    if score <= 4:
        return "Medium"
    return "High"
