class ViajeroF:
    __num_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self, num, dni, nom, ape, millacum):
        self.__dni = dni
        self.__num_viajero = num
        self.__millas_acum = millacum
        self.__nombre = nom
        self.__apellido = ape

    def cantidadTotalMillas(self):
        return self.__millas_acum

    def acumularMillas(self):
        millas= int(input("Ingrese las millas a acumular "))
        self.__millas_acum += millas
        return self.__millas_acum

    def canjearMillas(self):
        canje= int(input("Ingrese las millas a canjear "))
        if self.__millas_acum >= canje:
            self.__millas_acum -= canje
        else:
            print("No tiene la cantidad de millas necesarias para ese canje")
            print("Usted posee " + str(self.__millas_acum))
            self.canjearMillas()
        return self.__millas_acum

    def compararnumviajero (self, num):
        if (self.__num_viajero==num):
            return 1
