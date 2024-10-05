from Fila.Node import Node
from Fila.Queue import Queue

node = Node(1)
node2 = Node(2)
#print(node.valor)

fila = Queue()
fila.add(node)
fila.add(node2)
print(fila.get())