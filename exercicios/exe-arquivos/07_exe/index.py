vetor = input("vetor: ").split()

for x in vetor:
    try:
        vetor[vetor.index(x)] = bin(int(x))[2:] + '\n'
    except:
        vetor[vetor.index(x)] = "0" + '\n'

with open('binario.txt','a') as file:
    file.writelines(vetor)
