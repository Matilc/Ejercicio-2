import os
from ManejadorViajeros import ManejadorViajero
def menu_opciones():
    print("Menú de opciones:")
    print("1. Consultar cantidad de millas totales")
    print("2. Acumular millas")
    print("3. Canjear millas")
    print("4. Salir")

if __name__=='__main__':
    mv=ManejadorViajero()
    mv.cargarviajeros()
    i=mv.obtener_viajero()
    print (i)
    viajeroaux=mv.get_viajero(i)
    while True:
        os.system('cls')
        menu_opciones()
        menu= {
            "1": "print ('Sus millas totales son '+str(viajeroaux.cantidadTotalMillas()))",
            "2": "print ('Sus millas totales son '+str(viajeroaux.acumularMillas()))",
            "3": "print ('Sus millas totales son '+str(viajeroaux.canjearMillas()))",
            "4": "print ('Gracias por usar el sistema')"
        }
        opcion= input("Elija la opción ")
        os.system('cls')
        if opcion in menu:
            if opcion=='4':
                eval(menu[opcion])
                aux=input()
                break
            else:
                eval(menu[opcion])
                aux=input()
        else:
            print ('La opción que ha ingresado no es válida, por favor, ingrese una opción nuevamente')