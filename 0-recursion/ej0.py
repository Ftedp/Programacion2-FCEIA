def factorial(n: int) -> int:
    """ Precondicion: n entero >= 0
    Devuelve: n!
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)
