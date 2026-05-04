# Entrega3-Arzamendia-Python

Proyecto web desarrollado en Django para la tercera entrega: **Tu primera página**.

## Tema del proyecto

Blog musical dedicado a la banda argentina de rock **Airbag**.

## Requisitos cumplidos

- Proyecto Web Django con patrón MVT.
- Herencia de plantillas HTML mediante `base.html`.
- Tres clases en `models.py`: `Post`, `Integrante` y `Album`.
- Un formulario para insertar datos en cada modelo.
- Un formulario para buscar publicaciones en la base de datos.
- Botón para eliminar publicaciones con confirmación previa.
- README con el orden de prueba de funcionalidades.

## Cómo ejecutar el proyecto

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Abrir en el navegador:

```txt
http://127.0.0.1:8000/
```

## Orden recomendado para probar

1. Inicio: `http://127.0.0.1:8000/`
2. Crear publicación: `http://127.0.0.1:8000/crear-post/`
3. Crear integrante: `http://127.0.0.1:8000/crear-integrante/`
4. Crear álbum: `http://127.0.0.1:8000/crear-album/`
5. Buscar publicación: `http://127.0.0.1:8000/buscar/`
6. Eliminar publicación: desde el botón **Eliminar** de cada post en la página de inicio.
7. Acerca del proyecto: `http://127.0.0.1:8000/acerca/`

## Funcionalidades principales

- **Inicio:** muestra publicaciones cargadas.
- **Crear Post:** permite cargar publicaciones del blog.
- **Crear Integrante:** permite registrar integrantes de la banda.
- **Crear Álbum:** permite registrar álbumes musicales.
- **Buscar Post:** permite buscar publicaciones por título.
- **Eliminar Post:** permite borrar publicaciones desde la web con confirmación.

## Autor

Entrega realizada por Arzamendia.



# Entrega 3 - Blog Musical Airbag

Proyecto web desarrollado en Django utilizando el patrón MVT.

## Funcionalidades

- Crear publicaciones (Posts)
- Crear integrantes
- Crear álbumes
- Buscar publicaciones
- Eliminar publicaciones

## Cómo ejecutar el proyecto

1. Crear entorno virtual:
   py -m venv venv

2. Activar entorno:
   .\venv\Scripts\Activate

3. Instalar dependencias:
   pip install -r requirements.txt

4. Migraciones:
   python manage.py migrate

5. Ejecutar servidor:
   python manage.py runserver

6. Abrir en navegador:
   http://127.0.0.1:8000/

## Rutas principales

- / → Inicio
- /crear-post/ → Crear publicaciones
- /crear-integrante/ → Crear integrantes
- /crear-album/ → Crear álbumes
- /buscar/ → Buscar publicaciones