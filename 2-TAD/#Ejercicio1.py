# Complete la implementación del TAD Lista utilizando nodos enlazados.
#Falta implementar los métodos index, append, __len__ y __str__.
#Escriba código de prueba hasta convencerse de que esta clase funciona de manera análoga a las listas de Python.
from typing import Any

class Nodo:
  def __init__(self, dato: Any = None, prox=None):
        self.dato = dato
        self.prox = prox

  def __str__(self):
        return str(self.dato)


def ver_lista(nodo: Nodo | None) -> None:
    """Recorre todos los nodos a través de sus enlaces, mostrando sus
    contenidos.
    """
    if nodo is None:
        print("Lista vacía")
        return

    while nodo is not None:
        print(nodo)
        nodo = nodo.prox

class ListaEnlazada:
    """Modela una lista enlazada."""

    def __init__(self) -> None:
        """Crea una lista enlazada vacía."""
        # Referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # Cantidad de elementos de la lista
        self.len = 0

    def insert(self, i: int, x: Any) -> None:
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, imprime un error y retorna inmediatamente.
        """
        if i < 0 or i > self.len:
            print("Posición inválida")
            return
        nuevo = Nodo(x) #inicializo nodo con valor x
        if i == 0:
            # Caso particular : insertar al principio
            nuevo.prox = self.prim      #puntero del nodo nuevo apunta al actual primer nodo de la lista
            self.prim = nuevo           #se referencia (apunta) al nodo nuevo como primer nodo de la lista
        else:
            # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim           # se crea variable con primer nodo
            for pos in range(1, i):
                n_ant = n_ant.prox      # se recorre la lista enlazada
            # Intercalar el nuevo nodo
            nuevo.prox = n_ant.prox     # puntero del nuevo nodo apunta a donde apunta el nodo actual.
            n_ant.prox = nuevo          # nodo actual apunta a el nuevo nodo
        self.len += 1

    #Ejercicio 2:  Agregue a ListaEnlazada un método extend que reciba una ListaEnlazada y
    #agregue a la lista actual los elementos que se encuentran en la lista recibida.
    #¿Puede estimar la complejidad de este método?
     
    def extend(self, other: 'ListaEnlazada') -> None:
        """Agrega los elementos de la lista other a la lista actual."""
        if other.prim is None:
            return
        if self.prim is None:
            self.prim = other.prim
            self.len = other.len
        else:
            n_act = self.prim
            while n_act.prom is not None:
                n_act = n_act.prox
            n_act.prox = other.prim
            self.len += other.len
        return None

    def pop(self, i: int | None = None) -> Any:
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se muestra un mensaje de error y se
        retorna inmediatamente. Si no se recibe la posición, devuelve el
        último elemento.
        """
        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            print(" Posición inválida ")
            return
        if i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato       #creo variable con el dato
            self.prim = self.prim.prox      #referencio como primer nodo de la lista al actual segundo.
        else:
            # Buscar los nodos en las posiciones (i -1) e (i)
            n_ant = self.prim #apunto al primer nodo de la lista
            n_act = n_ant.prox #y al proximo nodo
            for pos in range(1, i):
                n_ant = n_act #actualizo nodo actual a nodo anterior
                n_act = n_ant.prox #y nodo el proximo al actual
            # Guardar el dato y descartar el nodo
            dato = n_act.dato
            n_ant.prox = n_act.prox
        self.len -= 1
        return dato

    def remove(self, x: Any) -> None:
        """Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, imprime un mensaje de error y retorna
        inmediatamente.
        """
        if self.len == 0:
            print("La lista esta vacía")
            return
        if self.prim.dato == x:
            # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
            # Buscar el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim #inicializa con el primer nodo de la lista
            n_act = n_ant.prox #inicializa con el nodo siguiente
            while n_act is not None and n_act.dato != x:
                n_ant = n_act                   # se mueve al nodo actual pero sigue siendo anterior ya que
                n_act = n_ant.prox              # el n_act se actualiza al prox del actual, dejandolo en ant nuevamente
            if n_act is None:
                print("El valor no está en la lista.")
                return
            # Descartar el nodo
            n_ant.prox = n_act.prox
        self.len -= 1

    def __len__(self):
        return self.len
      
    def __str__(self):
        elementos = []
        n_act = self.prim
        while n_act is not None:
            elementos.append(str(n_act.dato))
            n_act = n_act.prox
        return "[" + ", ".join(elementos) + "]"

    def append(self, x: Any) -> None:
        """Agrega un nuevo elemento a la lista"""
        nuevo = Nodo(x)
        if self.prim is None:
            self.prim = nuevo
        else: 
            n_act = self.prim
            while n_act.prox is not None:
                n_act = n_act.prox
            n_act.prox = nuevo
        self.len += 1

    def index(self, x: Any) -> int:
        """Devuele el indice de la primera aparición de x en la lista""" 
        n_act = self.prim
        idx = 0
        while n_act is not None:
            if n_act.dato == x:
                return idx
            n_act = n_act.prox
            idx += 1
        raise ValueError(f"{x} no está en la lista.")

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)
nodo7 = Nodo(7)
nodo8 = Nodo(8)
nodo9 = Nodo(9)
nodo10 = Nodo(10)

nodo1.prox = nodo2
nodo2.prox = nodo3
nodo3.prox = nodo4
nodo4.prox = nodo5
nodo5.prox = nodo6
nodo6.prox = nodo7
nodo7.prox = nodo8
nodo8.prox = nodo9
nodo9.prox = nodo10


ver_lista(nodo1)