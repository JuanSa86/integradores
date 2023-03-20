import numpy as np

# 1. Escribir una función que calcule el máximo común divisor entre dos números.
 
divX =[]
divY =[]
def maxComunDiv(x,y):
    dcm=1
    for numero in range(1,x+1):
        i=x%numero
        if (i == 0):
            divX.append(numero)
        i+=1
    #print(divX)
    for numero in range(1,y+1):
        i=y%numero
        if (i == 0):
            divY.append(numero)
        i+=1
    #print(divY)
    j = len(divX)-1
    while (divX[j] not in divY):
        j-=1
    dcm=divX[j]
    return dcm

""" 
num1 = 981
num2 = 2745
print("-------------\nMi formula CDM")
print (maxComunDiv(num1,num2),"\n-------------")

print("-------------\nCDM con pynum")
x = np.gcd(num1, num2)
print(x,"\n-------------")
 """

# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def minComunMltiplo(x,y):
    mcm = x * y / maxComunDiv(x,y)
    return mcm

""" 
print("-------------\nMi formula MCM")
print(minComunMltiplo(num1,num2))

w = np.lcm(num1, num2)
print("-------------\nMCM con pynum")
print(w,"\n-------------")
 """

# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).


cadena = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
diccionarioPalabrasFrecuencia = {}
def decadenaAdiccionario(cadena):
    listaPalabras = cadena.rsplit(" ")
    #print(listaPalabras)
    for palabra in listaPalabras:
        diccionarioPalabrasFrecuencia[palabra] = listaPalabras.count(palabra)
    return diccionarioPalabrasFrecuencia

"""
print("-------------------------------------")
print(decadenaAdiccionario(cadena))
print("-------------------------------------")
"""


# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia
 
def maxFrecuenciaTupla(diccionario):
    z=0
    i=0
    xd = 0
    for x, y in diccionario.items():
        #print(x, y)
        if y > z:
            z = y
            xd = x
        i+=1
        #print (diccionario[xd])
        keyMaxFrec = xd
        #print(diccionario[xd])
    tuplaMaxFrec = tuple((keyMaxFrec, z))
    return tuplaMaxFrec

""" 
dicc = decadenaAdiccionario(cadena)
tuplaMax = maxFrecuenciaTupla(dicc)
print(-------------------------------------)
print(tuplaMax)
print(-------------------------------------)
"""

# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.

def get_int_1(): #iterativa
    i=1
    while True:
        entrada = input("ingrese un numero: ")
        try:
            numero = int(entrada)
            if type(numero) == int:
                if i == 1:
                    print("Usted a introducido correctamente un numero entero. Y lo hizo en el primer intento!")
                    break
                else:
                    print(f"Usted a introducido correctamente un numero entero. Aunque te llevó {i} intentos lograrlo...")
                    i = 0
                    break
        except ValueError:
            i+=1
            print("Ese no es un numero. Por favor vuelva a intentarlo")
    print("-----------------------")

def get_int_2(): #recursiva
    x = input("ingrese un numero: ")
    try:
        x = int(x)
        print("Usted a introducido correctamente un numero")
    except ValueError:
        print(f"'{x}' no es un numero. Por favor vuelva a intentarlo")
        get_int_2()

#get_int_1()
#get_int_2()

