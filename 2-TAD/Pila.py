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

    def ver(self) -> Any:
      if self.isEmpty():
        print("La pila esta vacia")
        return None
      return self.prim.dato 

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


#Ejercicio 3
#Crear una clase PilaConMaximo que soporte las operaciones de Pila
#(push(item) y pop()), y además incluya el método obtener_maximo() que
#devuelva el elemento máximo de la pila sin sacarlo de la misma y que funcione en
#tiempo constante.
#Ayuda: usar dos pilas, una para guardar los elementos y otra para guardar
#los máximos.
class PilaConMaximo:
  def __init__(self):
        self.pila = Pila()          # Pila principal para los elementos.
        self.pila_maximos = Pila()   # Pila para almacenar los máximos.

  def push(self, item: Any) -> None:
    #agrega un elemento al tope de la pila

    self.pila.push(item)
    if self.pila_maximos.isEmpty() or item >= self.pila_maximos.prim.dato:
      self.pila_maximos.push(item)

  def pop(self) -> Any:
    #Desapila el nodo superior(tope) de la pila y lo devuelve.
    #si esta vacia, devuelve mensaje de error

    if self.pila.isEmpty():
      print("La pila esta vacia")
      return None

    dato = self.pila.pop()
    
    if dato == self.pila_maximos.ver(): 
      self.pila_maximos.pop()

    return dato
    
  def obtener_maximo(self) -> Any:
    if self.pila_maximos.isEmpty():
      print("La pila esta vacia")
      return None
    return self.pila_maximos.ver()
      

# Crear una instancia de la PilaConMaximo
pila = PilaConMaximo()

# Agregar algunos elementos y verificar el máximo
pila.push(3)
print("Máximo actual:", pila.obtener_maximo())  # Máximo debería ser 3

pila.push(5)
print("Máximo actual:", pila.obtener_maximo())  # Máximo debería ser 5

pila.push(2)
print("Máximo actual:", pila.obtener_maximo())  # Máximo debería seguir siendo 5

pila.push(7)
print("Máximo actual:", pila.obtener_maximo())  # Máximo debería ser 7

pila.push(1)
print("Máximo actual:", pila.obtener_maximo())  # Máximo debería seguir siendo 7

# Eliminar elementos y verificar el máximo en cada paso
pila.pop()
print("Máximo actual después de pop:", pila.obtener_maximo())  # Máximo debería seguir siendo 7

pila.pop()
print("Máximo actual después de pop:", pila.obtener_maximo())  # Máximo debería ser 5

pila.pop()
print("Máximo actual después de pop:", pila.obtener_maximo())  # Máximo debería seguir siendo 5

pila.pop()
print("Máximo actual después de pop:", pila.obtener_maximo())  # Máximo debería ser 3

pila.pop()
print("Máximo actual después de pop:", pila.obtener_maximo())  # La pila está vacía, debería mostrar un mensaje de vacío




