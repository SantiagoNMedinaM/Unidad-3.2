from ClasePersonal import Personal
class Investigador(Personal):
    __areaInv: str
    __tipoInv: str
    def __init__(self,apellido,nombre,cuil, sueldoBasico, antig,carrera='',cargo='',catedra='',areaInv='',tipoInv=''):
        super().__init__(apellido,nombre,cuil,sueldoBasico,antig,carrera,cargo,catedra,areaInv,tipoInv)
        self.__areaInv = areaInv
        self.__tipoInv = tipoInv
    def getAreaInvestigacion(self):
        return self.__areaInv
    def getTipoInvestigacion(self):
        return self.__tipoInv
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                cuil = self.getCUIL(),
                sueldobase = self.getSueldoBase(),
                antiguedad = self.getAntiguedad(),
                areaInv = self.__areaInv,
                tipoInv = self.__tipoInv
            )
        )
        return d
    def calculoSueldo(self):
        sueldo = self.getSueldoBase() + (self.getSueldoBase()*(self.getAntiguedad() / 100))
        return sueldo
    def __str__(self) -> str:
        return super().__str__() + ' ' + self.__areaInv + ' ' + self.__tipoInv
    def __gt__(self, otro):
        return super().__gt__(otro)