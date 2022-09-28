
dados = []
sexom = 'Masculino'
sexof = 'Feminino'
depo = 'deposito' 
reti = 'retirada'


while True:
    nome = input('Qual o seu nome?  ')
    dados.append(nome)
    sexo = input('Qual o seu sexo?(Digite M para masculino ou F para feminino): ')
    if sexo == 'M' or sexo == 'm':
        dados.append(sexom)
        print('Ok, sexo masculino.')
        
    elif sexo == 'F' or sexo == 'f':
        dados.append(sexof)
        print('Ok, sexo feminino.')
    datanasc = input('Qual a sua data de nascimento?')
    dados.append(datanasc)

    caixa = input('Qual caixa você gostaria de ser atendido?(responda usando números de 1 a 10)')
    if caixa == '1':
        op = input('Qual operação você gostaria de executar? Digite 1 para depósito ou 2 para retirada: ') 
        if op == '1':
            dep = float(input('Digite o valor para depósito: '))
            dados.append(depo)

        elif op == '2':
            ret = float(input('Digite o valor para retirada: '))
            dados.append(reti)
    break
print(dados)


    




