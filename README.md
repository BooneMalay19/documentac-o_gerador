# Gerador de Documentação

Este projeto gera automaticamente a documentação de um repositório Git contendo arquivos Python, Java, JavaScript, SQL e SQLite. Ele analisa funções, classes, métodos, parâmetros, tabelas e tipos de retorno, criando um arquivo `DOCUMENTATION.md`.

## Como Usar

1. **Clone o Repositório:**
   Certifique-se de ter `git` instalado em seu sistema.
   ```bash
   git clone https://github.com/BooneMalay19/documentac-o_gerador.git
   
2. Entre no diretório
   ```bash
   cd documentac-o_gerador/

3. Instale das dependências do arquivo requeriments.txt
   ```bash
   pip install -r requirements.txt
   
4. para criar a documentação digite a linguagem ou banco de dados que deseja gerar.
4.1 Para Python:
   
       python main_python.py
   
4.2 Para JavaScript:
   
       python main_javascript.py
   
4.3 Para Java:
   
       python main_java.py

4.4 Para SQL/SQLite:
   
       python main_sql.py

5. Com isso ele vai pedir para colocar a url do repositório desejado, analisar e gerar um arquivo MarkDown chamada DOCUMENTATION.md
