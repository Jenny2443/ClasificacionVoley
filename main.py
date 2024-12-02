import equipo

def crear_equipos():
    informatica = equipo.Equipo('Informatica')
    industriales = equipo.Equipo('Industriales')
    sistemas_teleco = equipo.Equipo('Sistemas Teleco')
    sistemas_informatica = equipo.Equipo('Sistemas Informatica')
    aeronauticos = equipo.Equipo('Aeronauticos')
    edificacion = equipo.Equipo('Edificacion')
    montes = equipo.Equipo('Montes')
    navales = equipo.Equipo('Navales')
    return [informatica, industriales, sistemas_teleco, sistemas_informatica, aeronauticos, edificacion, montes, navales]
    
def registrar_resultado(equipo1, equipo2, sets_equipo1, sets_equipo2):
    # Encontrar el equipo
    equipo1 = next((e for e in equipos if e.nombre == equipo1), None)
    equipo2 = next((e for e in equipos if e.nombre == equipo2), None)
    
    if equipo1 and equipo2:
        equipo1.registrar_sets_ganados(int(sets_equipo1))
        equipo1.registrar_sets_perdidos(int(sets_equipo2))
        equipo2.registrar_sets_ganados(int(sets_equipo2))
        equipo2.registrar_sets_perdidos(int(sets_equipo1))
        
        # Definir quien ha ganado
        if int(sets_equipo1) > int(sets_equipo2):
            equipo1.registrar_partidos_ganados()
            equipo2.registrar_partidos_perdidos()
        else:
            equipo2.registrar_partidos_ganados()
            equipo1.registrar_partidos_perdidos()
        
        # Definir puntos 
        equipo1.registrar_puntos(int(sets_equipo1))
        equipo2.registrar_puntos(int(sets_equipo2))
        
        return equipo1, equipo2
    else:
        print('Equipo no encontrado')
def mostrar_clasificacion(equipos):
    equipos_ordenados = sorted(equipos, key=lambda x: (-x.puntos, -x.partidos_ganados, -x.sets_ganados))
    #equipos_ordenados = sorted(equipos, key=lambda x: x.puntos, reverse=True)
    print("\nClasificación:")
    print("Equipo               Puntos  Partidos  PG  PP  SG  SP")
    print("-" * 50)
    for equipo in equipos_ordenados:
        print(f"{equipo.nombre:<20} {equipo.puntos:<8} {equipo.partidos_jugados:<9} {equipo.partidos_ganados:<3} {equipo.partidos_perdidos:<3} {equipo.sets_ganados:<3} {equipo.sets_perdidos:<3}")

if __name__ == '__main__':
    # Crear equipos
    equipos = crear_equipos()
    
    with open('resultados.txt', 'r') as archivo:
        for linea in archivo:
            equipo1, equipo2, sets_equipo1, sets_equipo2 = linea.strip().split('-')
            registrar_resultado(equipo1, equipo2, sets_equipo1, sets_equipo2)
            
    mostrar_clasificacion(equipos)
        