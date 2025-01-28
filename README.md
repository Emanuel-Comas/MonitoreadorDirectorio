# Monitoreo de directorio

-- Archivo principal: 'main.py'.

## Descripcion

-- Este proyecto esta diseñado para monitorear un directorio en busca de cambios en los archivos.
Cuando se detecta una modificacion, creacion o eliminacion de un archivo, se ejecuta una accion configurada, (como una notificacion).
-- Este tipo de herramienta puede ser útil para tareas de seguridad (Blue team) o para automatización de
procesos de sistemas de archivos.


### Funcionalidades principales y caracteristicas de seguridad

-- Monitoreo en tiempo real.
-- Alertas automaticas: notificacion en el escritorio cuando se detectan cambios (modificacion, creacion o eliminacion).
-- Posibilidad de realizar copias de seguridad después de ciertos eventos (si se hablita la opcion, actualmente no subida/habilitada).


### Tecnologias utilizadas

**Python 3.12.3**: Lenguaje de programación principal.
**Watchdog**: Libreria para monitorear el sistema de archivos.
**plyer**: Libreria para enviar notificaciones del sistema.
**subprocess**: Para ejecutar comandos del sistema (Como configurar para ejecutar backups).
**os**: Libreria estándar de python para interactuar con el sistema operativo.


### Posibles integraciones

**Logging**: Se puede agregar soporte para enviar eventos a un servidor syslog centralizado para auditoria y análisis posterior.
**Backup y Recuperación**: Si se configura, el sistema puede hacer copias de seguridad de los archivos antes de un cambio importante, como parte de una estrategia de recuperación. ante desastres


### Estrategia de respuesta

**Alertas Automáticas**: El sistema notifica inmediatamente a los administradores de seguridad sobre cualquier cambio inesperado o no autorizado.


### Normativas de seguridad cumplidas

**ISO 27001**: Cumple con los requisitos de seguridad de la información, ayudando a proteger la confidencialidad, integridad y disponibilidad de los datos.

**GDPR**: Asegura el cumplimiento de la normativa de proteccion de datos personales.

**PCI DSS**: Si se configura para entornos financieros, puede cumplir con los requisitos para el manejo de tarjetas de crédito y datos financieros.


### Configuración

-- Crea un archivo llamado 'directorio.py', luego crea la ruta a la cual monitorear.
(ej:  directorio_a_monitorear = r'Disco:/R/Ruta/Ruta/Tu_ruta').

luego la importas a main.py.
(ej: from config import directorio_a_monitorear).


