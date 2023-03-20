

# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona():
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if type(valor)==str and len(valor)>3:
            self.__nombre = valor
        else:
            print(f"{valor} no es un nombre valido")
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, valor):
        if valor>0:
            self.__edad = valor
        else:
            print("la edad no puede ser negativa")

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, valor):
        if type(valor)==int:
            self.__dni = valor
        else:
            print("el dni debe ser un entero")
    def mostrar(self):
        return f"El nombre de la persona es {self.__nombre} y tiene {self.__edad} años."

    def Es_mayor_de_edad(self):
        if (self.__edad >= 18):
            return True
        else:
            return False
""" 
p1 = Persona("Marta", 94, 5123456)
print(p1.nombre)
p1.nombre = "Mecha"
p1.edad = 39
p1.dni = 32540923
print(p1.mostrar())
print(p1.Es_mayor_de_edad())
 """

# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos.

class Cuenta(Persona):

    __saldo = 0

    def __init__(self, nombre, edad, dni, titular):
        super().__init__(nombre, edad, dni)
        self.__titular = titular

    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo

    def mostrar(self):
        return f"Nombre: {self.nombre}\nTitular: {self.__titular}\nEdad: {self.edad}\nDNI: {self.dni}\nSaldo: {self.__saldo}\n"
    
    def ingresar(self, valor):
        self.__saldo += valor

    def retirar(self, valor):
        self.__saldo -= valor
""" 
c1 = Cuenta("Juan Fernandez", 39, 32323232, "Juan Fernandez")
print(c1.mostrar())
c1.ingresar(1000.50)
c1.retirar(4500321.75)
print(c1.mostrar()) """

# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta.

class CuentaJoven(Cuenta):

    __saldo = 0

    def __init__(self, nombre, edad, dni, titular, bonificacion):
        super().__init__(nombre, edad, dni, titular)
        self.__bonificacion = bonificacion
    
    def ingresar(self, valor):
        self.__saldo =+ valor * self.__bonificacion / 100

    def es_titular_valido(self):
        if self.edad>=18 and self.edad<25:
            return True
        else:
            return False
        
    @property
    def saldo(self):
        return self.__saldo
    
    def retirar(self, valor):
        if self.es_titular_valido():
            self.__saldo -= valor
        else:
            print("Debe ctener entre 18 y 25 años para retirar dinero")

""" c2 = CuentaJoven("Marcos", 21, 52000001, "Marcos", 5)
print(c2.mostrar())
print(c2.saldo)
c2.retirar(2000)
print(c2.saldo)
 """
