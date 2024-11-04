from typing import Any
#Implementar el TAD Pila (Stack) utilizando una lista enlazada

class Nodo:
    #Clase para representar un nodo en una lista enlazada.
    def __init__(self, dato: Any = None, prox=None):
      self.dato = dato
      self.prox = prox

class Pila:
    #Implementacion de una clase pila con una lista enlazada.

    def __init__(self):
        self.prim = None
        self.len = 0
    
    def push(self, item: Any) -> None:
        #agrega un elemento al tope de la lista.
        nuevo_nodo = Nodo(item, self.prim)
        self.prim = nuevo_nodo
        self.len += 1
    
    def pop(self) -> Any:
        #Desapila el nodo superior(tope) de la pila y lo devuelve.
        #si esta vacia, devuelve mensaje de error
        
        if self.isEmpty():
            print("La pila esta vacia")
            return None
        
        dato = self.prim.dato
        self.prim = self.prim.prox
        self.len -= 1
        return dato

    def isEmpty(self) -> bool:
        #devuelve true si la pila está vacia, caso contrario false.
        return self.prim is None

    def __len__(self) -> int:
      return self.len

    def __str__(self) -> str:
      elementos = []
      actual = self.prim
      while actual is not None:
        elementos.append(str(actual.dato))
        actual = actual.prox
      return "->".join(elementos)



pila = Pila()

print("¿La pila está vacía?")  
print(pila.isEmpty())

pila.push(10)
pila.push(20)
pila.push(30)

print("Pila después de apilar 10, 20, 30:")
print(pila)  # 30 -> 20 -> 10

print("Elemento desapilado:", pila.pop())  # 30

print("Pila después de desapilar:")
print(pila)  # 20 -> 10

print("¿La pila está vacía?", pila.isEmpty())  # False

print("Número de elementos en la pila:", len(pila))  # 2

