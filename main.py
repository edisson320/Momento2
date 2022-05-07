
print("")

from ClassBanco.Banco import Cliente


#lisCliente=[]

cliente=Cliente()
opcion=7

print("Crea tu cuenta")
#while(opcion=="x"):
#SETTER
cliente.nombre=input("Digite su nombre: ")
cliente.apellido=input("Digite su apellido: ")
cliente.cedula=int(input("Ingrese el numero de su cedula: "))
cliente.ciudad=input("Ingrese la ciudad donde vive: ")
cliente.cuenta=int(input("Digite el nuemro de su cuanta: "))
cliente.saldo=int(input("Digite en monto a consignar: "))

print("")
print("¿Qué deseas Hacer? 1_para ver su saldo, 2_para consignar" )
print("")

while(opcion!=0):
    opcion = float(input("Ingrese la opción: "))
    if(opcion == 1):
        print(f"Su saldo es: {cliente.saldo}")
    elif(opcion==2):
        valor=float(input("Ingrese el valor a consignar: "))
        cliente.consignar(valor)       
    elif(opcion==3):
        valor=float(input("Ingrese el valor a retirar: "))
        if(valor>cliente.saldo):
            print("Su saldo es insuficiente")
        else:
            cliente.retirar(valor)
               
else:
    print("Fin de la Transacción")



