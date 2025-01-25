import re

def analyze_sql(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        print(f"Erro ao ler o arquivo {file_path}: {e}")
        return []

    analysis = []

    table_matches = re.findall(r"CREATE\s+TABLE\s+(\w+)\s*(.*?);", content, re.DOTALL | re.IGNORECASE)
    for table_name, columns in table_matches:
        column_list = [col.strip() for col in columns.split(",")]
        analysis.append({
            "type": "Table",
            "name": table_name,
            "columns": column_list
        })

    index_matches = re.findall(r"CREATE\s+INDEX\s+(\w+)\s+ON\s+(\w+)", content, re.IGNORECASE)
    for index_name, table_name in index_matches:
        analysis.append({
            "type": "Index",
            "name": index_name,
            "table": table_name
        })

    return analysis