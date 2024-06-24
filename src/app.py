from flask import Flask, render_template
# Importamos Flask para comenzar el proyecto. Para instalar flask en la terminal escribir pip install flask

import os
# Importamos os para acceder a los directorios

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# print (template_dir, " y hola mundo")

template_dir = os.path.join(template_dir, "src", "templates")
# Le agregamos los directorios src y templates

# Indicamos que se busque el archivo index.html en la carpeta que indicamos (templates) al ejecutar
app = Flask(__name__, template_folder=template_dir)

# vamos a generar nuestra primer ruta para poder ejecutar
# Ruta de la app
#@app.route('/') es un decorador. El decorador vincula una función específica del sitio web
# la función home() será la encargada de que se ejecute la página principal

# Importante a la primer línea de código (from flask import Flask) agregar render_template

@app.route('/')
def home():
    return render_template('index.html')

# Ejecución directa del archivo, en el puerto 4000 (http://localhost:4000)
if __name__ == '__main__':
    app.run(debug=True, port=4000)

# para ejecutar, dar al botón play arriba a la derecha, en vscode, o
# escribir en la terminal: python.exe .\src\app.py
# para terminar la ejecución, hacer click en la terminal y teclear Ctrl + C
