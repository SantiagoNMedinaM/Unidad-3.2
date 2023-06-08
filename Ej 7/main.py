from ClaseObjectEncoder import ObectEncoder
from ClaseLista import Lista
from ClaseMenu import Menu
if __name__ == "__main__":
    empleados = Lista()
    jsonF = ObectEncoder()
    diccionario = jsonF.leerJSON("personal.json")
    print(diccionario)
    empleados = jsonF.decodificar(diccionario)
    menu = Menu()
    menu.opciones(empleados)
    