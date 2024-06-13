from borracho import BorrachoTradicional 
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, show

def caminata(campo,borracho,pasos):
    inicio =campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho= tipo_de_borracho(nombre='Pedro')
    origen = Coordenada(0,0)
    distancias =[]

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho,origen)
        simular_caminata = caminata(campo, borracho, pasos) 
        distancias.append(round(simular_caminata, 1))
    return distancias

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label= 'pasos', y_axis_label= 'distancia ')
    grafica.line(x, y)
    
    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distacias_media_por_caminata = []

    #calculo de estadisticas 
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos,numero_de_intentos,tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distacias_media_por_caminata.append(distancia_media)
        distancia_max = max(distancias)
        distancia_min = min(distancias)
        # tipo_de_borracho.__name__  nos da el tipo de la clase
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'distancia media {distancia_media} , distancia maxima = {distancia_max} y la minima {distancia_min} ')
    graficar(distancias_de_caminata, distacias_media_por_caminata)


if __name__ == '__main__':
    # 
    distancias_de_caminata = [10,100,1000,10000]
    # cantidad de veces que queremos correr esta simulacion 
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)

