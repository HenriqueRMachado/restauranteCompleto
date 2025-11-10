import pyodbc

# Substitua pelos seus dados reais
server = r'localhost\SQLSERVERWAL' # Ex: 'localhost' ou 'NOME_DA_INSTANCIA'
database = 'RESTAURANTEWAL'

# String de conexão com autenticação do Windows
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};' # Verifique o nome exato do driver instalado
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

try:
    # Conectar ao banco de dados
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Conexão bem-sucedida!")

except pyodbc.Error as ex:
    sql_state = ex.args[0]
    if sql_state == '08001':
        print("Erro: O servidor SQL não foi encontrado.")
    else:
        print(f"Erro na conexão: {ex}")

finally:
    # Fechar o cursor e a conexão
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()
