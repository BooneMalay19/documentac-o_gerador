import ast

def analyze_code(file_path):

        with open(file_path, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read())
    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")
        return []

    analysis = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            docstring = ast.get_docstring(node)
            analysis.append({"type": "Function", "name": node.name, "docstring": docstring or "Sem descrição."})
        elif isinstance(node, ast.ClassDef):
            docstring = ast.get_docstring(node)
            analysis.append({"type": "Class", "name": node.name, "docstring": docstring or "Sem descrição."})

    return analysis