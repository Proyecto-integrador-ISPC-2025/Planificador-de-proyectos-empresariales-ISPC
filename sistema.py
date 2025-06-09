import os #permite interactuar con el sistema para limpiar la pantalla de consola
import platform #Permite identificar desde que sistema se ejecuta el programa
import hashlib #para poner contraseñas encriptadas
from getpass import getpass #Permite pedir contraseñas al usuario sin que se muestren en pantalla.
from usuario import Usuario
from validaciones import validar_contrasena #Importa la funcion para combrobar si esta cumple los requisitos

def limpiar_pantalla():
    #Limpia la pantalla de la consola
    command = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(command)

class SistemaEnMemoria:
    """
    Gestiona toda la lógica de la aplicación y almacena los datos en memoria.
    """
    def __init__(self):
        self._usuarios = [] # Lista para almacenar los objetos Usuario
        self._usuario_actual = None
        self._next_user_id = 1
        self._crear_admin_por_defecto()

    def _hashear_contrasena(self, contrasena: str) -> str:
        """Hashea la contraseña usando SHA-256."""
        return hashlib.sha256(contrasena.encode('utf-8')).hexdigest()

    def _crear_admin_por_defecto(self):
        """Crea un usuario administrador al iniciar el sistema para poder gestionarlo."""
        admin_pass_hash = self._hashear_contrasena("Admin123")
        admin = Usuario(
            id_usuario=self._next_user_id,
            nombre_usuario="admin",
            email="admin@sistema.com",
            contrasena_hash=admin_pass_hash,
            rol="administrador"
        )
        self._usuarios.append(admin)
        self._next_user_id += 1
        print("INFO: Creado usuario 'admin' con contraseña 'Admin123'")

    def iniciar(self):
        """Inicia el bucle principal de la aplicación."""
        while True:
            self.menu_principal()

    def menu_principal(self):
        limpiar_pantalla()
        print("--- SISTEMA DE GESTIÓN DE USUARIOS ---")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            self.registrar_usuario()
        elif opcion == '2':
            self.iniciar_sesion()
        elif opcion == '3':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            exit()
        else:
            print("Opción no válida.")
            input("\nPresione Enter para continuar...")

    def registrar_usuario(self):
        limpiar_pantalla()
        print("--- REGISTRO DE NUEVO USUARIO ---")
        nombre_usuario = input("Ingrese nombre de usuario: ")

        if any(u.nombre_usuario == nombre_usuario for u in self._usuarios):
            print("\nError: El nombre de usuario ya existe.")
            input("\nPresione Enter para continuar...")
            return

        email = input("Ingrese su email: ")
        
        while True:
            contrasena = getpass("Contraseña (mín. 6 chars, letras y números): ")
            if validar_contrasena(contrasena):
                break
            else:
                print("Error: La contraseña no cumple los requisitos.")
        
        nuevo_usuario = Usuario(
            id_usuario=self._next_user_id,
            nombre_usuario=nombre_usuario,
            email=email,
            contrasena_hash=self._hashear_contrasena(contrasena),
            rol="estandar"
        )
        self._usuarios.append(nuevo_usuario)
        self._next_user_id += 1
        
        print("\n¡Usuario registrado con éxito!")
        input("\nPresione Enter para volver al menú principal...")

    def iniciar_sesion(self):
        limpiar_pantalla()
        print("--- INICIO DE SESIÓN ---")
        nombre_usuario = input("Usuario: ")
        contrasena = getpass("Contraseña: ")
        contrasena_hash = self._hashear_contrasena(contrasena)

        usuario_encontrado = None
        for u in self._usuarios:
            if u.nombre_usuario == nombre_usuario and u.contrasena_hash == contrasena_hash:
                usuario_encontrado = u
                break
        
        if usuario_encontrado:
            self._usuario_actual = usuario_encontrado
            print(f"\n¡Inicio de sesión exitoso! Bienvenido, {self._usuario_actual.nombre_usuario}.")
            input("\nPresione Enter para continuar...")
            if self._usuario_actual.rol == 'administrador':
                self.menu_administrador()
            else:
                self.menu_estandar()
        else:
            print("\nError: Usuario o contraseña incorrectos.")
            input("\nPresione Enter para continuar...")
    
    def menu_administrador(self):
        # ... (El resto de los métodos del menú del administrador, solo se entra a este menu 
        #a usuario: admin contraseña:Admin123)
        while self._usuario_actual:
            limpiar_pantalla()
            print(f"--- MENÚ DE ADMINISTRADOR: {self._usuario_actual.nombre_usuario} ---")
            print("1. Ver listado de todos los usuarios")
            print("2. Cambiar rol de un usuario")
            print("3. Eliminar un usuario")
            print("4. Cerrar Sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == '1': self.ver_todos_los_usuarios()
            elif opcion == '2': self.cambiar_rol_usuario()
            elif opcion == '3': self.eliminar_usuario()
            elif opcion == '4':
                self._usuario_actual = None
                print("Sesión cerrada.")
                input("\nPresione Enter para volver...")
                break
            else:
                print("Opción no válida.")
                input("\nPresione Enter para continuar...")

    def ver_todos_los_usuarios(self):
        limpiar_pantalla()
        print("--- LISTADO DE USUARIOS REGISTRADOS ---")
        print(f"{'ID':<5} {'NOMBRE DE USUARIO':<25} {'EMAIL':<30} {'ROL':<15}")
        print("-" * 75)
        for user in self._usuarios:
            print(f"{user.id_usuario:<5} {user.nombre_usuario:<25} {user.email:<30} {user.rol:<15}")
        input("\nPresione Enter para volver al menú...")

    def cambiar_rol_usuario(self):
        try:
            id_usuario = int(input("Ingrese el ID del usuario a modificar: "))
            usuario_a_modificar = next((u for u in self._usuarios if u.id_usuario == id_usuario), None)

            if not usuario_a_modificar: print("Error: No se encontró un usuario con ese ID.")
            elif usuario_a_modificar.id_usuario == self._usuario_actual.id_usuario: print("Error: No puede cambiar su propio rol.")
            else:
                nuevo_rol = input("Ingrese el nuevo rol ('administrador' o 'estandar'): ").lower()
                if nuevo_rol in ['administrador', 'estandar']:
                    usuario_a_modificar.rol = nuevo_rol
                    print("¡Rol actualizado con éxito!")
                else: print("Error: Rol no válido.")
        except ValueError: print("Error: El ID debe ser un número.")
        input("\nPresione Enter para continuar...")

    def eliminar_usuario(self):
        try:
            id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
            usuario_a_eliminar = next((u for u in self._usuarios if u.id_usuario == id_usuario), None)

            if not usuario_a_eliminar: print("Error: No se encontró un usuario con ese ID.")
            elif usuario_a_eliminar.id_usuario == self._usuario_actual.id_usuario: print("Error: No puede eliminarse a sí mismo.")
            else:
                confirmacion = input(f"¿Seguro que desea eliminar a {usuario_a_eliminar.nombre_usuario}? (s/n): ").lower()
                if confirmacion == 's':
                    self._usuarios.remove(usuario_a_eliminar)
                    print("¡Usuario eliminado con éxito!")
                else: print("Operación cancelada.")
        except ValueError: print("Error: El ID debe ser un número.")
        input("\nPresione Enter para continuar...")

    def menu_estandar(self):
        # ... (El resto de los métodos del menú estándar)
        while self._usuario_actual:
            limpiar_pantalla()
            print(f"--- MENÚ DE USUARIO: {self._usuario_actual.nombre_usuario} ---")
            print("1. Ver mis datos personales")
            print("2. Cerrar Sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                print(f"\nNombre de Usuario: {self._usuario_actual.nombre_usuario}")
                print(f"Email: {self._usuario_actual.email}")
                print(f"Rol: {self._usuario_actual.rol}")
                input("\nPresione Enter para volver...")
            elif opcion == '2':
                self._usuario_actual = None
                print("Sesión cerrada.")
                input("\nPresione Enter para volver...")
                break
            else:
                print("Opción no válida.")
                input("\nPresione Enter para continuar...")
