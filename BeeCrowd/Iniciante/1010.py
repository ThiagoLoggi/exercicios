#recebendo valores das peças 1 
codigo1 = int(input())
quantidade_peca1 = int(input())
valor_peca1 = float(input())

#totalizando valor das peças 1
total_peca1 = quantidade_peca1*valor_peca1

#recebendo valores das peças 2
codigo2 = int(input())
quantidade_peca2 = int(input())
valor_peca2 = float(input())

#totalizando valor das peças 2
total_peca2 = quantidade_peca2*valor_peca2

#calculo final
total = total_peca1+total_peca2

print(f'VALOR A PAGAR: R$ {total:,.2f}')