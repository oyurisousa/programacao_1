inteiro = 0
cont = 0
while cont < 5:
    inteiro = int(input('valor inteiro + : '))
    if inteiro < 0:
        break 
    elif inteiro == 0:
        continue
    else:
        cont +=  1
        if cont == 5:
            print("todos os dados foram inseridos com sucesso!")
        