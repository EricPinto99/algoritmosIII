from ListaEncadeada import ListaEncadeada

lista = ListaEncadeada()

#print(lista)


#teste de insercao na lista
#######inserindo no inicio
lista.push("Eduarda", 0)
lista.mostrarLista()
print("Tamanho da lista: ", lista.tamanhoLista)

#inserindo no final
lista.push("Mario", 1)
lista.mostrarLista()
print("Tamanho da lista: ", lista.tamanhoLista)

#inserindo no meio
lista.push("Carlos", 1)
lista.mostrarLista()
print("Tamanho da lista: ", lista.tamanhoLista)

#inserindo no final
lista.push("Rubinho",3)
lista.mostrarLista()
print("Tamanho da lista: ", lista.tamanhoLista)

lista.push("Felipe",0)
lista.mostrarLista()
print("Tamanho da lista: ", lista.tamanhoLista)

# lista.mostrarLista()
#inserindo no meio
# lista.push("Meio",2)
# lista.mostrarLista()
# print("Tamanho da lista: ", lista.tamanhoLista)
#
print("------------ Removendo ---------")
##removendo
##do inicio
lista.pop(0)
lista.mostrarLista()
print("Tamanho da lista: ", lista.tamanhoLista)
##removendo do meio
lista.pop(1)
lista.mostrarLista()
print("Tamanho da lista: ", lista.tamanhoLista)
## #removendo do final
lista.pop(2)
lista.mostrarLista()
print("Tamanho da lista: ", lista.tamanhoLista)
