#Ejercicio1

# Complete la implementación del TAD Lista utilizando nodos enlazados.
#Falta implementar los métodos index, append, __len__ y __str__.
#Escriba código de prueba hasta convencerse de que esta clase funciona de manera análoga a las listas de Python.from typing import Any
from typing import Any

class _Nodo:
    def __init__(self, dato: Any = None, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)


def ver_lista(nodo: _Nodo | None) -> None:
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
        nuevo = _Nodo(x)
        if i == 0:
            # Caso particular : insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox
            # Intercalar el nuevo nodo
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.len += 1

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
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i -1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
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
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox
            if n_act is None:
                print("El valor no está en la lista.")
                return
            # Descartar el nodo
            n_ant.prox = n_act.prox
        self.len -= 1

    def __len__(self):
        """Devuelve el largo de la lista enlazada"""
        return self.len

    def __str__(self) -> str:
        """Imprime la lista enlazada"""
        elementos = []
        n_act = self.prim
        while n_act is not None:
            elementos.append(str(n_act.dato))
            n_act = n_act.prox
        return "[" + ", ".join(elementos) + "]"

    def append(self, x: Any) -> None:
        """Agrega un nuevo elemento a la lista"""
        nuevo = _Nodo(x)
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