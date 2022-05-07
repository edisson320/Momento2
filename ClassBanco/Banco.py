class Cliente():
    def __init__(self):
    
        self.__nombre=None
        self.__apellido=None        
        self.__cedula=None
        self.__ciudad=None
        self.__cuenta=None
        self.__saldo=None

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def cedula(self):
        return self.__cedula

    @property
    def ciudad(self):
        return self.__ciudad

    @property
    def cuenta(self):
        return self.__cuenta
    
    @property
    def saldo(self):
        return self.__saldo

    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @apellido.setter
    def apellido(self,apellido):
            self.__apellido=apellido
    
    @cedula.setter
    def cedula(self,cedula):
        self.__cedula=cedula
    
    @ciudad.setter
    def ciudad(self,ciudad):
        self.__ciudad=ciudad
    
    @cuenta.setter
    def cuenta(self,cuenta):
        self.__cuenta=cuenta

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo=saldo

    def consultaSaldo(self):
        saldoTotal=self.saldo
        return saldoTotal
    
    def consignar(self,valor):
        self.saldo=self.saldo+valor
        print("Exito en la transacción") 
        

    def retirar(self,valor):
        self.saldo=self.saldo-valor 
        print("Exito en la transacción") 
