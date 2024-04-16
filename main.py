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

if __name__ == '__main__':
    while(True):
        os.system('clear')
        print(MENU_DE_OPCOES)
        opcao = None

        try:
            opcao = int(input('Digite a opcao desejada: '))

            if opcao == 1:
                pass
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
                break      
        except:
            print('[ERRO]: Opção inválida! Tente novamente.')
        input('Digite ENTER para continar...')