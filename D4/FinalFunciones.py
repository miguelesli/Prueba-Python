##suma resta multiplicar, divicion, comparar tres numeros
##escrivamultiplicacion indeterminada
def suma ():
    print ("Selecciono Suma\n")
    a=int(input("ingrese el numero A: "))
    b=int(input("ingrese el numero B: "))
    c=a+b
    print("el resultado de la suma es : ",c)
    print("\n\n Regresando al menu\nSeleccione Otra Opcion\n\n\n")

def resta():
    print ("Selecciono Resta\n")
    a=int(input("ingrese el numero A: "))
    b=int(input("ingrese el numero B: "))
    c=a-b
    print("el resultado de la resta es : ",c)
    print("\n\n Regresando al menu\nSeleccione Otra Opcion\n\n\n")
def TablasM ():
    print ("Selecciono Tablas de Multiplcar\n")
    var2= int(input("que tabla quieres ver?: "))
    i =int(input("hasta que numero deseas ver"))
    i=i+1
    for i in range(i):
        print (i," *  ",var2," = ",i*var2)
    print("\n\n Regresando al menu\nSeleccione Otra Opcion\n\n\n")

def Divicion():
     print ("Selecciono Divicion\n")
     a=int(input("ingrese el numero A: "))
     b=int(input("ingrese el numero B: "))
     c=a/b
     print("el resultado de la divicion es : ",c)
     print("\n\n Regresando al menu\nSeleccione Otra Opcion\n\n\n")

def comparacion():
    print ("Selecciono Comparacion de tres numeros\n")
    a=int(input("dame el valor del numero A: "))
    b=int(input("dame el valor de B: "))
    c=int(input("dame el valor de C: "))

    print ("se procede a evealuar  los numeros")


    if a==b and b==c:
        print ("son iguales")
    if  a>b and a>c:
        print ("A es mayor")
    if b>a and b>c:
        print ("B es mayor")
    if c>a and c>b:
       print ("C es mayor")
    print("\n\n Regresando al menu\nSeleccione Otra Opcion\n\n\n")

def IVAS():
    print ("Selecciono Calculo del IVA \n")
    costo_neto=int(input("proporcione el costo neto del articulo"))
    IVA= int(input("proporcione el porcentaje del IVA"))
    iva_p=IVA/100
    iva_producto=costo_neto*iva_p
    total=costo_neto+iva_producto
    print("el iva del producto con costo de ",costo_neto," equivale a ",iva_producto,"dando el monto todal",total)
    print("\n\n Regresando al menu\nSeleccione Otra Opcion\n\n\n")
def MultiplicacionS():
    print ("Selecciono Multiplicacion \n")
    a=int(input("ingrese el numero A: "))
    b=int(input("ingrese el numero B: "))
    c=a*b
    print("el resultado de la multiplicacion es : ",c)
    print("\n\n Regresando al menu\nSeleccione Otra Opcion\n\n\n")





seleccion =0
while seleccion !=9:
    print ("Menu: \n1.- Suma \n2.- Resta\n3.- Tamblas de Multiplicar\n4.- Divicion\n5.- Comparacion de tres numeros\n6.- Calculo de IVA\n7.- Multiplicacion\n8.- Salir")
    seleccion=int(input("seleccione una opcion"))

##suma
    if seleccion==1:
        suma()

##resta
    elif seleccion==2:
         resta()

##Tablas de multiplicar
    elif seleccion==3:
         TablasM()

##Divicion
    elif seleccion==4:
        Divicion()

##Compara de 3 numeros
    elif seleccion==5:
        comparacion()
##IVA
    elif seleccion==6:
        IVAS()

##multiplicacion simple
    elif seleccion==7:
        MultiplicacionS()
##salir
    elif seleccion==8:
        print ("a elegido salir del programa")
        seleccion=9



input(">>>>")
