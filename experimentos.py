ruleta= int(input("Ingresa un numero: "))
dinero = 0

while ruleta not in [1,2]:
    ruleta = int(input("Ingresa una variable valida"))



if ruleta == 1:
    dinero = 100
    print(f"Aprobado {dinero}")  # corregí "Aprovado" a "Aprobado"
else:
    print("Nos vemos, mlp")