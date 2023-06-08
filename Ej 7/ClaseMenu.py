from ClaseObjectEncoder import ObectEncoder
from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseApoyo import Apoyo
class Menu:
    __opcion: int
    def __init__(self) -> None:
        self.__opcion = 0
    def nuevoEmpleado(self):
            tipo = str(input("Ingrese el tipo de agente que desdea ingresar: Docente, Investigador, Personal de Apoyo o Docente investigador: "))
            cuil = str(input("Ingrese el CUIL: "))
            ape = str(input("Ingrese el apellido: "))
            nomb = str(input("Ingrese el nombre: "))
            sb = float(input("Ingrese el sueldo basico: "))
            ant = int(input("Ingrese la antiguedad: "))
            if tipo == "Docente" or "docente":
                    carr = str(input("Ingrese la carrera: "))
                    carg = str(input("Ingrese el cargo: "))
                    cate = str(input("Ingrese la catedra: "))
                    unP = Docente(ape,nomb,cuil,sb,ant,carr,carg,cate)
            elif tipo == "Investigador" or "investigador":
                    areaInv = str(input("Ingrese el area de investigacion: "))
                    tipoInv = str(input("Ingrese el tipo de investigacion: "))
                    unP = Docente(ape,nomb,cuil,sb,ant, areaInv, tipoInv)
            elif tipo == "Personal de Apoyo" or "personal de apoyo" or "Personal de apoyo" or "Personal De Apoyo":
                    categoria = str(input("Ingrese la categorira: : "))
                    unP = Docente(ape,nomb,cuil,sb,ant,categoria)
            elif tipo == "Docente Investigador" or "Docente investigador" or "docente investigador":
                    carr = str(input("Ingrese la carrera: "))
                    carg = str(input("Ingrese el cargo: "))
                    cate = str(input("Ingrese la catedra: "))
                    areaInv = str(input("Ingrese el area de investigacion: "))
                    tipoInv = str(input("Ingrese el tipo de investigacion: "))
                    categ = str(input("Ingrese la categoria de investigacion: "))
                    impex = float(input("Ingrese el importe extra: "))
                    unP = Docente(ape,nomb,cuil,sb,ant,carr,carg,cate,areaInv,tipoInv,categ,impex)
            return unP
    def opciones(self,empleados):
        menuops = "Menu de opciones"
        while self.__opcion != 9:
            print(menuops.center(50,"-"))
            print("1) Ingresar un empleado a la lista")
            print("2) Agregar un empleado a la lista")
            print("3) Mostrar que tipo de empleado hay en cierta posicion")
            print ("4) El nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
            print("5) Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.")
            print("6) Listar empleados")
            print("7) Con una categoria ingresada por teclado listar apellido, nombre e importe extra, y mostrar Total")
            print("8) Guardar cambios en el archivo JSON")
            self.__opcion = int(input("Ingrese una opcion: "))
            if self.__opcion == 1:
                unP = self.nuevoEmpleado()
                indice = int(input("Ingrese la posicion donde desea ingresar al empleado: "))
                empleados.insertarElemento(unP,indice)
            elif self.__opcion == 2:
                  unP = self.nuevoEmpleado()
                  empleados.agregarElemento(unP)
            elif self.__opcion == 3:
                  indice = int(input("Ingrese la posicion que desea que se muestre: "))
                  empleados.mostrarElemento(indice)
            elif self.__opcion == 4:
                carrera = str(input("Ingrese el nombre de la carrera: "))
                empleados.listarCarrera(carrera)
            elif self.__opcion == 5:
                  area = str(input("Ingrese el area"))
                  empleados.contarPorArea(area)
            elif self.__opcion == 6:
                  empleados.listado()
            elif self.__opcion == 7:
                  cat = str(input("Ingrese la categoria deseada (I, II, III, IV o V)"))
                  empleados.listarCat(cat)
            elif self.__opcion == 8:
                  dicc = empleados.toJSON()
                  jsonF = ObectEncoder()
                  jsonF.guardarJSON(dicc,"personal.json")
            elif self.__opcion == 9:
                  print ("Saliendo del programa...")
            else:
                  print("Opcion invalida, por favor ingrese una opcion valida")
