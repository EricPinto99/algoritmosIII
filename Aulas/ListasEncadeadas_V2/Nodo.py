class Nodo:
    #primeiro defino o construtor
    def __init__(self, nomeNodo):
        self.nomeNodo = nomeNodo
        self.proximo = None

    #vamos fazer os metodos -  gets dos parametros
    def getNome(self):
        return self.nomeNodo
    def getProximo(self):
        return self.proximo

    #vamos fazer os metodos - sets dos parametros
    def setNome(self,nomeNodo):
        self.nomeNodo = nomeNodo
    def setProximo(self, proximo):
        self.proximo = proximo

