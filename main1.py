

print()
from Clase_Ciclista.Ciclista import Ciclista

option = ()
lisCiclistas = []

while (option != "N"):
    escarabajo = Ciclista()

    escarabajo.nombre = input("Digite el nombre del corredor: ")
    escarabajo.edad = int(input("Digite la edad del corredor: "))
    escarabajo.pais = input("Ingrese el país del corredor: ")
    escarabajo.equipo=input("Digite el equipo al cual petenece: ")
    escarabajo.tiempo = int(input("Digite el tiempo hecho por el corredor : "))

    ciclista = dict(nombre=escarabajo.nombre, edad=escarabajo.edad,
                 pais=escarabajo.pais,equipo=escarabajo.equipo, tiempo=escarabajo.tiempo)
    lisCiclistas.append(ciclista)

    option = input("¿Desea agregar otra escuderia? : (Y/N)")
    
    escarabajo.mejorTiempo(lisCiclistas)
    



    

