import database as db
import os 

MENU_DE_OPCOES = """ ### MENU ###

    1) Inserir um novo curso
    2) Consultar cursos cadastrados
    3) Excluir um curso pelo ID
    4) Excluir todos os cursos
    5) Alterar curso pelo ID 
    6) Importar cursos de um arquivo CSV
    7) Sair
"""

def cadastra_curso(conexao):
    nome = input('Digite o nome do curso: ')
    sigla = input('Digite a sigla do curso: ')
    turno = input('Digite o turno do curso (manhã, tarde ou noite): ')
    db.cadastra_curso(conexao, nome, sigla, turno)

if __name__ == '__main__':
    # conectando com o postgreSQL
    conexao = db.conecta_bd()
    while(True):
        os.system('clear')
        print(MENU_DE_OPCOES)
        opcao = None

        try:
            opcao = int(input('Digite a opcao desejada: '))

            if opcao == 1:
                cadastra_curso(conexao)
            elif opcao == 2:
                pass
            elif opcao == 3:
                pass
            elif opcao == 4:
                pass
            elif opcao == 5:
                pass       
            elif opcao == 6:
                pass       
            elif opcao == 7:
                print('Até logo!')
                if conexao:
                    conexao.close()  
                break      
        except:
            print('[ERRO]: Opção inválida! Tente novamente.')
        input('Digite ENTER para continar...')