# Entrega Final Comision 56065

## Nombre

- Andres Ramirez
- [Perfil de LinkedIn](https://www.linkedin.com/in/aramirezaliste/)
- [Perfil de Github](https://github.com/aramirezaliste/)

##  Resumen del Proyecto

- Simulando un blog de musica con framework Django, Bootstrap
- [Link a Youtube]()

## Pasos para ejecutar el proyecto

- [Link de Github](https://github.com/aramirezaliste/PlaygroundFinalProject-Ramirez)
- Clonar proyecto
- Instalar dependencias
        - Dependencias ocupadas (Listadas en requeriments.txt)

- Para instalar las dependencias utilizadas en el proyecto:
    - Crear un entorno virtual de python
        Linux/Mac
        ```
            $ python3 -m venv .venv
        ```
        Windows
        ```
            $ python -m venv .venv
        ```
    - Activar el entorno virtual
        Linux/Mac
        ```
            $ source .venv/bin/activate
        ```
        Windows
        ```
            $ .\.venv\Scripts\activate
        ```
    - Instalar paquete desde requeriments.txt
         ```
            $ pip3 install -r requirements.txt
        ```

- Como ejecutar la aplicacion web en el servidor local
    Despues de instalar las dependecias requeridas,
    En la terminal dirigirse a la carpeta donde se encuentra manage.py
    y ejecutar el siguiente codigo.

    - Para crear la base de datos local
        ```
            $ python3 manage.py migrate
        ```
    - Para ejecutar el servidor local
        ```
            $ python3 manage.py runserver
        ```
