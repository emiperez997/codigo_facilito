# Anotaciones de tipo
# Aunque no es obligatorio, es una buena practica
# a: str = 'Hola'
# b: int = 10
# c: float = 10.5
# d: bool = True

# print(a)
# print(b)
# print(c)
# print(d)

# def suma(numero1: int, numero2: int) -> int:
#     return numero1 + numero2

# valor1: int = 10
# valor2: int = 20
# valor3: int

# resultado: int = suma(valor1, valor2)

# print(resultado)

# class User():
    
#     def __init__(self, username: str, password: str) -> None:
#         self.username = username
#         self.password = password

#     def saluda(self) -> str:
#         return f'Hola, {self.username}'


# cody = User('Cody', '1234')

# print(cody.saluda())

from typing import List
from typing import Tuple

calificaciones: List[int] = [10, 9, 10, 8, 9, 10, 10]

def promedio(calificaciones: List[int]) -> float:
    return sum(calificaciones) / len(calificaciones)

print(promedio(calificaciones))

configuraciones: Tuple[str] = ("http://localhost", "8080", "root")