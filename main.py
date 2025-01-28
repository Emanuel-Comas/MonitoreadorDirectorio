import os
import time
from watchdog.observers import Observer
from manejador_de_eventos import ManejadorDeEventos
from config import directorio_a_monitorear

def monitorear_directorio():
    # Se crea un objeto observador
    observer = Observer()
    # Se establece el manejador de eventos
    manejador = ManejadorDeEventos()
    # Establece al observacion en el directorio
    observer.schedule(manejador, directorio_a_monitorear, recursive=True)

    # Se inicia el observador
    observer.start()
    print(f'Monitoreo de el directorio {directorio_a_monitorear}')
    try:
        while True:
            # Se mantiene en ejecucion el script.
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print('Monitoreo detenido.')
    observer.join()

    

# Ejecucion del script
if __name__ == '__main__':
    monitorear_directorio()