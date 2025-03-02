from time import sleep

def opc():
    opc = '''\n==================
    SELECIONE UMA OPÇÃO\n
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] historico
    [5] novo usuario
    [6] criar conta
    [7] listar contas
    [8] Sair
    ==================
    ''' 
    return input(opc)
        


def depositar(contas):

    cpf = int(input('Insira o CPF: '))
    if cpf not in [contas["cpf"] for contas in contas]:
        print("\n@@@ Usuário não encontrado, fluxo de depósito encerrado! @@@")
        return contas
    else:
        valor = float(input('insira o valor a ser depositado: '))
        if valor <= 0:
            print("\nVALOR INVALIDO\n")
            extrato += f'Valor inválido\n'
            return contas
        for contas in contas: 
            if contas["cpf"] == cpf:
                contas["saldo"] += valor
                contas["extrato"]  += f'Deposito: {valor}\n'
                print('=============\nDeposito realizado com sucesso\n______________')
                return contas["saldo"], contas["extrato"]
  
def sacar(contas,LIMITE_SAQUE,SAQUE_MAX,qtd_saque):
    cpf = int(input('Insira o CPF: '))
    valorsaque = int(input('Insira o valor a ser sacado: '))

    if cpf not in [contas["cpf"] for contas in contas]:
        print("\n@@@ Usuário não encontrado, fluxo de saque encerrado! @@@")        
        return None
    elif valorsaque > SAQUE_MAX:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\nsaque maior que o permitido\n')     
        return None
    else:
        for contas in contas:
            if contas["cpf"] == cpf:
                if valorsaque > contas["saldo"]:
                    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\nSaldo insuficiente\n')
                    return None
                else:
                        contas["saldo"] -= valorsaque
                        contas["extrato"] +=(f'Saque: {valorsaque}\n')
                        print('\n=-=-=-=-=-=-=-==\nSaque realizado com sucesso\n=-=-=-=-=-=-=-==\n')
                        return contas

def exibir_saldo(contas):
    cpf = int(input('Insira o CPF: '))
    if cpf not in [contas["cpf"] for contas in contas]:
        print("\n@@@ Usuário não encontrado, fluxo de exibição de saldo encerrado! @@@")
        return None
    else:
        for contas in contas:
            if contas["cpf"] == cpf:
                print("\n================ EXTRATO ================")
                print(f"\nSaldo:\t\tR$ {contas['saldo']:.2f}")
                print("==========================================")
        
def historico(conta):
    cpf = int(input('Insira o CPF: '))
    if cpf not in [contas["cpf"] for contas in conta]:
        print("\n@@@ Usuário não encontrado, fluxo de exibição de extrato encerrado! @@@")
        return None
    else:
        for contas in conta:
            if contas["cpf"] == cpf:
                    print("\n================ HISTÓRICO ================")
                    print(f"\n{contas['extrato']}")
                    print("==========================================")
                    return conta

def criar_usuario(cpf,nome,usuarios):

    if cpf in [usuario["cpf"] for usuario in usuarios]:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return None
    else:
        usuarios.append({"nome": nome, "cpf": cpf} )
        print("=== Usuário criado com sucesso! ===")
        return usuarios

def criar_conta(contas,usuarios,saldo=0.0,extrato=''):
    cpf = int(input("Informe o CPF do usuário: "))
    if cpf not in [usuario["cpf"] for usuario in usuarios]:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return None
    elif cpf in [conta["cpf"] for conta in contas]:
        print("\n@@@ Já existe conta para esse CPF! @@@")
        return None
    else:
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                nome = usuario["nome"]
        print("\n=== Conta criada com sucesso! ===")
        contas.append({"cpf" : cpf,"nome" : nome, "saldo" : saldo, "extrato" : extrato})
        print(contas)
        return contas
    
def listar_contas(contas):
    for conta in contas:
        print(f"CPF: {conta['cpf']}\nNome: {conta['nome']}\nSaldo: {conta['saldo']}\n")

def main():
    
    qtd_saque = 0
    usuarios =  []
    contas = []
    LIMITE_SAQUE = 3
    SAQUE_MAX = 500.00

    while True:


        menu = opc()

        if menu == '1':
            depositar(contas)
        elif menu == '2':
            
            sacar(contas,LIMITE_SAQUE,SAQUE_MAX,qtd_saque)
            
        elif menu == '3':
            exibir_saldo(contas)
            
        elif menu == '4':
            historico(contas)
        
        elif menu == '5':
            cpf = int(input("Informe o CPF do usuário: "))
            nome = input("Informe o nome completo: ")
            criar_usuario(cpf, nome, usuarios)
            
            
        elif menu == '6':
            criar_conta(contas,usuarios)
            print(contas)
        
        elif menu == '7':
            listar_contas(contas)
                
        elif menu == '8':
            sleep(1)
            print('Encerrando o programa...\n', '...', '\n\nPROGRAMA ENCERRADO') 
            break
        else:
            print('Opção inválida\n')
            print('Por favor, escolha uma opção válida.\n=====================\n')


main()