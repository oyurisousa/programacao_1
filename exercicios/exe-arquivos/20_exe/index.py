posi = []
matriz = []

with open('dados.txt', "r") as file:
    for line in file:
        if len(line.split()) !=2:
            [N,M,Q] = line.split()
            
        else:
            posi.append(line.split())


for i in range(int(N)):
    matriz.append([])
    for j in range(int(M)):
        matriz[i].append(1)
for x in range(len(posi)):
    matriz[int(posi[x][0])][int(posi[x][1])] = 0


for i in matriz:
    for j in i:
        print(f"{j} ",end="")
    print()
