# Faça uma função que receba uma lista de inteiros e um valor inteiro. A função deve remover os elementos iguais usando o operador DEL

num_int = []

# for i in num_int:
#     print(num_int.count(i))

cont = 0

while True:
    var = int(input('Digite 5 números para atribuí-los à lista: '))
    num_int.append(var)
    cont += 1
    
    if cont == 5:
        for n in num_int:
            rep = num_int.count(n)
            # del num_int
            print(rep)

        # del num_int.count(2)
        # del num_int[0]
        # print(num_int)

        break

