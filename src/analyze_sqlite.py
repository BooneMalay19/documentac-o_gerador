import sqlite3

def analyze_sqlite(db_path):

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados {db_path}: {e}")
        return []

    analysis = []

    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table_name, in tables:
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            analysis.append({
                "type": "Table",
                "name": table_name,
                "columns": [col[1] for col in columns]
            })
    except Exception as e:
        print(f"Erro ao analisar tabelas em {db_path}: {e}")

    conn.close()
    return analysis