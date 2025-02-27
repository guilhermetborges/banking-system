def depositar(valor,valor_na_conta,extrato):
    
    valor_na_conta += valor
    extrato += f'Deposito: {valor}\n'
    print('Deposito realizado com sucesso')
    return valor_na_conta, extrato
  

def sacar(valorsaque,valor_na_conta,LIMITE_SAQUE,SAQUE_MAX,qtd_saque,extrato):

    if valorsaque > SAQUE_MAX:
        print('Limite de saque excedido')
        extrato += f'Limite de saque excedido\n'
        return valor_na_conta, extrato, qtd_saque
    elif valorsaque > valor_na_conta:
        print('Saldo insuficiente')
        extrato += f'Saldo insuficiente\n'
        return valor_na_conta, extrato, qtd_saque
    elif qtd_saque >= LIMITE_SAQUE:
        print('Limite de saque dia excedido')
        extrato += f'Limite de saque dia excedido\n'
        return valor_na_conta, extrato, qtd_saque
    else:
        valor_na_conta -= valorsaque
        qtd_saque += 1
        extrato += f'Saque: {valorsaque} \n'
        print('Saque realizado com sucesso')
        return valor_na_conta, extrato, qtd_saque
    
   

