fatorial = int(input('valor: '))
fat = 1
if fatorial == 0 or fatorial == 1:
    print(fat)
elif fatorial > 20 or fatorial <  0:
      print('o valor deve ser maior que ou igual a 0 e menor ou igual a 20')
else:
    for x in range(2,fatorial+1):
        fat = fat * x
    print(fat)

#função recursiva
"""def fatorial(fat):
    if fat == 0:
        return 1
    elif fat == 1:
        return 1
    else:
        return fatorial(fat-1) * fat
    

print(fatorial(0))
"""