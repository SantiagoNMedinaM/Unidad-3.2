from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseApoyo import Apoyo
class Nodo:
    __personal: object
    __siguiente: object
    def __init__(self,personal):
        if isinstance(personal,Personal):
            self.__personal = personal
        self.__siguiente = None
    def getDato(self):
        return self.__personal
    def setSiguiente(self,personal):
        self.__siguiente = personal
    def getSiguiente(self):
        return self.__siguiente
    def getTipo(self):
        tipo = None
        if isinstance(self.__personal, DocenteInvestigador):
            tipo = "Docente Investigador"
        elif isinstance (self.__personal, Investigador):
            tipo = "Investigador"
        elif isinstance (self.__personal,Docente):
            tipo = "Docente"
        elif isinstance (self.__personal, Apoyo):
            tipo = "Personal de Apoyo"
        return tipo
    def __gt__(self, otro):
        return self.__personal.__gt__(otro.getDato())
    
        