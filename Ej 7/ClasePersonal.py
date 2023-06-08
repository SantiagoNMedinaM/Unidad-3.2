from abc import ABC
import abc
class Personal:
    __cuil: str
    __apellido: str
    __nombre: str
    __sueldoBase: float
    __antig: int

    def __init__(self,nombre,apellido,cuil,sueldoBasico,antig,carrera,cargo,catedra,areaInv,tipoInv):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBase = sueldoBasico
        self.__antig = antig
    def getCUIL(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getSueldoBase(self):
        return self.__sueldoBase
    def getAntiguedad(self):
        return self.__antig
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.__nombre,
                apellido = self.__apellido,
                cuil = self.__cuil,
                sueldobase = self.__sueldoBase,
                antiguedad = self.__antig
            )
        )
        return d
    @abc.abstractmethod
    def calculoSueldo():
        pass
    def __str__(self) -> str:
        return str(self.__cuil) + ' ' + self.__nombre + ' ' + self.__apellido + ' ' + str(self.__sueldoBase) + ' ' + str(self.__antig)
    def __gt__(self,otro):
        return self.getApellido() > otro.getApellido()