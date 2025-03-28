# necesario para que Python trate el directorio muebleria como un paquete
# Importamos las clases de muebles.py para facilitar su acceso desde otros módulos
from .muebles import Silla, Mesa, Armario

# Se definen los elementos que se exportan al hacer `from muebleria import *`
__all__ = ["Silla", "Mesa", "Armario"]
