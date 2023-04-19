cont = 0
while True:
    idade = int(input("Idade: "))
    altura = float(input("altura: "))
    if altura == 0 or idade == 0:
        break
    elif idade >= 13 and altura < 1.50:
        cont += 1

print(cont)
