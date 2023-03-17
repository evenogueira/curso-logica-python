
#criando uma lista

lista = ['Casa','Carro',1]

#adicionando e removendo elementos em uma lista

lista.append('Arvore')
lista.remove(1)
#acessando elementos da lista
# print(lista[0:2])

#alterando elementos lista
lista[0] = 'Cachorro'

# print(lista)
#criando uma tupla

tupla = (3,5,7,7)

tupla2 = tupla+(9,)
#acessando elementos da tupla
# print(tupla[0])
#criando nova tupla com antiga
# print(tupla)
#criando um set com

conjunto = {2,4,8}
#adicionado e removendo elementos de um set com add, remove e discard
conjunto.add(10)
conjunto.discard(20)
print(conjunto)