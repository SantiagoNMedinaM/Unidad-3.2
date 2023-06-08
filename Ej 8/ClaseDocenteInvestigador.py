from ClaseDocente import Docente
from ClaseInvestigador import Investigador
class DocenteInvestigador(Docente, Investigador):
    __categInvestigacion: str
    __importeExtra: float
    def __init__(self, apellido, nombre, cuil,sueldoBasico, antig, carrera, cargo, catedra, areaInv, tipoInv,categInvestigacion,importeExtra):
        super().__init__(apellido, nombre, cuil,sueldoBasico, antig, carrera, cargo, catedra, areaInv, tipoInv)
        self.__categInvestigacion = categInvestigacion
        self.__importeExtra = importeExtra
    def getCategoria(self):
        return self.__categInvestigacion
    def getImporteExtra(self):
        return self.__importeExtra
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                cuil = self.getCUIL(),
                sueldobase = self.getSueldoBase(),
                antiguedad = self.getAntiguedad(),
                carrera = self.getCarrera(),
                cargo = self.getCargo(),
                catedra = self.getCatedra(),
                areaInv = self.getAreaInvestigacion(),
                tipoInv = self.getTipoInvestigacion(),
                categoria = self.__categInvestigacion,
                impExtra = self.__importeExtra
            )
        )
        return d
    def modificarImporteExtra(self,nuevo):
        self.__importeExtra = nuevo
        print("El importe extra se modifico: {}".format(self.getImporteExtra()))
    def calculoSueldo(self):
        sueldo = Docente.calculoSueldo(self) + self.__importeExtra
        return sueldo
    def __str__(self) -> str:
        return super().__str__() + ' ' + self.__categInvestigacion + ' ' + str(self.__importeExtra)
    def __gt__(self, otro):
        return self.getNombre() > otro.getNombre()
