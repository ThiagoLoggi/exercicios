#recebendo valores
numero_funcionario = int(input())
horas = int(input())
valor_hrs = float(input())

#calculo das horas * valor por hora
salario = horas*valor_hrs

print ('NUMBER = '  ,numero_funcionario)
print (f'SALARY = U$ {salario:,.2f}')
