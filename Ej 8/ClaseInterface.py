from zope.interface import Interface, implementer
class IElemento(Interface):
    def insertarElemento(obj,pos):
        pass
    def agregarElemento(obj):
        pass
    def mostrarElemento(pos):
        pass
