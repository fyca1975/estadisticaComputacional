# simular una baraja de poker
# mayuscula porque son consatantes PALOS
import random 
import collections


PALOS = ['espada','corazon','rombos', 'trebol']
VALORES = ['as','2','3','4','5','6','7','8','9','10','j','q','k']


#generar la baraja 

def crear_baraja():
    barajas= []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor)) 
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)  # obtiene un valor diferente para evitar obtener el mismo valor sample
    return mano

def main(tamano_mano, intenos):
    barajas = crear_baraja()

    manos=[]
    for _ in range(intenos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores =[]
        for carta in mano:
            valores.append(carta[1])
          
        counter = dict(collections.Counter(valores))
        
        # encontrar un par
        for val in counter.values():
            if val == 2:
                pares += 1
                break
        probabilidad_par = pares /intenos
    print(f'la probabilidad de obtener un par en una mano de {tamano_mano} barajas es : {probabilidad_par}')


if __name__ == '__main__':    
    tamano_mano = int(input('de Cuantas barajas sera la mano '))
    intentos = int(input('Intentos para calcular la probabilidad: '))
    main(tamano_mano, intentos) 

    
    
    # barajas = crear_baraja()
    # print(barajas)
    # mano = obtener_mano(barajas, 5)
    # print (mano)
    