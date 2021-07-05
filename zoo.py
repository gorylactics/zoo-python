from animal import Animal
from leon import Leon
from oso import Oso
from pyton import Pyton

zoologico = []
inicio = f'\nBienvenido a GoryZoo\nDesea entrar???\n---->(Y/N)<----'
print(inicio)
respuesta = input()
opciones = f'Bienvenido\nQue le gustaria hacer???:\n\n1_Ver los animales\n2_Crear animales\n3_Alimentar a los animales\n4_Ver estado de los animales\n5_Salir'

if respuesta == 'y' or respuesta == 'Y':   
    print('\n') 
    while True:
        print(opciones)
        print('\n')
        respuestaInterna = int(input())
        if respuestaInterna == 1:
            if zoologico == []:
                print('el zoo esta vacio por el momento')
                print('\n')
            else:
                print(zoologico)
                print('\n')
        elif respuestaInterna == 2:
            print(f'elija el animal:\n1_Oso\n2_Leon\n3_Pyton')
            eleccion = int(input())
            if eleccion == 1:
                tipo = 'Oso'
                nombre = input('ingrese nombre\n')
                edad = int(input('ingrese edad\n'))
                atributo = input('ingrese atributo\n')
                zoologico.append(Oso(tipo , nombre , edad , atributo))
                print('el animal se sumo al zoo')
            elif eleccion == 2:
                tipo = 'Leon'
                nombre = input('ingrese nombre\n')
                edad = int(input('ingrese edad\n'))
                atributo = input('ingrese atributo\n')
                zoologico.append(Leon(tipo , nombre , edad , atributo))
                print('el animal se sumo al zoo')
            elif eleccion == 3:
                tipo = 'Pyton'
                nombre = input('ingrese nombre\n')
                edad = int(input('ingrese edad\n'))
                atributo = input('ingrese atributo\n')
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
    
