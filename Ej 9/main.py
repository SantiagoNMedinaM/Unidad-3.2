from menu import Menu
from claselista import Lista
from clasevehiculonuevo import VehiculoNuevo
from clasevehiculousado import VehiculoUsado
import unittest

class TestVehiculos(unittest.TestCase):
    def testInsertar(self):
        m=Lista()
        self.__vehiculo1=VehiculoNuevo('Yaris',4,'blanco',13000,'Ford','full')
        self.__vehiculo2=VehiculoNuevo('Corolla',4,'negro',14000,'Ford','full')
        m.agregarVehiculoIndice(self.__vehiculo1,1)
        self.assertEqual(self.__vehiculo1,m.getObjeto(1))  
        m.agregarVehiculoIndice(self.__vehiculo2,2)
        self.assertEqual(self.__vehiculo2,m.getObjeto(2)) 
        self.__vehiculo3=VehiculoNuevo('Hilux',4,'rosado',15000,'Ford','base')
        m.agregarVehiculoFinal(self.__vehiculo3)
        self.assertEqual(self.__vehiculo3,m.obtenerultimo())
    def testVerificar(self):
        m=Lista()
        self.__vehiculo1=VehiculoNuevo('Yaris',4,'blanco',13000,'Ford','full')
        self.__vehiculo2=VehiculoNuevo('Corolla',4,'negro',14000,'Ford','full')
        m.agregarVehiculoFinal(self.__vehiculo1)
        m.agregarVehiculoFinal(self.__vehiculo2)
        self.assertEqual(self.__vehiculo1,m.getObjeto(1))
        self.assertEqual(self.__vehiculo2,m.getObjeto(2))
    def testModifcarPrecioVenta(self):
        m=Lista()
        self.__vehiculo1=VehiculoUsado('Yaris',4,'blanco',13000,'Toyota','ABC123',2010,50000)
        m.agregarVehiculoFinal(self.__vehiculo1)
        patente=self.__vehiculo1.getPatente()
        precio=m.getPrecioXPatente(patente)
        self.assertEqual(self.__vehiculo1.mostrarprecioventa(),precio)




if __name__=='__main__':
    #menu=Menu()
    #m=M()
    #m.cargarlista()
    unittest.main()
    #menu.opciones(m)