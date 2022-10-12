
# tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    num = float(input('Digite um número para ver sua tabuada: '))
    op = input(' ============================ \n Digite a operação desejada: \n Use + ou mais para soma. \n Use - ou menos para subtração \n Use x ou mult para multiplicar \n Use / ou div para dividir.\nUse ** ou exp para elevar \n ============================\n Ou digite sair para encerar\n  : ')

    if op == '+' or op =='mais':
        for i in range(1,11):
            print(f'{num} + {i}=', num + i)

    elif op == '-' or op =='menos':
        for i in range(1,11):
            print(f'{num} - {i}=', num - i)
    
    elif op == 'x' or op =='mult':
        for i in range(1,11):
            print(f'{num} x {i}=', num * i)

    elif op == '/' or op =='div':
        for i in range(1,11):
            print(f'{num} dividido por {i}=', num / i)

    elif op == '**' or op =='exp':
        for i in range(1,11):
            print(f'{num} elevado por {i}=', num ** i)
    
    elif op == 'sair':
        print('ENCERRADO.\nObrigado por usar nosso app.')
        break
        
    
    else:
        print('Valor Invalidos')