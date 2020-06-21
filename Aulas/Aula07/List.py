from Node import Node

class List:

   def __init__(self):
       self.first = None
       self.size = 0

   def __len__(self):
       return self.size

   def push(self, value):
       if self.first:
           aux = self.first
           while (aux.next):
               aux = aux.next
           aux.next = Node(value)
       else:
           self.first = Node(value)

       self.size = self.size + 1

   def addList(self, position, value):
       if position == 0:
           no = Node(value)
           no.next = self.first
           self.first = no
       else:
           preview = self.first
           for i in range(position - 1):
               if preview:
                   anterior = preview.next
           no = Node(value)
           no.next = preview.next
           preview.next = no

       self.size = self.size + 1

   def print(self):
       print()
       aux = self.first
       while (aux):
           print(aux.value, "\n")
           aux = aux.next