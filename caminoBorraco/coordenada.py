

class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)
    
    def distancia(self, llega_cordenada):
        delta_x = self.x - llega_cordenada.x
        delta_y = self.y - llega_cordenada.y
# pitagoras distancia
        return(delta_x**2 + delta_y**2)**0.5