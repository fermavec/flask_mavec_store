# Flask App
<br></br>

Con el archivo __init__.py en la carpeta app estamos dando a entender que la carpeta app funcionará como un paquete lo cual nos permitirá importar todo lo que esta dentro de la carpeta de forma directa.
<br></br>
<br></br>
## Estructurando el archivo.
<br></br>
1. Crear carpeta app con dos carpetas internas: static y templates.
<br></br>
2. Instalar las librerías Flask y Flask-script en un entorno virtual.
<br></br>
3. Crear el archivo __init__.py en la carpeta app que nos permitira trabajar con la importación y manejo de archivos.
<br></br>
4. Crear el archivo manage.py en la carpeta general. Este archivo nos permite gestionar nuestra app
<br></br>
5. Correr el servidor en la terminal con:

```sh
python3 manage.py runserver
```

- *Nota: Si tienes problema para correr el servidor debido a un modulo llamado _compat, puedes dirigirte a la carpeta del entorno virtual y cambiar la siguiente línea de código: from flask._compat import text_type por from flask_script._compat import text_type*
<br></br>

6. Crea una vista en tu archivo __init__.py para verificar que el servidor esté corriendo.
<br></br>
7. Genera un archivo en la carpeta principal llamado config.py. En este archivo, encontraremos los parametros de configuración de nuestro servidor por lo que tendrás que crear dos clases y un diccionario de configuración como se muestra en el archivo de este proyecto.
<br></br>
8. Actualiza la información de configuración en el archivo __init__.py y en el manage.py
<br></br>
9. Desarrolla un manejador de errores. En este caso creamos la carpeta error_templates y actualizamos el archivo init con un register_error_handler y una vista para el error 404.
<br></br>
10. Definir la estructura básica de nuestros templates. En este caso, comenzamos con un base.html, un body.html que hereda de base y un index.html que hereda del body.
<br></br>
11. (opcional) Trabajar con un framework de desarrollo como bootstrap. Se puede hacer a través de una CDN (Content Delivery Network) o a través de la descarga e importación de los archivos específicos para nuestro proyecto.

- En mi caso decidí hacerlo con CDN pero, si decidieras hacerlo mediante la importación de archivos solo debes integrar la carpeta de boostrap descargada en la ruta ./app/static/lib y en los archivos correspondientes, en la seccion de hoja de estilos o scripts referenciarla mediante el uso de  {{ url_for('static', filename='ruta/archivo') }}
<br></br>
<br></br>
## Trabajando con Formularios
<br></br>
1. Creamos la función de login y los templates correspondientes, así como los estilos de css y los evento javascript.
<br></br>
2. Configuramos el formulario y agregamos los methods del HTTP request.
<br></br>
3. Simulamos una conexión con un usuario y un password a través de un condicional en la función login con el metodo POST; esto para identificar el funcionamiento de los metodos y autorizaciones.
<br></br>
4. Preparándonos para evitar un ataque CSRF instalando Flask-WTF

```sh
pip install Flask-WTF
```

- Ajustamos la clase Config en el archivo config.py para agregar un token.
- Actualizamos la función app_init para que procese el token de seguridad.
- Agregamos un input escondido en nuestro formulario con el metodo csrf_token().
<br></br>
5. Agregamos algunos validadores como el minlength o maxlength al formulario en login.html