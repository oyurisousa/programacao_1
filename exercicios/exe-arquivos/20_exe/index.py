[N,M,Q] = input("NMQ: ").split()
posi = []
matriz = []
for x in range(int(Q)):
    posi.append(input(f"p{x}: ").split())

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