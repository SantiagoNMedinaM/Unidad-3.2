from ClasePersonal import Personal
class Apoyo(Personal):
    __categoria: str
    def __init__(self,nombre,apellido, cuil,sueldoBasico, antig, carrera= '', cargo= '', catedra= '', areaInv= '', tipoInv= '', categoria= 0):
        super().__init__(nombre, apellido,cuil,sueldoBasico, antig, carrera, cargo, catedra, areaInv, tipoInv)
        self.__categoria = categoria
    def getCat(self):
        return self.__categoria
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                cuil = self.getCUIL(),
                antiguedad = self.getAntiguedad(),
                categoria = self.__categoria
            )
        )
        return d
    def calculoSueldo(self):
        sueldo = self.getSueldoBase() + (self.getSueldoBase()*(self.getAntiguedad() / 100))
        if self.__categoria > 0 and self.__categoria <= 10:
            sueldo += (self.getSueldoBase()*10)/100
        elif self.__categoria > 10 and self.__categoria <= 20:
            sueldo += (self.getSueldoBase()*20)/100
        elif self.__categoria > 20 and self.__categoria <= 22:
            sueldo = (self.getSueldoBase()*30)/100
        return sueldo
    def __str__(self) -> str:
        return super().__str__() + ' ' + str(self.__categoria)
    def __gt__(self, otro):
        return super().__gt__(otro)