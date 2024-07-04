from flask import Flask, render_template, request, redirect, url_for
# Importamos Flask para comenzar el proyecto. Para instalar flask en la terminal escribir pip install flask

import os
# Importamos os para acceder a los directorios

import database as db
# Importamos la conexión a base de datos con alias db

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

@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/cineytv')
def cineytv():
    return render_template('cineytv.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/foro', methods=['GET'])
def foro():
    return render_template('foro.html')

@app.route('/usuarios', methods=['GET'])
def usuarios():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM usuarios")
    miResultado = cursor.fetchall()
    # Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for registro in miResultado:
        insertObject.append(dict(zip(columnNames, registro)))
    cursor.close() # Es una buena práctica cerrar los cursores luego de usarlos

    return render_template('usuarios.html', data=insertObject)

# Ruta para guardar usuarios en la base de datos.
@app.route('/alta_usuario', methods=['POST'])
def addUser():
    user_mail = request.form['mail']
    user_name = request.form['nombre']
    user_pass = request.form['clave']

    if user_mail and user_name and user_pass:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuarios (mail, nombre, clave) VALUES (%s, %s, %s)"
        data = (user_mail, user_name, user_pass)

        # hay que ejecutar la consulta y luego hacer el commit
        cursor.execute(sql, data)
        db.database.commit()
    return redirect (url_for('usuarios'))

# Ruta para borrar usuarios
@app.route('/borrarusuario/<string:id>')
def borrar_usuario(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM usuarios WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect (url_for('usuarios'))

# Ruta para modificar datos
@app.route('/editar_usuario/<string:id>', methods=['POST'])
def editar(id):
    user_mail = request.form['mail']
    user_name = request.form['nombre']
    user_pass = request.form['clave']

    if user_mail and user_name and user_pass:
        cursor = db.database.cursor()
        sql = "UPDATE usuarios SET mail = %s, nombre = %s, clave = %s WHERE id=%s"
        data = (user_mail, user_name, user_pass, id)

        # hay que ejecutar la consulta y luego hacer el commit
        cursor.execute(sql, data)
        db.database.commit()
    return redirect (url_for('usuarios'))


# Ejecución directa del archivo, en el puerto 4000 (http://localhost:4000)
if __name__ == '__main__':
    app.run(debug=True, port=4000)

# para ejecutar, dar al botón play arriba a la derecha, en vscode, o
# escribir en la terminal: python.exe .\src\app.py
# para terminar la ejecución, hacer click en la terminal y teclear Ctrl + C
