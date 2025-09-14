import re
from typing import List

def _explain_python(line: str) -> str:
    if re.match(r"^\s*#.*", line):
        return "This is a comment."
    if re.match(r"^\s*import\s+\w+", line) or re.match(r"^\s*from\s+\w+\s+import", line):
        return "Imports a module or specific names for use."
    if re.match(r"^\s*def\s+(\w+)\s*\((.*?)\)\s*:", line):
        m = re.match(r"^\s*def\s+(\w+)\s*\((.*?)\)\s*:", line)
        name, params = m.group(1), m.group(2)
        return f"Defines a function '{name}' with parameters: {params or 'none'}."
    if re.match(r"^\s*class\s+(\w+)\s*:", line):
        m = re.match(r"^\s*class\s+(\w+)\s*:", line)
        return f"Defines a class '{m.group(1)}'."
    if re.match(r"^\s*for\s+.+\s+in\s+.+:", line):
        return "Starts a for-loop that iterates over a sequence."
    if re.match(r"^\s*while\s+.+:", line):
        return "Starts a while-loop that runs while the condition is True."
    if re.match(r"^\s*if\s+.+:", line):
        return "Begins a conditional branch (if)."
    if re.match(r"^\s*elif\s+.+:", line):
        return "An additional conditional branch (elif)."
    if re.match(r"^\s*else\s*:", line):
        return "Fallback branch (else)."
    if re.match(r"^\s*try\s*:", line):
        return "Start of a try block to catch exceptions."
    if re.match(r"^\s*except\b", line):
        return "Exception handling block."
    if re.match(r"^\s*print\s*\(", line):
        return "Prints output to the console."
    if re.match(r"^\s*return\b", line):
        return "Returns a value from the function."
    if "=" in line and "==" not in line:
        return "Assigns a value to a variable."
    return "Executes a statement."

def _explain_javascript(line: str) -> str:
    if re.match(r"^\s*//", line):
        return "This is a single-line comment."
    if re.match(r"^\s*/\*", line):
        return "Start of a multi-line comment."
    if re.match(r"^\s*import\s+.+from\s+['\"].+['\"]\s*;?", line):
        return "Imports a module."
    if re.match(r"^\s*function\s+(\w+)\s*\((.*?)\)\s*{", line) or re.match(r"^\s*(const|let|var)\s+(\w+)\s*=\s*\((.*?)\)\s*=>\s*{?", line):
        return "Declares a function."
    if re.match(r"^\s*class\s+(\w+)\s*{", line):
        return "Defines a class."
    if re.match(r"^\s*(const|let|var)\s+\w+\s*=", line):
        return "Declares and assigns a variable."
    if re.match(r"^\s*for\s*\(", line) or re.match(r"^\s*while\s*\(", line):
        return "Starts a loop."
    if re.match(r"^\s*if\s*\(", line) or re.match(r"^\s*else if\s*\(", line) or re.match(r"^\s*else\s*{", line):
        return "Conditional branch."
    if re.match(r"^\s*console\.log\s*\(", line):
        return "Logs output to the console."
    if re.match(r"^\s*return\b", line):
        return "Returns a value from a function."
    return "Executes a statement."

def _explain_java(line: str) -> str:
    if re.match(r"^\s*//", line):
        return "This is a single-line comment."
    if re.match(r"^\s*/\*", line):
        return "Start of a multi-line comment."
    if re.match(r"^\s*import\s+[\w\.]+\s*;", line):
        return "Imports a class or package."
    if re.match(r"^\s*public\s+class\s+(\w+)\s*{", line) or re.match(r"^\s*class\s+(\w+)\s*{", line):
        return "Defines a class."
    if re.match(r"^\s*public\s+static\s+void\s+main\s*\(", line):
        return "Java program entry point (main method)."
    if re.match(r"^\s*(int|float|double|String|char|boolean)\s+\w+\s*=", line):
        return "Declares and assigns a variable."
    if re.match(r"^\s*for\s*\(", line) or re.match(r"^\s*while\s*\(", line):
        return "Starts a loop."
    if re.match(r"^\s*if\s*\(", line) or re.match(r"^\s*else if\s*\(", line) or re.match(r"^\s*else\s*{", line):
        return "Conditional branch."
    if re.match(r"^\s*return\b", line):
        return "Returns a value from a method."
    if re.match(r"^\s*System\.out\.println\s*\(", line):
        return "Prints output to the console."
    return "Executes a statement."

def explain_code(code: str, language: str) -> List[str]:
    """Return line-by-line plain-English explanations (very beginner-friendly)."""
    lines = code.splitlines()
    expl: List[str] = []

    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip():
            expl.append("Blank line.")
            continue

        if language == "python":
            expl.append(_explain_python(line))
        elif language == "javascript":
            expl.append(_explain_javascript(line))
        elif language == "java":
            expl.append(_explain_java(line))
        else:
            expl.append("Executes a statement.")
    return expl
