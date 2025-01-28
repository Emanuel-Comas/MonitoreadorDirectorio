from plyer import notification
from watchdog.events import FileSystemEventHandler
from config import directorio_a_monitorear


class ManejadorDeEventos(FileSystemEventHandler):

    def on_modified(self, evento):
        self.responder_evento(evento)
    
    def on_created(self, evento):
        self.responder_evento(evento)
    
    def on_deleted(self, evento):
        self.responder_evento(evento)


    # Funcion para responder a los eventos.
    def responder_evento(evento):
        print(f'Evento detectado: {evento.event_type}', {evento.src_path})

        # Acciones que se pueden tomar.
        if evento.event_type == 'modified':
            print(f'El archivo {evento.src_path} ah sido modificado.')
            # Se envia una notificacion al desktop.
            notification.notify(
                title = 'Modificacion de archivo ejecutada.',
                message = f'Se ha modificado un archivo en la ruta {directorio_a_monitorear}',
                timeout = 10 # Tiempo en segundos que durara la alerta.
            )

        elif evento.event_type == 'created':
            print(F'Un nuevo archivo se a creado: {evento.src_path}')

            notification.notify(
                title = 'Creacion de archivo ejecutada.',
                message = f'Se ha creado un archivo en la ruta {directorio_a_monitorear}',
                timeout = 10 # Tiempo en segundos que durara la alerta.
            )

        elif evento.event_type == 'deleted':
            print(f'El archivo {evento.src_path} ha sido eliminado.')

            notification.notify(
                title = 'Eliminacion de archivo ejecutada.',
                message = f'Se ha eliminado un archivo en la ruta {directorio_a_monitorear}',
                timeout = 10 # Tiempo en segundos que durara la alerta.
            )

        else:
            print(f'Evento desconosido: {evento.src_path}')