from ClaseObjectEncoder import ObectEncoder
from ClaseLista import Lista
from ClaseMenu import Menu
from ClaseInterfaceTesorero import ITesorero
from ClaseInterfaceDirector import IDirector
from zope.interface import implementer
if __name__ == "__main__":
    empleados = Lista()
    jsonF = ObectEncoder()
    diccionario = jsonF.leerJSON("personal.json")
    print(diccionario)
    empleados = jsonF.decodificar(diccionario)
    tipo = int(input("Ingrese como desea ingresar al programa: 1) Usuario 2)Tesorero 3) Director: "))
    if tipo == 1:
        menu = Menu()
        menu.opciones(empleados)
    elif tipo == 2:
        usuario = str(input("Ingrese usuario: "))
        if usuario == "uTesoreso":
            contrasenia = str(input("Ingrese contraseña: "))
            if contrasenia == "ag@74ck":
                dni = str(input("Ingrese DNI de la persona a consultar sueldo"))
                empleados.tesorero(dni)
    elif tipo == 3:
        usuario = str(input("Ingrese usuario: "))
        if usuario == "uDirector":
            contrasenia = str(input("Ingrese contraseña: "))
            if contrasenia == "ufC77#!1":
                opcion = 0
                while opcion != 5:
                    menuops = "Menu de opciones"
                    print(menuops.center(50,"-"))
                    print("1) Modificar sueldo")
                    print ("2) Modificar porcentaje por cargo")
                    print("3) Modificar porcentaje por categoria")
                    print("4) Modificar Importe extra")
                    print ("5) Salir.")
                    opcion = int(input("Ingrese una opcion: "))
                    if opcion == 1:
                        basico = float(input("Ingrese nuevo sueldo basico"))
                        dni = str("Ingrese dni de la persona a modificar el sueldo basico")
                        empleados.modificarBasico(dni,basico)
                    if opcion == 2:
                        dni = str(input("Ingrese dni de la persona a cambiar porcentaje por cargo"))
                        nuevoPorcentaje = float(input("Ingrese nuevo porcentaje por cargo"))
                        empleados.modificarPorcentajeporcargo(dni,nuevoPorcentaje)
                    if opcion == 3:
                        dni = str(input("Ingrese DNI de la persona a cambiar porcentaje por categoria"))
                        nuevoPorcentaje = float(input("Ingrese nuevo porcentaje por categoria"))
                        empleados.modificarPorcentajeporcategoría(dni,nuevoPorcentaje)
                    if opcion == 4:
                        dni = str(input("Ingrese DNI de la persona a cambiar el importe extra"))
                        nuevoImporte = float(input("Ingrese nuevo importe extra"))
                        empleados.modificarImporteExtra(dni,nuevoImporte)