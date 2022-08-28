class Celda:
    __sig = None
    __item = None

    def __init__(self, item = None):
        self.__sig = None
        self.__item = item

    def setItem(self, item):
        self.__item = item
    
    def setSig(self, celda):
        self.__sig = celda

    def getItem(self):
        return self.__item
    
    def getSig(self):
        return self.__sig

class Pila:
    __cant = None
    __tope = None

    def __init__(self, cant = 0):
        self.__cant = cant
        self.__tope = None

    def Vacio(self):
        return self.__cant == 0

    def Mostrar (self):
        if not (self.Vacio()):
            i = self.__cant-1
            tope = self.__tope
            while (i >= 0):
                print(tope.getItem())
                tope = tope.getSig()
                i -= 1

    def Insertar(self, x):
        unaCelda = Celda()
        unaCelda.setItem(x)
        unaCelda.setSig(self.__tope)
        self.__tope = unaCelda
        self.__cant += 1
        return unaCelda.getItem()

    def Suprimir(self):
        if (self.Vacio()):
            print("\nla Pila esta vacia")
            return 0
        else:
            aux = self.__tope
            x = self.__tope.getItem()
            self.__tope = self.__tope.getSig()
            self.__cant -= 1
            del aux
            return x