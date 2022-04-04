valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

tri = (a*c)/2
cir = (3.14159 * c**2)
tra = ((a + b)*c) /2
qua = b**2
ret = a * b

print ('TRIANGULO: {:.3f}'.format(tri))
print ('CIRCULO: {:.3f}'.format(cir))
print ('TRAPEZIO: {:.3f}'.format(tra))
print ('QUADRADO: {:.3f}'.format(qua))
print ('RETANGULO: {:.3f}'.format(ret))