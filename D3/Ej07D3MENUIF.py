##1 suma 2 resta 3 div 4 imprime los datod del uusario 5, multoplicacion  de dos digitos 7 tamblas de multiplicar clase 7 salir

print (" Elije la opcion")
seleccion=int(input("0.- comparacion de numeros. \n1.- Suma, \n2.-Resta. \n3.-Divicion. \n4.-Datos del Usuario. \n5.-Multiplicacion. \n6.- tablas de bultiplicar. \n7.- salir"))
if seleccion==1:
     a=int(input("ingrese el numero A: "))
     b=int(input("ingrese el numero B: "))
     c=a+b
     print("el resultado de la suma es : ",c)
elif seleccion==2:
     a=int(input("ingrese el numero A: "))
     b=int(input("ingrese el numero B: "))
     c=a-b
     print("el resultado de la resta es : ",c)
elif seleccion==3:
     a=int(input("ingrese el numero A: "))
     b=int(input("ingrese el numero B: "))
     c=a/b
     print("el resultado de la divicion es : ",c)
elif seleccion==4:
     print ("elejiste la opcion 3 datos. \n ingrese sus datos")
     nombre=input ("tu nombre es?")
     edad = input("tu edad es?")
     peso = input("tu peso es?")
     print (" tellamas: ", nombre, "\ntienes: ",edad,"años","\npesas:",peso,"Kg")

elif seleccion==5:
          a=int(input("ingrese el numero A: "))
          b=int(input("ingrese el numero B: "))
          c=a*b
          print("el resultado de la multiplicacion es : ",c)
elif seleccion==6:
     var2= int(input("que tabla quieres ver?: "))
     i =int(input("hasta que numero deseas ver"))
     i=i+1

     for i in range(i):
         print (i," *  ",var2," = ",i*var2)

elif seleccion==7:
     print ("fin del programa")

elif seleccion==0:
     a=int(input("dame el valor del numero A: "))
     b=int(input("dame el valor de B: "))
     ##c=int(input("dame el valor de C: "))

     print ("se procede a evealuar  los numeros")


     if a==b: ##and b==c:
         print ("son iguales")
     if  a>b:
         print ("A es mayor")
     if a<b:
         print ("B es mayor")


     print ("fin del programa")
     input(".......")

input (".....")
