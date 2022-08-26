from pila import Pila
import math

if __name__ == "__main__":
    unaPila = Pila()
    x = int(input("\nIngrese el numero a cambiar a binario:"))
    elem = x
    while (x >= 1):
        elem = x%2
        x = math.floor(x/2)
        unaPila.insertar(elem)
    unaPila.mostrar()
