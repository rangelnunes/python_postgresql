import psycopg2

parametros = {
    "host": "localhost",
    "dbname": "aula_python_postgresql",
    "user": "postgres",
    "password": "pgsql"
}

CRIA_TABELA_CURSO = """
    create table if not exists curso(
	id_curso serial primary key,
	nome varchar(60) not null unique,
	sigla char(5) not null,
	turno varchar(40) check(turno in ('manhã', 'tarde', 'noite'))
);
"""

def conecta_bd():
    conexao = None
    try:
        conexao = psycopg2.connect(**parametros) 
        print('Conexão estabelecida com sucesso!')
    except Exception as erro:
        print('[ERRO]: ', erro)
    return conexao

def cria_tabelas(conexao):
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(CRIA_TABELA_CURSO)
                print('Tabela criada com sucesso!')
                conexao.commit()
    except Exception as erro:
        print('[ERRO]: ', erro)

if __name__ == '__main__':
    conexao = conecta_bd()
    cria_tabelas(conexao)