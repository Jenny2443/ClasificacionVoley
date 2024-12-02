# Generador de Rankings de Equipos

Este proyecto es una aplicación que genera un **ranking de equipos** basado en los resultados de partidos almacenados en un archivo de texto (`resultados.txt`). 

## Características

- **Lectura de resultados**: Procesa los resultados almacenados en `resultados.txt` para calcular el ranking.
- **Generación de rankings**: Ordena los equipos según las reglas predefinidas, puntos, partidos ganados, sets ganados
- **Gestión de equipos**: La clase `Equipo` permite gestionar la información de cada equipo.

## Estructura del proyecto
```bash
├── equipo.py        # Clase para gestionar equipos
├── resultados.txt   # Archivo con los resultados de los partidos
├── main.py          # Lógica principal del programa
├── README.md        # Documentación del proyecto
```

## Archivos del Proyecto

- `equipo.py`: Contiene la clase `Equipo`, que define las propiedades y métodos para manejar los equipos.
- `resultados.txt`: Archivo de texto donde se almacenan los resultados de los partidos. El programa lee este archivo para calcular el ranking.
- `main.py`: Es el archivo principal que ejecuta el programa, procesa los resultados y genera el ranking.

## Requisitos

- **Python 3.8 o superior**.

## Instalación

1. Clona este repositorio en tu ordenador:
   ```bash
   git clone <URL-del-repositorio>
2. Accede a la carpeta
   ```bash
   cd <nombre-del-repositorio>
3. Ejecuta el main
    ```bash
    python3 main.py

