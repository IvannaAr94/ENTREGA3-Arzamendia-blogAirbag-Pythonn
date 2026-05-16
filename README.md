# Proyecto Final Python/Django - Blog Musical Airbag

Proyecto web desarrollado en **Python + Django** como entrega final del curso.  
La aplicación es un blog musical dedicado a la banda argentina **Airbag**, con publicaciones, integrantes, álbumes, usuarios, perfiles y mensajería interna.

---

# Repositorio

- GitHub: https://github.com/IvannaAr94/ENTREGAFINAL-Arzamendia-BlogAirbag-Python-Django
  
-En la carpeta esta el VIDEO.

-ONEDRIVE: https://1drv.ms/f/c/1ee7f3dd5a9dfa96/IgD3Eq18_hiZQpREmNyhrYf1AX6tfcySZZMt8N4RT_Ignd4?e=SDsfow 
---

# Funcionalidades principales

- Home del sitio.
- Vista **Acerca de mí / About** en `/about/`.
- Vista de listado de publicaciones en `/pages/`.
- Detalle de cada publicación mediante el botón **Leer más**.
- Mensaje visible si no hay páginas creadas o si una búsqueda no devuelve resultados.
- Creación, edición y eliminación de publicaciones protegidas para usuarios logueados.
- Registro de usuarios con username, email y password.
- Login y logout.
- Perfil de usuario con nombre, apellido, email, avatar, biografía, link y fecha de nacimiento.
- Edición de perfil y cambio de contraseña.
- App de mensajería para enviar y recibir mensajes entre usuarios.
- Sección de integrantes.
- Sección de álbumes con imagen, año y descripción.
- Panel de administración de Django.
- Uso de herencia de templates desde `base.html`.
- Uso de vistas basadas en clases, mixins y decoradores.
- Formulario con imagen y editor enriquecido mediante CKEditor CDN.

---

# Apps del proyecto

## `blog`
Maneja:
- home
- about
- pages
- detalle de publicaciones
- creación
- edición
- eliminación
- integrantes
- álbumes

## `accounts`
Maneja:
- registro
- login
- logout
- perfil
- edición de perfil
- cambio de contraseña

## `messenger`
Maneja:
- mensajes entre usuarios

---

# Requisitos técnicos cumplidos

- Proyecto individual en Django.
- Herencia de templates.
- Navbar implementada en `base.html`.
- Archivo `.gitignore` configurado para excluir:
  - `__pycache__/`
  - `*.py[cod]`
  - `db.sqlite3`
  - `media/`
  - `venv/`
  - `.env`
- Archivo `requirements.txt` actualizado.
- Modelo principal `Post` con:
  - `titulo` → CharField
  - `subtitulo` → CharField
  - `contenido` → TextField
  - `imagen` → ImageField
  - `fecha` → DateField
- Uso de vistas basadas en clases:
  - `PageListView`
  - `PageDetailView`
  - `PageCreateView`
  - `PageUpdateView`
  - `PageDeleteView`
- Uso de mixin:
  - `LoginRequiredMixin`
- Uso de decorador:
  - `@login_required`
- Modelos registrados en admin:
  - `Post`
  - `Integrante`
  - `Album`
  - `Profile`
  - `Message`

---

# Cómo ejecutar el proyecto


## 1. Clonar el repositorio

```bash
git clone https://github.com/IvannaAr94/ENTREGAFINAL-Arzamendia-BlogAirbag-Python-Django.git
```

## 2. Ingresar a la carpeta del proyecto

```bash
cd ENTREGAFINAL-Arzamendia-BlogAirbag-Python-Django
```

## 3. Crear entorno virtual

```bash
py -m venv venv
```

## 4. Activar entorno virtual

### PowerShell

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

### CMD

```cmd
venv\Scripts\activate.bat
```

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 6. Aplicar migraciones

```bash
python manage.py migrate
```

## 7. Crear superusuario

```bash
python manage.py createsuperuser
```

## 8. Ejecutar servidor

```bash
python manage.py runserver
```

## 9. Abrir el proyecto en el navegador

```txt
http://127.0.0.1:8000/
```

## Panel de administración Django

```txt
http://127.0.0.1:8000/admin/
```
