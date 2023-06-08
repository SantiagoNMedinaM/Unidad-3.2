from clasevehiculo import Vehiculo
from clasevehiculonuevo import VehiculoNuevo
from clasevehiculousado import VehiculoUsado
class Nodo:
    __vehiculo:Vehiculo
    __siguiente:object

    def __init__(self,vehiculo):
        self.__vehiculo=vehiculo
        self.__siguiente=None
    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__vehiculo 
    def getTipo(self):
        if isinstance(self.__vehiculo,VehiculoUsado):
            print('El auto con posicion ingresada es usado \n')
        elif isinstance(self.__vehiculo,VehiculoNuevo):
            print('El auto con posicion ingresada es nuevo \n')   
    def getPatente(self):
        if isinstance(self.__vehiculo,VehiculoUsado):
            return(self.__vehiculo.getPatente())
        else:
            return False        
    
    def modificarpreciobase(self,precionuevo):
        if isinstance(self.__vehiculo,VehiculoUsado):
            self.__vehiculo.modificarpreciobase(precionuevo)

    def mostrarprecioventa(self):
        return self.__vehiculo.mostrarprecioventa()  

    def toJSON(self):
        if isinstance(self.__vehiculo,VehiculoUsado):
            d=dict(tipo='usado',modelo=self.__vehiculo.getModelo(),cantpuertas=self.__vehiculo.getCantpuertas(),color=self.__vehiculo.getColor(),preciobase=self.__vehiculo.getPreciobase(),marca=self.__vehiculo.getMarca(),patente=self.__vehiculo.getPatente(),anio=self.__vehiculo.getAño(),kilometraje=self.__vehiculo.getKilometraje())  
        elif isinstance(self.__vehiculo,VehiculoNuevo):
            d=dict(tipo='nuevo',modelo=self.__vehiculo.getModelo(),cantpuertas=self.__vehiculo.getCantpuertas(),color=self.__vehiculo.getColor(),preciobase=self.__vehiculo.getPreciobase(),marca=self.__vehiculo.getMarca(),version=self.__vehiculo.getVersion())   
        return d         

