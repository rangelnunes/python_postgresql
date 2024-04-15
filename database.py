import psycopg2

paramentros = {
    "host": "localhost",
    "dbname": "aula_python_postgresql",
    "user": "postgres",
    "password": "pgsql"
}

def conecta_bd():
    conexao = None
    try:
        conexao = psycopg2.connect(**paramentros)
        print('Conexão realizada com sucesso!')
    except Exception as erro:
        print('[ERRO]: ', erro)
    return conexao

if __name__ == '__main__':
    conexao = conecta_bd()