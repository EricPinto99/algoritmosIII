from Nodo import Nodo

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanhoLista = 0

    def verificarListaVazia(self):
        if self.primeiro == None:
            return True
        else:
            return False

    def verificarTamanhoLista(self):
        return self.tamanhoLista

    def mostrarLista(self):
        nodoAtual = self.primeiro
        while (nodoAtual != None):
            print(nodoAtual.getNome(), end = " | ")
            nodoAtual = nodoAtual.getProximo()
        print(" ")

    #para inserir a gente passa o: nome do nodo e a ***posicao desejada
    def push(self, nomeNodo, indice):
       if (indice >= 0):
           #crio o primeiro nodo
            nodoCriado = Nodo(nomeNodo)
            #sprint(nodoCriado)
       if self.verificarListaVazia():
           #inserir nodo em uma lista: temos so um nodo e portanto ele é o primeiro e o ultimo
           self.primeiro = nodoCriado
           self.ultimo = nodoCriado
       else:
           #lista nao esta vazia - vamos comercar inserindo no inicio
            if (indice == 0):
                nodoCriado.setProximo(self.primeiro)
                self.primeiro = nodoCriado
            elif (indice >= self.tamanhoLista): #inserir no final
                self.ultimo.setProximo(nodoCriado)
                self.ultimo = nodoCriado
            else: #inserir no meio
                #preciso percorrer a lista até encontrar a posição desejada
               nodoAnterior = self.primeiro #backup do primeiro nodo
               nodoAtual = self.primeiro.getProximo()
               indiceAtual = 1

                #se nao é o primeiro nodo
                #comeco a percorrer a lista até encontrar
               while (nodoAtual != None):
                   if (indiceAtual == indice):
                       #primeiro inseri o nodo no meio da lista
                       nodoCriado.setProximo(nodoAtual)
                       #atualizei o encadeamento
                       nodoAnterior.setProximo(nodoCriado)

                       break
                   nodoAnterior = nodoAtual
                   nodoAtual = nodoAtual.getProximo()
                   indiceAtual +=1

       self.tamanhoLista +=1


    # metodo de remover
    def pop(self, indice):
        if not self.verificarListaVazia() and indice >= 0 and indice < self.tamanhoLista:
                flagRemove = False
                # removendo do inicio - tem apenas um elemento
                if self.primeiro.getProximo() == None:  # o proximo do primeiro nao existe ou seja  se so tem um elemento
                    # possui apenas 1 elemento
                    self.primeiro = None  # removendo o unico elemento
                    self.ultimo = None
                    flagRemove = True
                # removendo do inicio - tem mais de um elemento
                if indice == 0:  # deseja remover o primeiro elemento, mas a lista tem mais de um elemento
                    # remove do inicio, mais de um elemento
                    self.primeiro = self.primeiro.getProximo()  # removendo primeiro elemento, indice 0
                    flagRemove = True
                else:
                    # ** se chegou aqui é porque a lista possui mais de um elemento
                    # ** e a remoção nao é mais do inicio
                    nodoAnterior = self.primeiro  # fazendo backup
                    nodoAtual = self.primeiro.getProximo()
                    indiceAtual = 1
                    while(nodoAtual != None):
                        if (indiceAtual == indice):
                            nodoAnterior.setProximo(nodoAtual.getProximo())
                            nodoAtual.setProximo(None)
                            flagRemove = True
                            break
                        #se eu nao encontrar o indice, eu tenho que seguir procurando
                        nodoAnterior = nodoAtual
                        nodoAtual = nodoAtual.getProximo()
                        indiceAtual += 1

                if flagRemove:
                    # atualiza o tamanho da lista
                    self.tamanhoLista -= 1
