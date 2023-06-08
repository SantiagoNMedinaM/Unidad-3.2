from ClasePersonal import Personal
from ClaseDocente import Docente
import json
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseApoyo import Apoyo
from ClaseInvestigador import Investigador
from ClaseLista import Lista
class ObectEncoder:
    def guardarJSON(self,d,archivo):
        with open(archivo,'w',encoding='UTF-8') as destino:
            json.dump(d,destino,indent=4)
            destino.close()
    def leerJSON(self,archivo):
        with open(archivo,'r',encoding='UTF-8') as fuente:
            d = json.load(fuente)
            fuente.close
            return d
    def decodificar(self,d):
        if "__class__" not in d:
            return d
        else:
            class_name = d["__class__"]
            class_ = eval(class_name)
            if class_name == "Lista":
                listaP = class_()
                personas = d["personal"]
                for i in range (len(personas)):
                    uP = personas[i]
                    class_name = uP.pop("__class__")
                    class_ = eval(class_name)
                    atributos = uP["__atributos__"]
                    UnPersonal = class_(**atributos)
                    listaP.agregarElemento(UnPersonal)
        return listaP

