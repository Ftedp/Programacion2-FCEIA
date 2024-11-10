from typing import Any

class Nodo:
    def __init__(self, dato: Any = None, next=None):
        self.dato = dato
        self.next = next

class Queue:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.len = 0

    def enqueue(self, item: Any) -> None:
      # Agrega un elemento al final de la cola.
      
        nuevo_nodo = Nodo(item)
        if self.isEmpty():
            self.inicio = self.final = nuevo_nodo # Si la cola está vacía, el nuevo nodo es el primero y el último
        else:
            self.final.next = nuevo_nodo   # Enlazamos el nodo al final
            self.final = nuevo_nodo   # Actualizamos el puntero 'final'
        self.len += 1

    def dequeue(self) -> Any:
        # elimina y devuelve el primer elemento de la cola

        if self.isEmpty():
            print("La cola esta vacía")
            return None

        valor = self.inicio.dato
        self.inicio = self.inicio.next
        if self.inicio is None:
            self.final = None
        self.len -= 1
        return valor
    
    def isEmpty(self) -> None:
        # Devuelve True si la cola está vacía, caso contrario False.
        return self.inicio is None
    
    def front(self) -> Any:
        #Devuelve el primer elemento de la cola sin eliminarlo

        if self.isEmpty():
            print("La cola está vacía")
            return None
        
        return self.inicio.dato
    
    def __len__(self) -> int:
        return self.len
    
    def __str__(self) -> str:
        # Representación en forma de cadena de la cola
        elementos = []
        actual = self.inicio
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.next
        return " <- ".join(elementos)
    

    # Pruebas para la clase Queue con lista enlazada
cola = Queue()

# Encolar elementos
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print("Cola después de encolar 1, 2, 3:", cola)

# Ver el frente de la cola
print("Frente de la cola:", cola.front())

# Desencolar un elemento
print("Elemento desencolado:", cola.dequeue())

# Ver la cola después de desencolar
print("Cola después de desencolar:", cola)

# Verificar si la cola está vacía
print("¿Está la cola vacía?", cola.isEmpty())

# Verificar el tamaño de la cola
print("Tamaño de la cola:", len(cola))