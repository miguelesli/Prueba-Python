var ="M"
lista=["Esli", "Alvarez", 1.85, 409010947,var]
print(lista)
print(len(lista[1]))##ver el tamaño del elemento numero 2 de la lista
##ára lusar len la sintaxis es len(variable)
print(type(lista[4]))
print(type(lista[3]))
print(type(lista[2]))

lista.append("incercion") ##append adjunta o añade al final un dato o variable mas l final de la lista
##lista.extend(12,64,67)##no funciono no entendi
lista.insert(3,89)
lista.insert(0,"fdfad")
print (lista)
print(lista.index(var))##inde permite ver el numero de indice de la lista donde se encuentra una variable
print(lista.index(lista[2]))##redundante pero queria ver si la sintaxis era la correcta


input(";;;;;;;;;")
