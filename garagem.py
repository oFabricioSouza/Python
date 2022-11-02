# Fabricio de Souza e Victor Bernardo

# Declaração das listas usadas.

motoristas = []
carros = []

# Repetição usada no menu.
while True:
    # Primeira parte para seleção dos menus.
    menu = input('| Seja bem-vindo(a) à garagem. \n| Digite 1 se for motorista. \n| Digite 2 se for o despachante responsável. \n| Ou 0 para sair.\n| Digite aqui: ')
    
    # Início do menu de motoristas.
    if menu == "1":
        menu_motorista = input('| Seja bem-vindo, Sr Motorista.\n| Se for novo, digite 1 para se registrar; \n| Digite 2 para logar:')
        while True:
            if menu_motorista == '1':
                nome = input('| Digite seu nome:')
                motoristas.append(nome)

                matricula = input('|Digite sua matrícula (Número de 6 dígitos que correspondem ao seu registro na empresa):')
                motoristas.append(matricula)
                break

            elif menu_motorista == '2':
                print('| Menu de login.')
                login = input('| Digite seu primeiro nome:')
                senha = input('| Digite sua senha (Sua matrícula)')

    # Início do menu de despachante.
    elif menu == "2":
        senha = input('| Seja bem-vindo ao menu de despachantes! \n Digite a senha de despachante para passar: ')
        if senha == "@rodoviario2":
            menu_despachante = input('| O que deseja ver, Sr Despachante?')
            
        else:
            print('Senha inválida')

    elif menu == "0":
        print("Operação encerrada.")
        break

print(' ================ \n F I M \n ================')
