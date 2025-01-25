from src.analyze_sql import analyze_sql
from src.analyze_sqlite import analyze_sqlite
from src.fetch_repo import clone_repository
import os

def generate_documentation(repo_url):
    clone_dir = "cloned_repo"
    repo_path = clone_repository(repo_url, clone_dir)

    documentation = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".sql"):
                analysis = analyze_sql(file_path)
                documentation.append({"file": file_path, "analysis": analysis})
            elif file.endswith(".sqlite") or file.endswith(".db"):
                analysis = analyze_sqlite(file_path)
                documentation.append({"file": file_path, "analysis": analysis})

    markdown = "\n# Documentação do Projeto (SQL e SQLite)\n\n"
    for file_doc in documentation:
        markdown += f"## Arquivo: {file_doc['file']}\n"
        if file_doc["analysis"]:
            for item in file_doc["analysis"]:
                markdown += f"### {item['type']}: {item['name']}\n"
                if item["type"] == "Table":
                    markdown += f"**Colunas**: {', '.join(item['columns'])}\n\n"
                elif item["type"] == "Index":
                    markdown += f"**Tabela**: {item['table']}\n\n"
        else:
            markdown += "Nenhuma tabela ou índice detectado.\n\n"

    with open("DOCUMENTATION.md", "a") as doc_file:
        doc_file.write(markdown)

    print("Documentação SQL/SQLite gerada em 'DOCUMENTATION.md'!")


if __name__ == "__main__":
    repo_url = input("Digite o URL do repositório Git: ")
    generate_documentation(repo_url)