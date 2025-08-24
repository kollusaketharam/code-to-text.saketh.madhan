def to_mermaid_flowchart(code: str, language: str) -> str:
    """
    Produce a very rough Mermaid flowchart.
    """
    lines = [ln.strip() for ln in code.splitlines() if ln.strip()]
    if not lines:
        return "flowchart TD\n  A[Start] --> B[End]"

    nodes = []
    edges = []
    prev = "S"
    nodes.append("S[Start]")

    idx = 0
    for ln in lines:
        idx += 1
        node_id = f"N{idx}"
        label = ln.replace('"', "'")
        if any(ln.startswith(k) for k in ("if ", "if(", "elif ", "else if", "else")):
            nodes.append(f'{node_id}{{{label}}}')
        else:
            nodes.append(f'{node_id}["{label}"]')
        edges.append(f"{prev} --> {node_id}")
        prev = node_id

    nodes.append("E[End]")
    edges.append(f"{prev} --> E")

    return "flowchart TD\n  " + "\n  ".join(nodes + edges)
