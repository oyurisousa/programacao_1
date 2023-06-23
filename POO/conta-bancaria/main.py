from conta import Conta
from historico import Historico
import os

def menu_principal():
    print("""
    ############## MENU PRINCIPAL ##############

    1.criar conta
    2.entrar
    3.ver contas
    0.sair 
    """)

    acao = input('O que você deseja fazer ?')
    limpa()
    if acao == '0':
        print("você saiu!")
        return
    elif acao == '1':
        
        print("=============== CRIANDO CONTA ===============")
        try:
            nome = input("Nome: ")
            saldoI = float(input("Saldo Inicial: "))
            
        except:
            limpa()
            print("Por favaor digite apenas numeros!")
            return menu_principal()
        else:
            criar_conta(nome,saldoI)
    elif acao == '2':
        try:
            num = int(input("numero da sua conta: "))
        except:
            limpa()
            print("conta inválida!")
            return menu_principal()
        else:
            limpa()
            login(num)
    elif acao == '3':
        for x in Conta.contas:
            print(x.__dict__)
        return menu_principal()
    else:
        print('opção invalida')
        return menu_principal()

def criar_conta(nome, saldoI = 0):
    
    x = Conta(nome,saldoI)
    Conta.contas.append(x)
    limpa()
    print(f"Parabéns {x.titular}, sua conta foi criada com sucesso!")
    print(f"O número da sua conta é {x.numero}")
    return menu_conta(x)

def login(conta):
    try:
        if Conta.existe_conta(conta):
            menu_conta(Conta.existe_conta(conta))
        else:
            print("Essa conta não existe!")
            menu_principal()
    except:
        limpa()
        print("Valores inválidos!")
        print("por favor digite apenas numeros.")
        return menu_principal()

def menu_conta(x):
    print(f"""
    =============== MENU CONTA ===============
    titular: {x.titular}  cont
    a: {x.numero}
    ------------------------------------------
    1.ver saldo
    2.depositar
    3.sacar
    4.transferir
    5.extrato
    0.sair
    
    """)
    acao = input("O que você deseja fazer -> ")
    limpa()
    if acao == '0':
        print("Você foi deslogado!")
        return menu_principal()
    elif acao == '1':
        limpa()
        print(f"SALDO: {x.saldo}")
        return menu_conta(x)
    elif acao == '2': 
        try:
            valor = int(input("Valor: "))
        except:
            limpa()
            print("valor inválido!")
            return menu_conta(x)
        else:
            limpa()
            x.depositar(valor)
            return menu_conta(x)
    elif acao == '3':
        try:
            valor = int(input("Valor: "))
        except:
            limpa()
            print("valor inválido!")
            return menu_conta(x)
        else:
            limpa()
            x.sacar(valor)
            return menu_conta(x)
    elif acao == '4':
        try:
            contaD = int(input(f'Conta de destino-> '))
            valor = int(input("Valor: "))
        except:
            print("valor inválido!")
            return menu_conta(x)
        else:
            x.transferir(contaD,valor)
            return menu_conta(x)
    elif acao == '5':
        print(f"============== EXTRATO ==============")
        x.extrato()
        return menu_conta(x)
    else:
        limpa()
        print("Opção invalida!")
        return menu_conta(x)

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')
    
if __name__ == "__main__":
    menu_principal()

   