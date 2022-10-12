
notas = []

while True:
    menu = input('Digite 1 para poder atribuir as notas dos alunos ou 2 para encerrar: ')

    if menu == '1':
        nota = float(input('Digite sua nota da média: '))
        notas.append(nota)

    elif menu == '2':
        for i in notas:
            print('Encerrado. ')
            print(sum (notas)/len(notas))
            break
    else:
        print('Digite uma opção válida.\n'),menu

