class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_perdidos = 0
        self.sets_ganados = 0
        self.sets_perdidos = 0
        self.puntos_favor = 0
        self.puntos_contra = 0

    def registrar_puntos(self, puntos):
        self.puntos += puntos
    
    def registrar_partidos_ganados(self):
        self.partidos_ganados += 1
        self.partidos_jugados += 1
    
    def registrar_partidos_perdidos(self):
        self.partidos_perdidos += 1
        self.partidos_jugados += 1
    
    def registrar_sets_ganados(self, numSetsGanados):
        self.sets_ganados += numSetsGanados
    
    def registrar_sets_perdidos(self, numSetsPerdidos):
        self.sets_perdidos += numSetsPerdidos
    
    def registrar_puntos_favor(self, puntos):
        self.puntos_favor += puntos
    
    def registrar_puntos_contra(self, puntos):
        self.puntos_contra += puntos

    def __str__(self):
        return f'Nombre: {self.nombre}\n - Puntos: {self.puntos}\n - Partidos jugados: {self.partidos_jugados}\n - Partidos ganados: {self.partidos_ganados}\n - Partidos perdidos: {self.partidos_perdidos}\n - Sets ganados: {self.sets_ganados}\n - Sets perdidos: {self.sets_perdidos}'