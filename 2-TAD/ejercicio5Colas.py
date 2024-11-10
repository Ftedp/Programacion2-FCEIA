# Cola Generalizada.

# Ejercicio 6
# Hace un montón de años había una viejísma sucursal del correo que tenía un
# cartel que decía "No se recibirán más de 5 cartas por persona". O sea que la
# gente entregaba sus cartas (hasta la cantidad permitida) y luego tenía que
# volver a hacer la cola si tenía más cartas para despachar. Modelar una cola de
# correo generalizada, donde en la inicialización se indica la cantidad (no
# necesariamente 5) de cartas que se reciben por persona.

class Cliente():
    def __init__(self, nombre: str, cant_cartas: int = 1) -> None:
        self.nombre = nombre
        self.cant_cartas = cant_cartas

class Nodo():
    def __init__(self, dato: Cliente, prox=None):
        self.dato = dato
        self.prox = prox

class ColaGeneralizada:
    def __init__(self, limite_cartas: int = 5) -> None:
        self.limite_cartas = limite_cartas
        self.frente = None 
        self.final = None

    def push(self, cliente: Cliente) -> None:
        #agregar el cliente a la cola
        nuevo_nodo = Nodo(cliente)
        
        if self.final:
            self.final.prox = nuevo_nodo
        self.final = nuevo_nodo
        if not self.frente:
            self.frente = nuevo_nodo
        
    def remove(self) -> None:
        if self.isEmpty():
            print("La lista está vacía")
            return
    
        cliente = self.frente.dato   # Obtiene el cliente en el frente de la cola
        cartas_despachadas = min(cliente.cant_cartas, self.limite_cartas)   # Máximo cartas a despachar según el límite
        cliente.cant_cartas -= cartas_despachadas
        print(f"Atendido cliente {cliente.nombre}, despachadaas {cartas_despachadas} cartas.")

        if cliente.cant_cartas > 0:
            self.push(cliente)

        self.frente = self.frente.prox #mueve el puntero inicial al siguiente nodo
        if not self.frente:
            self.final = None
        
    def isEmpty(self) -> bool:
        return self.frente is None
    


correo = ColaGeneralizada()
correo.push(Cliente("Ana", 1))
correo.push(Cliente("Facu", 1))
correo.push(Cliente("Seba", 2))
correo.push(Cliente("Joe", 6))
correo.push(Cliente("Pablo", 9))
correo.push(Cliente("Ana", 1))
correo.push(Cliente("Facu", 1))
correo.push(Cliente("Seba", 2))

# Procesa cada cliente en la cola hasta que esté vacía
while not correo.isEmpty():
    correo.remove()