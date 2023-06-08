from ClasePersonal import Personal
class Docente(Personal):
    __carrera: str
    __cargo: str
    __catedra: str
    __porcentaje: float
    def __init__(self,apellido, nombre,cuil, sueldoBasico, antig,carrera,cargo,catedra,areaInv='',tipoInv='', porcentaje = 0.0):
        super().__init__(apellido, nombre,cuil,sueldoBasico, antig,carrera,cargo,catedra,areaInv,tipoInv, porcentaje)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
        self.__porcentaje = porcentaje
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                cuil = self.getCUIL(),
                sueldobase = self.getSueldoBase(),
                antiguedad = self.getAntiguedad(),
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra
            )
        )
        return d
    def modificarPorcentajeporcargo(self,nuevoporc):
        self.__porcentaje = nuevoporc
        print("Porcentaje por cargo modificado: {}".format(self.getPorcentaje()))
    def getPorcentaje(self):
        return self.__porcentaje
    def calculoSueldo(self):
        sueldo = self.getSueldoBase() + (self.getSueldoBase()*(self.getAntiguedad() / 100))
        if self.__cargo == "Simple" or "simple":
            sueldo += (self.getSueldoBase() * 10)/100
        elif self.__cargo == "semiexclusivo" or "Semiexclusivo":
            sueldo += (self.getSueldoBase()*20)/100
        elif self.__cargo == "exclusivo" or "Exlusivo":
            sueldo += (self.getSueldoBase()*50)/100
        return sueldo
    def __str__(self) -> str:
        return super().__str__() + ' ' + self.__carrera + ' ' + self.__cargo + ' ' + self.__catedra
    def __gt__(self, otro):
        return super().__gt__(otro)
        
    
