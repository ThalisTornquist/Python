import sqlite3

conexao = sqlite3.connect('usuarios_arquivo_sql.db')

cursor = conexao.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios_arquivo_sql(
        nome TEXT,
        idade INTEGER
        )   
    """
)

conexao.commit()
conexao.close()