from animal import Animal
from leon import Leon
from oso import Oso
from pyton import Pyton

zoologico = []
inicio = f'Bienvenido al zoo del Gory\nDesea entrar???\nIngrese:\nY/N'
print(inicio)
respuesta = input(str())
opciones = f'Bienvenido\nQue le gustaria hacer???:\n1_Ver los animales\n2_Crear animales\n3_Alimentar a los animales\n4_Ver estado de los animales\n5_Salir'

if respuesta == 'y' or respuesta == 'Y':   
    print('*'*100) 
    while True:
        print(opciones)
        print('*'*100)
        respuestaInterna = int(input())
        if respuestaInterna == 1:
            if zoologico == []:
                print('el zoo esta vacio por el momento')
                print('*'*100)
            else:
                print(zoologico)
                print('*'*100)
        elif respuestaInterna == 2:
            print(f'elija el animal:\n1_Oso\n2_Leon\n3_Pyton')
            eleccion = int(input())
            if eleccion == 1:
                tipo = 'Oso'
                nombre = input('ingrese nombre')
                edad = int(input('ingrese edad'))
                atributo = input('ingrese atributo')
                zoologico.append(Oso(tipo , nombre , edad , atributo))
                print('el animal se sumo al zoo')
            elif eleccion == 2:
                tipo = 'Leon'
                nombre = input('ingrese nombre')
                edad = int(input('ingrese edad'))
                atributo = input('ingrese atributo')
                zoologico.append(Leon(tipo , nombre , edad , atributo))
                print('el animal se sumo al zoo')
            elif eleccion == 3:
                tipo = 'Pyton'
                nombre = input('ingrese nombre')
                edad = int(input('ingrese edad'))
                atributo = input('ingrese atributo')
                zoologico.append(Pyton(tipo , nombre , edad , atributo))
                print('el animal se sumo al zoo')


        elif respuestaInterna == 3:
            print('alimentando animales') 
        elif respuestaInterna == 4:
            print('Mostrando estado de animales')
        elif respuestaInterna == 5:
            print('Adios')
            break
elif respuesta == 'n' or respuesta == 'N':
    print('Hasta luego')
else:
    print(f'opcion no valida\nBuen dia')
    
