
import math

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

delta = b * b - 4 * a * c

print("Delta: ", delta)

if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Raiz x1: ", x1)
    print("Raiz x2: ", x2)
else:
    print("Nao existem raízes reais")