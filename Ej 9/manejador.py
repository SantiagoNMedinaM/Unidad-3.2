from zope.interface import implementer
from clasevehiculonuevo import VehiculoNuevo
from clasevehiculousado import VehiculoUsado
from interface import IVehiculo
from claselista import Lista
from claseObjectEncoder import ObjectEncoder

@implementer(IVehiculo)
class Manejador:
    __lista=Lista()

    def __init__(self):
        self.__lista=Lista()

    def insertarelemento(self, vehiculo, posicion):
        self.__lista.agregarVehiculoIndice(vehiculo,posicion)

    def agregarelemento(self, vehiculo):
        self.__lista.agregarVehiculoFinal(vehiculo)

    def mostrarelemento(self, posicion):
        print('{}'.format(self.__lista.mostrarVehiculoIndice(posicion)))

    def mostrartipo(self,posicion):
        self.__lista.getTipo(posicion)  

    def buscarpatente(self,patente):
        band=self.__lista.buscarpatente(patente)
        return band    
    
    def modificarpreciobase(self,patente,nuevoprecio):
        self.__lista.modificarpreciobase(patente,nuevoprecio)

    def mostrarprecioventa(self,patente):
        return(self.__lista.mostrarprecioventa(patente))     
    
    def buscareconomico(self):
        self.__lista.buscareconomico()

    def toJSON(self):
        json=ObjectEncoder()
        d=self.__lista.toJSON()
        json.guardarJSONArchivo(d,'vehiculos2.json')   

    def getObjeto(self,posicion):
        return self.__lista.getObjeto(posicion)   
    def obtenerultimo(self):
        return self.__lista.obtenerultimo()  

    def cargarlista(self):
        json=ObjectEncoder()   
        diccionario=json.leerJSONArchivo('vehiculos.json')
        vehiculos=json.decodificarDiccionario(diccionario)
        for vehiculo in vehiculos:
            tipo=str(vehiculo["tipo"])
            modelo=str(vehiculo["modelo"])
            cantpuertas=int(vehiculo["cantpuertas"])
            color=str(vehiculo["color"])
            preciobase=float(vehiculo["preciobase"])
            marca=str(vehiculo["marca"])

            if tipo=='nuevo':
                version=str(vehiculo["version"])
                unvehiculo=VehiculoNuevo(modelo,cantpuertas,color,preciobase,marca,version)
                self.agregarelemento(unvehiculo)

            elif tipo=='usado':
                patente=str(vehiculo["patente"])
                año=int(vehiculo["año"])
                kilometraje=int(vehiculo["kilometraje"])  
                unvehiculo=VehiculoUsado(modelo,cantpuertas,color,preciobase,marca,patente,año,kilometraje)      
                self.agregarelemento(unvehiculo)

    def mostrarlista(self):
        self.__lista.mostrartodos()    
            
        
            