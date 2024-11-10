# Ejercicio 7
# Dado un Stack (usando colas y nodos) de números, reordenarlos para que estén abajo los impares y
# arriba los pares, pero que entre números del mismo tipo preserven el orden.
# Ayuda: utilizar dos Stacks auxiliares de números pares e impares
# respectivamente.
# Ejemplo:

# 4      4
# 3  =>  2
# 2      3
# 1      1

from typing import Any

class Nodo:
  def __init__(self, dato: Any = None, next=None):
    self.dato = dato
    self.next = next

class Stack:
  def __init__(self):
    self.top = None

  def push(self, dato: Any) -> None:
    nuevo_nodo = Nodo(dato)
    if self.top is None:
      self.top = nuevo_nodo
    else:
      nuevo_nodo.next = self.top
      self.top = nuevo_nodo

  def pop(self) -> Any:
    if self.isEmpty():
      print("El stack está vacío.")
      return None
    valor = self.top.dato
    self.top = self.top.next
    return valor

  def isEmpty(self) -> bool:
    return self.top is None

  def __str__(self) -> str:
    elementos = []
    actual = self.top
    while actual:
      elementos.append(str(actual.dato))
      actual = actual.next
    return " <- ".join(elementos)

def reordenar_stack(stack: Stack) -> None:
  stack_par = Stack()
  stack_impar = Stack()

  while not stack.isEmpty():
    dato = stack.pop()
    if dato % 2 == 0:
      stack_par.push(dato)
    else:
      stack_impar.push(dato)

  while not stack_impar.isEmpty():
    stack.push(stack_impar.pop())

  while not stack_par.isEmpty():
    stack.push(stack_par.pop())




# Ejemplo de uso:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Stack original:")
print(stack)

# Reordenar el stack
reordenar_stack(stack)

print("\nStack reordenado:")
print(stack)
