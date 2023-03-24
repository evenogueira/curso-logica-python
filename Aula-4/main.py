#loops com while e for

#while

contador = 0

while contador <= 5:
    print(contador)
    contador += 1


#for
for i in range(5):
    print(i)

#iteracao listas e tuplas
lista = ["casa","cadeira","carro","cachorro"]

for i in lista:
    print(i)

#usando o break
for i in lista:
    if i == "carro":
        break
    print(i)


#usando o continue
for i in lista:
    if i == "carro":
        continue
    print(i)