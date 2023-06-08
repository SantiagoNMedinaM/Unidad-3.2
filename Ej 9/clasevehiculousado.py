from clasevehiculo import Vehiculo

class VehiculoUsado(Vehiculo):
    __patente=str
    __año=int
    __kilometraje=int


    def __init__(self, modelo, cantpuertas, color, preciobase, marca,patente,año,kilometraje):
        super().__init__(modelo, cantpuertas, color, preciobase, marca)
        self.__patente=patente
        self.__año=año
        self.__kilometraje=kilometraje

    def toJSON(self):
        d=dict(
            __class__==self.__class__.__name__,
            __atributos__=dict(
                       modelo=self.__modelo,
                       cantpuertas=self.__cantpuertas,
                       color=self.__color,
                       preciobase=self.__preciobase,
                       marca=self.__marca,
                       patente=self.__patente,
                       año=self.__año,
                       kilometraje=self.__kilometraje 
            )
        ) 
        return d   

    def getPatente(self):
        return self.__patente
    def getAño(self):
        return self.__año
    def getKilometraje(self):
        return self.__kilometraje   
    
    def modificarpreciobase(self,precionuevo):
        self.__preciobase=precionuevo

    def mostrarprecioventa(self):
        if isinstance(self,VehiculoUsado):
            precioventa=0
            añoant=2023-self.getAño()
            precioventa=float(super().getPreciobase()-float((super().getPreciobase()/100)*añoant))
            if self.getKilometraje()>100000:
                precioventa=float(precioventa-float(2*precioventa/100))
        return precioventa              

    def __str__(self):
        return 'Modelo:{} Cantpuertas:{} Color:{} Preciobase:{} Marca:{} Patente:{} Año:{} Kilometraje:{}'.format(self.getModelo(),self.getCantpuertas(),self.getColor(),self.getPreciobase(),self.getMarca(),self.__patente,self.__año,self.__kilometraje) 