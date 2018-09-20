import math
x1 = int(input("Digite o valor de x1: "))
x2 = int(input("Digite o valor de x2: "))
y1 = int(input("Digite o valor de y1: "))
y2 = int(input("Digite o valor de y2: "))
#Calcular o valor da distancia entre os pontos
d = math.sqrt( (x1-x2) **2 + (y1-y2) **2)
#Imprima o valor
print("A distância entre os pontos é: ", d)