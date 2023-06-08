from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseApoyo import Apoyo
from ClaseNodo import Nodo
from zope.interface import Interface, implementer
from ClaseInterface import IElemento
from ClaseException import Error
@implementer(IElemento)
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __tope: int
    __indice: int
    def __init__(self):
        self.__comienzo = None
        self.__indice = 0
        self.__actual = None
        self.__tope = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    def insertarElemento(self,obj,pos):
        nuevo = Nodo(obj)
        cont = 0
        if pos < 0 or pos > self.__tope:
            raise Error("La posicion no es valida")
        else:
            if self.__comienzo == None:
                nuevo.setSiguiente(self.__comienzo)
                self.__comienzo = nuevo
                self.__actual = nuevo
                self.__tope += 1
            elif cont + 1 == pos:
                nuevo.setSiguiente(self.__comienzo)
                self.__comienzo = nuevo
                self.__actual = nuevo
                self.__tope += 1
            else:
                aux = self.__comienzo
                ant = self.__comienzo
                while aux != None and cont < pos:
                    ant = aux
                    aux = aux.getSiguiente()
                    cont += 1
                ant.setSiguiente(nuevo)
                nuevo.setSiguiente(aux)
                self.__tope += 1
    def agregarElemento(self,o):
        nuevo = Nodo(o)
        aux = self.__comienzo
        if aux == None:
            nuevo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo
            self.__actual = nuevo
            self.__tope += 1
        else:
            i = 0
            while aux != None and i < self.__tope:
                ant = aux
                aux = aux.getSiguiente()
                i += 1
            if ant != None:
                ant.setSiguiente(nuevo)
                nuevo.setSiguiente(aux)
                self.__tope += 1 
    def mostrarElemento(self,pos):
        c = 0
        aux = self.__comienzo
        if pos < 0 and pos > self.__tope:
            raise Error("La posicion no es valida")
        else:
            while c != pos and aux != None:
                aux = aux.getSiguiente()
                c += 1
            if pos == c:
                print (aux.getDato())
            else:
                print("Esa posicion no se encuentra dentro de la lista")
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            comienzo = [dato.toJSON() for dato in self]
        )
        return d
    def listarCarrera(self,carrera):
        aux = self.__comienzo
        listado = []
        while aux != None:
            if isinstance(aux.getDato(), DocenteInvestigador):
                if carrera == aux.getDato().getCarrera():
                    personal = aux.getDato()
                    listado.append(personal)
            aux = aux.getSiguiente()
        listado.sort()
        for datos in listado:
            print(datos)
    def mostrarLista(self):
        aux = self.__comienzo
        while aux != None:
            print (aux.getDato())
            aux = aux.getSiguiente
    def contarPorArea(self,area):
        aux = self.__comienzo
        c = 0
        c1 = 0
        while aux != None:
            if isinstance(aux.getDato(), DocenteInvestigador):
                if aux.getDato().getAreaInvestigacion() == area:
                    c += 1
            if isinstance(aux.getDato(),Investigador):
                if aux.getDato().getAreaInvestigacion() == area:
                    c1 += 1
            aux = aux.getSiguiente()
        print("La cantidad de docentes investigadores en el area {} son: {}".format(area,c))
        print("La cantidad de investigadores del area {} son: {}".format(area,c1))
    def listado(self):
        nodo = self.__comienzo
        listado = []
        while nodo != None:
            personal = nodo
            listado.append(personal)
            nodo = nodo.getSiguiente()
        listado.sort()
        for dato in listado:
            print("Nombre: {} Apellido: {} Agente: {} Sueldo: {}".format(dato.getDato().getNombre(),dato.getDato().getApellido(),dato.getTipo(),dato.getDato().calculoSueldo()))
    def listarCat(self,cat):
        sum = 0
        aux = self.__comienzo
        while aux != None:
            if isinstance(aux.getDato(),DocenteInvestigador):
                if aux.getDato().getCategoria() == cat:
                    print ("Apellido: {} Nombre: {} Importe extra: {}".format(aux.getDato().getApellido(),aux.getDato().getNombre(),aux.getDato().getImporteExtra()))
                    sum += aux.getDato().getImporteExtra()
            aux = aux.getSiguiente()
        print ("El total de dinero para los importes extra que se le debe solicitar a la Secretaria es de : {}$".format(sum))
