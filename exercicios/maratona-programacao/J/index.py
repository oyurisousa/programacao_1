# linha1  - N -  numero de rodadas
# linha2 - cartas de joão
# linha3 - cartas de maria
# linha 4 - N inteiros, as cartas comuns

cartas = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, '11': 10, '12': 10, '13': 10, }
countCartas = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
               '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0}

# for x, i in enumerate(cartas):
#    print(cartas[i])


def count_cartas(lista):
    for x in lista:
        countCartas[x] += 1


# declaracao de variaves através do prompt
num_rodadas = int(input("num-rodadas: "))

cartas_joao = input("cartas João: ")
cartas_maria = input("cartas maria: ")
cartas_rodadas = input("cartas das rodadas: ")

# split para virra lista
cartas_joao = cartas_joao.split()
count_cartas(cartas_joao)
cartas_maria = cartas_maria.split()
count_cartas(cartas_maria)
cartas_rodadas = cartas_rodadas.split()
count_cartas(cartas_rodadas)

# soma das cartas
sum_joao = cartas[cartas_joao[0]] + cartas[cartas_joao[1]]
sum_maria = cartas[cartas_maria[0]] + cartas[cartas_maria[1]]

# subtração

limit_joao = 23 - sum_joao
limit_maria = 23 - sum_maria

# somar as rodadas

for x in range(num_rodadas):
    limit_joao -= cartas[cartas_rodadas[x]]
    limit_maria -= cartas[cartas_rodadas[x]]


# condições
def mJ(c, i):
    if limit_joao == i:
        print(-1)
        return
    elif countCartas[f"{c}"] == 4:
        i += 1
        print('oi')
        return mJ(c+1, i)
    else:
        print(limit_joao+i)
        return


def jM(c, i):
    if i > limit_joao:
        print(-1)
        return
    elif countCartas[f"{c}"] == 4:
        i += 1
        return jM(c+1, i)
    else:
        print(limit_joao+i)
        return


if limit_maria < limit_joao:

    if countCartas[f"{limit_maria}"] == 4:
        print(limit_maria+1)
    else:
        print(limit_maria)
elif limit_maria > limit_joao:
    if countCartas[f"{limit_joao + 1}"] == 4:
        jM(limit_joao+2, 2)
    else:
        print(limit_joao + 1)
else:
    print(23- limit_maria)


"""print(limit_joao)
print(limit_maria)
"""
