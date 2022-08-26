class Pila:
    __tope = 0
    __cant = 0
    __item = None

    def __init__(self, cant = 0):
        self.__tope = -1
        self.__cant = cant
        self.__item = []

    def vacio(self):
        return (self.__tope == 0)

    def llena(self):
        return self.__tope == self.__cant

    def insertar(self, x):
        if (self.__tope < self.__cant):
            self.__cant += 1
            self.__tope += 1
            self.__item.append(x)
            return x
        else: return 0

    def suprimir (self):
        if (self.vacio()):
            print("\nLa pila esta vacia")
            return 0
        else:
            self.__tope -= 1
            x = self.__item.pop(self.__tope)
            return x

    def mostrar (self):
        if not (self.vacio()):
            i = self.__tope
            while (i >= 0):
                print(self.__item[i])
                i -= 1