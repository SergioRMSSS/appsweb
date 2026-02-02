# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def inici():
#     return "hello world y adios"

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/my/secret/page")
def secret_page():
    return "Top secret!"



import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # Usuario por defecto de XAMPP
        password="",        # Contraseña por defecto (vacía)
        database="nom_mail" # Nombre de tu base de datos en la imagen
    )

@app.route("/addmail", methods=['GET', 'POST'])
def registro_usuario():
    mensaje = None
    
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('email')
        
        # Insertar en la base de datos
        db = conectar_db()
        cursor = db.cursor()
        
        sql = "INSERT INTO usuarios (Nombre, Mail) VALUES (%s, %s)"
        valores = (nombre, correo)
        
        cursor.execute(sql, valores)
        db.commit() # Importante para guardar los cambios
        
        cursor.close()
        db.close()
        
        return f"<h3>Usuario {nombre} registrado correctamente en la base de datos.</h3>"
    
    return render_template('addmail.html', mensaje=mensaje)




@app.route("/getmail", methods=['GET', 'POST'])
def buscar_email():
    if request.method == 'POST':
        nombre_buscado = request.form.get('usuario')
        
        db = conectar_db()
        cursor = db.cursor()
        
        # Usamos una consulta SQL para buscar el mail por nombre
        sql = "SELECT Mail FROM usuarios WHERE Nombre = %s"
        cursor.execute(sql, (nombre_buscado,))
        
        resultado = cursor.fetchone()
        
        cursor.close()
        db.close()
        
        if resultado:
            return f"<h3>El correo de {nombre_buscado} es: {resultado[0]}</h3><br><a href='/getmail'>Volver a buscar</a>"
        else:
            return f"<h3>No se encontró ningún usuario con el nombre '{nombre_buscado}'.</h3><br><a href='/getmail'>Reintentar</a>"
    
    # Si es GET, cargamos el formulario de búsqueda
    return render_template('getmail.html')