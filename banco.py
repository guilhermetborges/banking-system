from defs import depositar,sacar
from time import sleep


global valor_na_conta
valor_na_conta = 0.0
qtd_saque = 0
global extrato 
extrato = ''

while True:
    LIMITE_SAQUE = 3
    SAQUE_MAX = 500

    menu = input('''
SELECIONE UMA OPÇÃO
[1] Depositar
[2] Sacar
[3] Extrato
[4] historico
[5] Sair
==================
''') 

    if menu == '1':
        valor = float(input('insira o valor a ser depositado: '))
        valor_na_conta, extrato = depositar(valor,valor_na_conta,extrato)
    elif menu == '2':
        valor_saque = float(input('insira o valor a ser sacado [MAX 500]: '))
        valor_na_conta, extrato,qtd_saque = sacar(valor_saque, valor_na_conta,LIMITE_SAQUE,SAQUE_MAX,qtd_saque,extrato)
        
    elif menu == '3':
        print(f'Saldo: R$ {valor_na_conta:.2f}')
           
    elif menu == '4':
        print("\nHistórico de Transações:")
        print(extrato if extrato else "Nenhuma transação realizada.")
            
    elif menu == '5':
        print('Encerrando o programa...')
        sleep(0.5)
        print('...')
        sleep(0.4)
        print('...')
        sleep(0.2)
        print('Programa encerrado')
        break
    else:
        print('Opção inválida')
        print('Por favor, escolha uma opção válida.')
