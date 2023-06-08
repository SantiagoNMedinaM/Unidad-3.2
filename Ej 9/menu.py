from clasevehiculonuevo import VehiculoNuevo
from clasevehiculousado import VehiculoUsado
class Menu:
    __opcion=0

    def __init__(self):
        self.__opcion==0

    def opciones(self,m):
        while self.__opcion!=8:
            print('1--Insertar vehiculo por indice\n2--Agregar vehiculo al final\n3--Mostrar tipo de vehiculo por indice\n4--Modificar precio base por patente\n5--Mostrar todos los datos y vehiculo mas economico\n6--Mostrar modelo, cantidad de peurtas e importe de cada vehiculo\n7--Almacenar objetos en el JSON\n8--SALIR DEL SISTEMA\n')
            self.__opcion=int(input('Ingrese una opcion '))
            if self.__opcion==1:
                tipo=str(input('Ingrese tipo de vehiculo a ingresar(usado o nuevo ) '))
                modelo=str(input('Ingrese modelo '))
                cantpuertas=int(input('Ingrese cantidad de puertas '))
                color=str(input('Ingrese color '))
                preciobase=int(input('Ingrese precio base '))
                marca=str(input('Ingrese marca '))
                if tipo =='nuevo':
                    version=str(input('Ingrese version(base o full) '))
                    unvehiculo=VehiculoNuevo(modelo,cantpuertas,color,preciobase,marca,version)
                elif tipo=='usado':
                     patente=str(input('Ingrese patente '))
                     año=int(input('Ingrese año ')) 
                     kilometraje=int(input('Ingrese kilometraje '))
                     unvehiculo=VehiculoUsado(modelo,cantpuertas,color,preciobase,marca,patente,año,kilometraje) 
                posicion=int(input('Ingrese posicion a insertar el vehiculo '))
                m.insertarelemento(unvehiculo,posicion)
                print('Vehiculo insertado')
                print('\n')

            elif self.__opcion==2:
                tipo=str(input('Ingrese tipo de vehiculo a ingresar(usado o nuevo ) '))
                modelo=str(input('Ingrese modelo '))
                cantpuertas=int(input('Ingrese cantidad de puertas '))
                color=str(input('Ingrese color '))
                preciobase=int(input('Ingrese precio base '))
                marca=str(input('Ingrese marca '))
                if tipo =='nuevo':
                    version=str(input('Ingrese version(base o full) '))
                    unvehiculo=VehiculoNuevo(modelo,cantpuertas,color,preciobase,marca,version)
                elif tipo=='usado':
                     patente=str(input('Ingrese patente '))
                     año=int(input('Ingrese año ')) 
                     kilometraje=int(input('Ingrese kilometraje '))
                     unvehiculo=VehiculoUsado(modelo,cantpuertas,color,preciobase,marca,patente,año,kilometraje)
                m.agregarelemento(unvehiculo)
                print('Vehiculo agregado')
                print('\n')

            elif self.__opcion==3:
                posicion=int(input('Ingrese posicion a para saber tipo del vehiculo '))
                m.mostrartipo(posicion)
                print('\n')

            elif self.__opcion==4:
                patente=str(input('Ingrese patente a modificar el precio base '))
                band=m.buscarpatente(patente)
                if band==True:
                    nuevoprecio=int(input('Ingrese nuevo precio base '))
                    m.modificarpreciobase(patente,nuevoprecio)
                    print('{}'.format(m.mostrarprecioventa(patente)))
                else:
                    print('Patente ingresada no encontrada ')    
                print('\n')

            elif self.__opcion==5:
                print('Vehiculo mas economico')
                m.buscareconomico()
                print('\n')
            elif self.__opcion==6:
                print('LISTA:')
                m.mostrarlista()
                print('\n')
            elif self.__opcion==7:
                m.toJSON()
                print('Archivo cargado con exito ')
                print('\n')
            elif self.__opcion==8:
                print('HA SALIDO DEL SISTEMA ')
            else:
                print('Opcion ingresada incorrecta ')
        
               