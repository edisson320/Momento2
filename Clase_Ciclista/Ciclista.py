
'''Codificar un programa que permita recibir el nombre,
edad, país, equipo y tiempo(minutos)) de la última prueba
de crono individual de varios ciclistas del giro de
Italia, al final el software estará en la capacidad de
indicar cual fue el ciclista con el mejor tiempo y
mostrar todos sus datos
'''

class Ciclista:
    def __init__(self):
        self.__nombre=None
        self.__edad= None
        self.__pais= None
        self.__equipo=None
        self.__tiempo= None

    #GETTERS
    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def edad(self):
        return(self.__edad)

    @property
    def pais(self):
        return(self.__pais)
    
    @property
    def equipo(self):
        return(self.__equipo)

    @property
    def tiempo(self):
        return(self.__tiempo)

    #SETTERS
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    
    @edad.setter
    def edad(self,edad):
        self.__edad=edad

    @pais.setter
    def pais(self,pais):
        self.__pais=pais
    
    @equipo.setter
    def equipo(self,equipo):
        self.__equipo=equipo
    
    @tiempo.setter
    def tiempo(self,tiempo):
        self.__tiempo=tiempo

    
    def mejorTiempo(self,listaCiclistas):
        mejorTiempo=listaCiclistas[0].get('tiempo')
        for ciclista in listaCiclistas:
            if (ciclista.get('tiempo') < mejorTiempo):
                mejorTiempo=ciclista.get('tiempo')
                # print(f"El nombre del ciclista con el mejor tiempo es: {ciclista.get('nombre')}")
                print(f" El mejor tiempo es:  {mejorTiempo}")
    

    