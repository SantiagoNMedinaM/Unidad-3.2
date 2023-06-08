from clasevehiculo import Vehiculo
class VehiculoNuevo(Vehiculo):
    __version=str

    def __init__(self, modelo, cantpuertas, color, preciobase, marca,version):
        super().__init__(modelo, cantpuertas, color, preciobase, marca='Ford')
        self.__version=version

    def toJSON(self):
        d=dict(
            __class__==self.__class__.__name__,
            __atributos__=dict(
                       modelo=self.__modelo,
                       cantpuertas=self.__cantpuertas,
                       color=self.__color,
                       preciobase=self.__preciobase,
                       marca=self.__marca,
                       version=self.__version
            )
        ) 
        return d   

    def getVersion(self):
        return self.__version
    
    def mostrarprecioventa(self):
        if isinstance(self,VehiculoNuevo):
            precioventa=0
            precioventa=float(super().getPreciobase()+float((10*super().getPreciobase()/100)))
            if self.__version=='Full' or self.__version=='full':
                precioventa=float(precioventa+(float(2*precioventa/100)))
        return precioventa        

    
    def __str__(self):
        return 'Modelo:{} Cantpuertas:{} Color:{} Preciobase:{} Marca:{} Version:{}'.format(self.getModelo(),self.getCantpuertas(),self.getColor(),self.getPreciobase(),self.getMarca(),self.__version)
    
