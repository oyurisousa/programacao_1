base = int(input('base: '))
expoente = int(input('expoente: '))
resp = base

if expoente == 0:
    print(1)
else:
    for x in range(expoente - 1):
        resp = resp * base
    print(resp)


#print(base ** expoente)