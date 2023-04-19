from random import randint
import os
import platform

numero_contas =  [] #armazenar numero das contas
contas = [] #armazenar todas as contas/dados




def Start():     # Inicia o programa #
    MenuInicial()


def MenuInicial():   #Menu inicial#
    print("""
############### MENU INICIAL ###############
1.Criar conta   2.ENTRAR 
0.sair   
----------------------------------------------
    """)
    try:
        acao = int(input("O que você deseja fazer-> "))
    except:
        print("Opção inválida, tente novamente")
        return MenuInicial()
    LimpaTerminal()
    if acao == 1:
        return CriarConta()
    elif acao == 2:
        Login()
    elif acao == 0:
        print("Você saiu! ")
        return
   


##ações do menu inicial ##
def CriarConta():
    numero_contas.append(GerarNumConta())
    contas.append({f"{numero_contas[-1]}":{}})
    contas[-1][f"{numero_contas[-1]}"]["titular"] = input("Titular: ")
    try:
        contas[-1][f"{numero_contas[-1]}"]["CPF"] = int(input("CPF: "))
    except:
        contas.pop()
        numero_contas.pop()
        print("digite somente numeros, por favor tente novamente!")
        MenuInicial()
    if VerifCPF(contas[-1][f"{numero_contas[-1]}"]["CPF"]) == True:
        contas.pop()
        numero_contas.pop()
        print("CPF já pertence a uma conta!")
        return MenuInicial()
    
    contas[-1][f"{numero_contas[-1]}"]["saldo"] = 0
    LimpaTerminal()
    print(f"Parabéns {contas[-1][f'{numero_contas[-1]}']['titular']} sua conta foi criada com sucesso! ")
    print(f"O numero da sua conta é {numero_contas[-1]}")
    print(numero_contas)
    return MenuPrincipal(numero_contas.index(numero_contas[-1]))


def Login():
    numConta = int(input("digite o numero da sua conta: "))
    index = False
    if numConta in numero_contas:
        index = numero_contas.index(numConta)
        return MenuPrincipal(index)
    else:
        print("A conta não existe!")
        return MenuInicial()


def MenuPrincipal(index):  #Menu Principal
    
    print(f"""
----------------------------------
Titular: {contas[index][f'{numero_contas[index]}']['titular']}
----------------------------------
############### MENU PRINCIPAL ###############
1.Mostrar Saldo   2.Depósito      
3.Saque           4.Tranferência
5.Relatório Geral 0.sair da conta
----------------------------------------------
    """)
    try:
        acao = int(input("O que você deseja fazer-> "))
    except ValueError as err:
        print('opção inválida')
        return MenuPrincipal(index)
    
    LimpaTerminal()
    if acao == 0:
        print("Você saiu!")
        return MenuInicial()
    elif acao == 1:
        return MostrarSaldo(index)
    elif acao == 2:
        return Depositar(index)
    elif acao == 3:
        return Sacar(index)
    elif acao == 4:
        return Tranferir(index)
    elif acao == 5:
        pass


## AÇÕES DO MENU PRINCIPAL ##


def MostrarSaldo(index):
    LimpaTerminal()
    print(f"Saldo: {contas[index][f'{numero_contas[index]}']['saldo']}")
    return MenuPrincipal(index)


def Depositar(index):
    try:
        valorDeposito = float(input("Valor do Depósito: "))
    except:
        print("naõ foi possivel realizar o deposito")
        return MenuPrincipal(index)
    contas[index][f'{numero_contas[index]}']['saldo'] += valorDeposito
    print("Depósito realizado com sucesso!")
    return MenuPrincipal(index)


def Sacar(index,):
    try:
        valorSaque = float(input("Valor do Saque: "))
    except:
        print("naõ foi possivel realizar o saque")
        return MenuPrincipal(index)
    if valorSaque > contas[index][f'{numero_contas[index]}']['saldo']:
        print("Não foi possivel realizar o saque!")
        print("O valor de inserido ultrapassa o saldo da conta!")
        return MenuPrincipal(index)
    else:
        contas[index][f'{numero_contas[index]}']['saldo'] -= valorSaque
        print("Saque realizado com sucesso!")
        return MenuPrincipal(index)
    
       
def Tranferir(index):

    valorTransferencia = float(input("Valor da transferência: "))
    if valorTransferencia > contas[index][f'{numero_contas[index]}']['saldo']:
        print("Não foi possivel realizar a transferencia!")
        print("O valor de inserido ultrapassa o saldo da conta!")
        return MenuPrincipal(index)
    
    contaDestino = int(input("digite o numero da conta ao qual deseja transferir: "))
    indexDestino = 0
    if contaDestino in numero_contas:
        indexDestino = numero_contas.index(contaDestino)
    else:
        print("A conta destinada não existe!")
        return MenuInicial()
    
    contas[index][f'{numero_contas[index]}']['saldo'] -= valorTransferencia
    contas[indexDestino][f'{numero_contas[indexDestino]}']['saldo'] += valorTransferencia
    print("tranferencia realizada com sucesso!")
    return MenuPrincipal(index)

## FUNÇÕES EXTRAS ##

def VerifCPF(cpf): #verificar se cpf ja existe
    for x in range(len(contas)-1):
        if contas[x][f"{numero_contas[x]}"]['CPF'] == cpf:
            return True
    return False


def GerarNumConta(): # gerar numero aleatório para a conta
    numeroConta = randint(1000,10000)  
    if numeroConta in numero_contas:
        GerarNumConta()
    else:
        return numeroConta


#função para identificar o SO e limpar o terminal
def LimpaTerminal():
    so = platform.system()
    if so == "Windows":
        return os.system("cls")
    elif so == "Linux":
        return os.system("clear")
    else:
        return

Start()
