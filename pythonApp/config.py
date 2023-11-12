import mysql.connector

try:
    midb = mysql.connector.connect(
        user="root", password="", host="localhost", port=3306, database="notas_bd"
    )
    print("Conexion exitosa")
except Exception as err:
    print(f"Error en la conexion, {err}")



# Funcion para agregar usuario a la tabla usuario
def agregar_user(nombre, email, password):
    cursor = midb.cursor()
    sql = f"INSERT INTO usuario (nombre,email,password) VALUES('{nombre}','{email}','{password}')"
    cursor.execute(sql)
    midb.commit()
    return "Usuario agregado"

#agregar_user('Hilda Castillo', 'hilda@mail.com', 'Hilda11')
# agregar_usuario("Martha Bermudez", "martha@mail.com", "123")

# agregar_usuario('Fernando Argueta', 'fernando@mail.com', 'ferdrake')

def login_user(email):
    cursor = midb.cursor()
    sql = f"SELECT * FROM usuario WHERE email = '{email}'"
    cursor.execute(sql)
    usuario = cursor.fetchone()
    user = usuario
    return user

# Funcion mostrar usuario
def listar_notas(email):
        cursor = midb.cursor()
        sql = f"SELECT * FROM notas  WHERE usuario_email = '{email}'"
        cursor.execute(sql)
        notas = cursor.fetchall()
        return notas


#print(mostrar_usuario('martha@mail.com'))


# Crear nueva nota en la tabla nota
def crear_nota(usuario_email, titulo, contenido):
    cursor = midb.cursor()
    sql = f"INSERT INTO notas (usuario_email, titulo, contenido) VALUES ('{usuario_email}','{titulo}','{contenido}')"
    cursor.execute(sql)
    midb.commit()
    print("Nota agregada con exito")
    return "Nota agregada"

#crear_nota('fernando@mail.com','La robotica en el 2023','Esto es el contenido de  anota python y la robotica')
#crear_nota('Alexis@mail.com','Las IA en el 2023','Esto es el contenido de una nota python y la IA')

# Funcion para eliminar una nota en la tabla notas

def eliminar_nota(id):
    cursor = midb.cursor()
    sql = f"DELETE FROM notas WHERE id = {id}"
    cursor.execute(sql)
    midb.commit()
    print("Nota eliminada con exito")
    return "Nota Eliminada"


#eliminar_nota(1)


# Mostrar las notas agregadas
"""def mostrar_notas():
    cursor = midb.cursor()
    sql = "SELECT * FROM notas"
    cursor.execute(sql)
    notas = cursor.fetchall()
    #print(notas)
    return notas

 #print(mostrar_notas())"""


# editar las notas
def editar_nota(id):
    cursor = midb.cursor()
    sql = f"SELECT * FROM notas WHERE id = '{id}'"
    cursor.execute(sql)
    nota = cursor.fetchone()
    return  nota


#actualizar_nota(2,'Las nuevas TICs','Contenido actualizado desde la funcion')

def actualizar_nota(id, titulo, contenido):
    cursor = midb.cursor()
    sql = f"UPDATE notas SET titulo = '{titulo}', contenido = '{contenido}' WHERE id = {id}"
    cursor.execute(sql)
    midb.commit()
    return "Nota actualizada"



#editar_nota(2,'Las nuevas TICs','Contenido actualizado desde la funcion')
