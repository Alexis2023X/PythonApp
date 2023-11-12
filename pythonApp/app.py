#app.py
from flask import Flask, render_template, request, url_for, redirect, session
from config import (
    midb,
    login_user,
    listar_notas,
    crear_nota,
    eliminar_nota,
    editar_nota,
    actualizar_nota,
    agregar_user,
    #mostrar_notas
)

app = Flask(__name__)
app.secret_key = 'clave secreta' #Para la seguridad de la app tienes que poner una clave fuerte


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/usuario")
def usuario():
    return render_template("registro.html")


@app.route("/nuevo_usuario", methods=["POST", "GET"])
def nuevo_usuario():
    try:
        if request.method == "POST":
            nombre = request.form["nombre"]
            email = request.form["email"]
            password = request.form["password"]
            agregar_user(nombre, email, password)
            return redirect(url_for("home"))
    except Exception as err:
        print(err)
        return redirect(url_for("home"))


@app.route("/login", methods=["POST", "GET"])
def login():
    try:
        email = request.form["email"]
        password = request.form["password"]
        usuario = login_user(email)
        if email == usuario[2] and password == usuario[3]:
            session["user"] = usuario[2]
            session["nombre"] = usuario[1]
        return redirect(url_for("listar"))
    except Exception as err:
        print(err)
        return redirect(url_for("home"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.route("/listar")
def listar():
    try:
        if session["user"] != None:
            usuario_db = session["user"]
            notas = listar_notas(usuario_db)
            return render_template(
                "listar_notas.html", nombre=session["nombre"], notas=notas
            )
    except:
        return redirect(url_for("home"))

@app.route("/ruta_nueva")
def ruta_nueva():
    return render_template("nueva_nota.html")

##############################
@app.route("/acerca_nota")
def acerca_nota():
    return render_template("acerca_notas.html")
##############################

@app.route("/crear", methods=["POST", "GET"])
def crear():
    if request.method == "POST":
        usuario = session["user"]
        titulo = request.form["titulo"]
        contenido = request.form["contenido"]
    try:
        crear_nota(usuario, titulo, contenido)
        return redirect(url_for("listar"))
    except Exception as err:
     print(err)


@app.route("/editar/<int:id>")
def editar(id):
    nota = editar_nota(id)
    #print(nota)
    return render_template("editar_nota.html", nota=nota)


@app.route("/actualizar/<id>", methods=["POST", "GET"])
def actualizar(id):
    if request.method == "POST":
        titulo = request.form["titulo"]
        contenido = request.form["contenido"]
    try:
        actualizar_nota(id, titulo, contenido)
        print("Dato actualizado")
        return redirect(url_for("listar"))
    except Exception as err:
        print(err)



@app.route("/eliminar/<int:id>")
def eliminar(id):
    eliminar_nota(id)
    print("Nota eliminada")
    return redirect(url_for("listar"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)


"""

def mostrar_notas():
    notas = notas()
    return notas

@app.route("/mostrar")
def mostrar():
    try:
        if session["titulo"] != None:
            titulo = session["titulo"]
            notas = mostrar_notas()
            return render_template(
                "listar_notas.html", contenido=session["contenido"], notas=notas
            )
    except:
        return redirect(url_for("home"))


@app.route("/listar")
def listar():
    try:
        if session["user"] !=None:
            titulo = session["titulo"]
            notas = listar_notas(usuario_db)
            return render_template(
                "listar_notas.html", contenido=session["contenido"], notas = notas
            )
    except:
        return redirect(url_for("home"))"""