class Vehiculo:
    __modelo=str
    __cantpuertas=int
    __color=str
    __preciobase=float

    def __init__(self,modelo,cantpuertas,color,preciobase,marca):
        self.__modelo=modelo
        self.__cantpuertas=cantpuertas
        self.__color=color
        self.__preciobase=preciobase
        self.__marca=marca

    def getModelo(self):
        return self.__modelo
    def getCantpuertas(self):
        return self.__cantpuertas
    def getColor(self):
        return self.__color
    def getPreciobase(self):
        return self.__preciobase
    def getMarca(self):
        return self.__marca    


    def __str__(self):
        return '{} {} {} {}'.format(self.__modelo,self.__cantpuertas,self.__color,self.__preciobase)
    