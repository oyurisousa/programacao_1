# não trivial - possui ao menos dois elementos
# monótomo -  todos os caracteres iguais

N = int(input())
string = input("")
soma = 0
contA = 0


def A(N, string, contA, soma):

    # verificar se é uma string não-trivial ou diferente de N
    if N < 2 or len(string) != N:
        return
    else:  # verificar os "a" e "b"
        for x in range(len(string)):
            if string[x] == "a":
                contA += 1
            elif string[x] == "b":
                if contA >= 2:
                    soma += contA
                    contA = 0
                else:
                    contA = 0
            else:
                return
        if string[-1] == "a" and contA >= 2:
            soma += contA
            print(soma)
        else:
            print(soma)


A(N, string, contA, soma)
