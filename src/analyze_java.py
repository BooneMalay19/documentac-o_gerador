import re

def analyze_java(file_path):
    """
    Analisa um arquivo Java para identificar classes, métodos e comentários associados.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except Exception as e:
        print(f"Erro ao ler o arquivo {file_path}: {e}")
        return []

    analysis = []
    comment_buffer = []

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        if stripped_line.startswith("//"):
            comment_buffer.append(stripped_line.lstrip("//").strip())
        elif stripped_line.startswith("/*"):
            comment_buffer.append(stripped_line.lstrip("/*").rstrip("*/").strip())
        elif stripped_line.startswith("*") and comment_buffer:
            comment_buffer.append(stripped_line.lstrip("*").strip())

        class_match = re.match(r"class\s+(\w+)", stripped_line)
        if class_match:
            analysis.append({
                "type": "Class",
                "name": class_match.group(1),
                "docstring": " ".join(comment_buffer) if comment_buffer else "Sem descrição."
            })
            comment_buffer = []

        method_match = re.match(r"((public|private|protected)\s+)?[\w<>]+\s+(\w+)\s*.*", stripped_line)
        if method_match:
            method_name = method_match.group(3)
            analysis.append({
                "type": "Method",
                "name": method_name,
                "docstring": " ".join(comment_buffer) if comment_buffer else "Sem descrição."
            })
            comment_buffer = []

    return analysis