# simular una baraja de poker
# mayuscula porque son consatantes PALOS
import random 


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

if __name__ == '__main__':    
    barajas = crear_baraja()
    print(barajas)
    mano = obtener_mano(barajas, 5)
    print (mano)
    