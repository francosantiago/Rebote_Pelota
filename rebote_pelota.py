"""NÚMERO DE REBOTES QUE DA UNA PELOTA"""


print("-----------------------------------------------")
print("--CALCULAR EL NÚMERO DE REBOTES DE UNA PELOTA--")
print("-----------------------------------------------")

H = int(input("Ingrese la altura de lanzamiento de la pelota: "))
A = H/5
N = 0


while H > A:
    H = H - (H*0.10)
    N = N + 1

print("el Número de veces que rebotara la pelota antes de no alcanzar la quinta parte de su altura incial sera ", N)
