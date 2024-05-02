print("Bienvenidos, elija una opción.")

inicio = ["A)_ Registrar usuario.", "B)_ Ver los usuarios ingresados.",
"C)_ Mostrar listado de ingreso", "D)_ Iniciar Sesión","E)_ Finalizar tarea"]

datos = []
id = 0 

def new_user():
    global id  
    if opcion_usuario.lower() == "a":
        cant_registro = int(input("¿Cuántos registros quieres ingresar?: "))
        for _ in range(cant_registro):
            usuario = input('Coloque su usuario: ')
            contraseña = input('Coloque su contraseña: ')
            id += 1  
            datos.append({
                'ID': id,
                'Nombre': usuario,
                'Contraseña': contraseña
            })
        
        print("Ingresaste los datos correctamente")
    return datos  

def show_user(user_id):
    for registro in datos:
        if registro['ID'] == user_id:
            print(registro)
            break
    else:
        print("No existe ese ID, prueba con otro.")

def list_users():
    if not datos:
        print("No hay registros ingresados.")
    else:
        for registros in datos:
            print(dict(registros))


def login():
    usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    
    for registro in datos:
        if registro['Nombre'] == usuario and registro['Contraseña'] == contraseña:
            print("Inicio de sesión exitoso.")
            return True
    else:
        print("Usuario o contraseña incorrectos.")
        return False



def finished():
    print("Finalizando tarea. ¡Hasta luego!")

while True:
    for opcion in inicio:
        print(opcion)
    opcion_usuario = input("Ingresa una opción por favor: ")

    if opcion_usuario.lower() == "a":
        new_user()
    elif opcion_usuario.lower() == "b":
        id_ver_usuario = int(input("Ingresa el ID del usuario que quieras ver: "))
        show_user(id_ver_usuario)
    elif opcion_usuario.lower() == "c":
        list_users()
    elif opcion_usuario.lower() == "d":
        login()
    elif opcion_usuario.lower() == "e":
        finished()
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida (A, B, C, D, E, F).")

