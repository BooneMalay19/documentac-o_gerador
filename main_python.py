from src.fetch_repo import clone_repository
from src.analyze_python import analyze_code
import os

def generate_documentation(repo_url):
    clone_dir = "cloned_repo"
    repo_path = clone_repository(repo_url, clone_dir)

    documentation = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                analysis = analyze_code(file_path)
                documentation.append({"file": file_path, "analysis": analysis})

    markdown = "# Documentação do Projeto (Python)\n\n"
    for file_doc in documentation:
        markdown += f"## Arquivo: {file_doc['file']}\n"
        if file_doc["analysis"]:
            for item in file_doc["analysis"]:
                markdown += f"### {item['type']}: {item['name']}\n"
                markdown += f"**Descrição**: {item['docstring']}\n\n"
        else:
            markdown += "Sem funções, classes ou docstrings detectadas.\n\n"

    with open("DOCUMENTATION.md", "a") as doc_file:
        doc_file.write(markdown)

    print("Documentação Python gerada em 'DOCUMENTATION.md'!")


if __name__ == "__main__":
    repo_url = input("Digite o URL do repositório Git: ")
    generate_documentation(repo_url)