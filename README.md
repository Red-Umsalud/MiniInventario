# Documentación de uso Básica

## Introducción

La aplicación esta pensada en ser utilizada desde un dipositivo móvil directamente desde el panel de administración de Django.
Por esta razón, es necesaria la creación de un nuevo "Super Usuario", de forma que se puedan agregar nuevos artículos a los depósitos de Red Umsalud II. Esto se puede hacer mediante el siguiente comando:

```sh
python manage.py createsuperuser
```

O también de forma alternativa:
```shell
django-admin createsuperuser
```

En caso de haber fallado con esta configuración es posible que usted no sepa de entornos virtuales de trabajo y/o de Django por lo que debe activar el entorno virtual existente e instalar las dependencias necesarias del archivo `requirements.txt`.

Para esto debe hacer lo siguiente:

Desde Linux o WSL, primero crear un entorno virtual de Python ingresando a la raiz del directorio y posteriormente ejecutando el siguiente comando:

```shell
virtualenv <nombredelentorno_porconvencion_env>
```
Ejemplo:
```sh
virtualenv env
```

Felicidades!!!1 usted creó su primer entorno virtual de Python. Ahora es necesario activar dicho entonrno para instalar los paquetes y poder ejecutar los comandos de Django. Para esto ejecutar lo siguiente:

```sh
source <ubicacion_del_archivo_activate>
```

Ejemplo:
```sh
source env/bin/activate
```

Una vez se tiene activo el Entorno Virtual debemos instalar las bibliotecas de Python utilizadas en el proyecto:

```sh
pip install -r requirements.txt
```

Si todo funcionó de forma correcta ya se puede iniciar el servidor, para esto ejecutamos el comando:

```sh
python manage.py runserver 0.0.0.0:5000
```

Con lo que la aplicación aceptará las todas las conexiones a través del puerto 5000.

fin del comunicado.