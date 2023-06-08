from clasenodo import Nodo

class Lista:
    __comienzo=Nodo
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__tope=0
    def agregarVehiculoFinal(self,vehiculo):
        nuevonodo = Nodo(vehiculo)
        if self.__comienzo == None:
            self.__comienzo = nuevonodo
        else:
            temporal = self.__comienzo
            while temporal.getSiguiente() is not None:
                temporal = temporal.getSiguiente()
            temporal.setSiguiente(nuevonodo)    
        self.__tope+=1    

    def agregarVehiculoIndice(self,vehiculo,indice):
        nuevonodo=Nodo(vehiculo)
        if indice == 1:
            nuevonodo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevonodo
        else:
            temporal = self.__comienzo
            contador = 1
            while temporal:
                if contador + 1 == indice:
                    nuevonodo.setSiguiente(temporal.getSiguiente())
                    temporal.setSiguiente(nuevonodo)
                    break
                temporal = temporal.getSiguiente()
                contador += 1
        self.__tope+=1           

    def mostrarVehiculoIndice(self, indice):
        temporal = self.__comienzo
        contador = 0
        while temporal:
            if contador+1 == indice:
                return temporal.getTipo()
            temporal = temporal.getSiguiente()
            contador += 1

    def mostrartodos(self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.getDato())
            print('Importe de venta:{}'.format(aux.mostrarprecioventa()))
            aux=aux.getSiguiente()        

    def getTipo(self,posicion):
        c=0
        aux=self.__comienzo
        while aux!= None and c!= posicion:
            aux=aux.getSiguiente()
            c+=1
        if c==posicion:
            aux.getTipo()            

    def buscarpatente(self,patente):
        aux=self.__comienzo
        band=False
        while aux!= None and patente != aux.getPatente():
            aux=aux.getSiguiente()
        if aux.getPatente()==patente:
            band=True
        return band

    def modificarpreciobase(self,patente,nuevoprecio):
        aux=self.__comienzo
        while aux != None and patente!=aux.getPatente():
            aux=aux.getSiguiente()
        if aux.getPatente()==patente:
           aux.modificarpreciobase(nuevoprecio)     

    def mostrarprecioventa(self,patente):
        aux=self.__comienzo
        while aux!=None and patente!=aux.getPatente():
            aux=aux.getSiguiente()
        if aux.getPatente()==patente:
            return(aux.mostrarprecioventa())  

    def buscareconomico(self):
        min=9999999999
        minaux=''
        aux=self.__comienzo
        while aux!=None:
            if aux.mostrarprecioventa()<min:
                min=aux.mostrarprecioventa()
                minaux=aux
            aux=aux.getSiguiente()
        print('{}'.format(minaux.getDato()))
        print('Importe:{}'.format(minaux.mostrarprecioventa()))                     

    def getObjeto(self,posicion):
        aux=self.__comienzo
        c=0
        while aux!=None and c!=posicion:
            c+=1
            if c==posicion:
                return aux.getDato()
            aux=aux.getSiguiente()
            
    def obtenerultimo(self):
        aux=self.__comienzo
        c=0
        while aux!=None:
            c+=1
            if c==self.__tope:
                return aux.getDato()
            aux=aux.getSiguiente()

    def getPrecioXPatente(self,patente):
        aux=self.__comienzo
        while aux!=None:
            if aux.getPatente()==patente:
                return aux.mostrarprecioventa()
            aux=aux.getSiguiente()        

    def toJSON(self):
        aux=self.__comienzo
        listajson=[]
        while aux!=None:
            vehic=aux.toJSON()
            listajson.append(vehic)
            aux=aux.getSiguiente()  
        return listajson      