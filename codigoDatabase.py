import mysql.connector
from datetime import date

class ConexionBD:
    def __init__(self):
        try:
            self._conexion = mysql.connector.connect(
                host="localhost", user="root", password="toor", database="biblioteca"
            )
        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
            exit(1)

class Libro:
    def __init__(self, titulo="", autor="", anio=0, disponible=True, id1_libro=0):
        self.__id = id_libro
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__disponible = disponible
    
    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_autor(self): return self.__autor
    def get_anio(self): return self.__anio
    def get_disponible(self): return self.__disponible
    
    def __str__(self):
        disp = "Disponible" if self.__disponible else "Prestado"
        return f"ID: {self.__id}, {self.__titulo} - {self.__autor} ({self.__anio}) [{disp}]"

class Usuario:
    def __init__(self, nombre="", tipo="", id_usuario=0):
        self.__id = id_usuario
        self.__nombre = nombre
        self.__tipo = tipo
    
    def get_id(self): return self.__id
    def get_nombre(self): return self.__nombre
    def get_tipo(self): return self.__tipo
    
    def __str__(self):
        return f"ID: {self.__id}, {self.__nombre} ({self.__tipo})"

class Biblioteca:
    def __init__(self):
        self.conexion_bd = ConexionBD()
        self.conexion = self.conexion_bd._conexion

    def registrar_libro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        anio = int(input("Año: "))
        
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO libros (titulo, autor, anio, disponible) VALUES (%s, %s, %s, %s)", 
                      (titulo, autor, anio, True))
        self.conexion.commit()
        print(f"Libro '{titulo}' registrado (ID: {cursor.lastrowid})")
        cursor.close()

    def listar_libros(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM libros")
        for libro in cursor.fetchall():
            print(Libro(libro[1], libro[2], libro[3], libro[4], libro[0]))
        cursor.close()

    def buscar_libro(self):
        criterio = input("Buscar por (1)Título (2)Autor: ")
        termino = input("Término: ")
        
        cursor = self.conexion.cursor()
        if criterio == "1":
            cursor.execute("SELECT * FROM libros WHERE titulo LIKE %s", (f"%{termino}%",))
        else:
            cursor.execute("SELECT * FROM libros WHERE autor LIKE %s", (f"%{termino}%",))
        
        for libro in cursor.fetchall():
            print(Libro(libro[1], libro[2], libro[3], libro[4], libro[0]))
        cursor.close()

    def registrar_usuario(self):
        nombre = input("Nombre: ")
        tipo = input("Tipo: ")
        
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, tipo) VALUES (%s, %s)", (nombre, tipo))
        self.conexion.commit()
        print(f"Usuario '{nombre}' registrado (ID: {cursor.lastrowid})")
        cursor.close()

    def listar_usuarios(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        for usuario in cursor.fetchall():
            print(Usuario(usuario[1], usuario[2], usuario[0]))
        cursor.close()

    def registrar_prestamo(self):
        id_usuario = int(input("ID Usuario: "))
        id_libro = int(input("ID Libro: "))
        
        cursor = self.conexion.cursor()
        
        # Verificar libro disponible
        cursor.execute("SELECT disponible FROM libros WHERE id = %s", (id_libro,))
        libro = cursor.fetchone()
        if not libro or not libro[0]:
            print("Libro no disponible")
            cursor.close()
            return
        
        # Registrar préstamo
        cursor.execute("INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo) VALUES (%s, %s, %s)", 
                      (id_usuario, id_libro, date.today()))
        
        # Marcar libro como no disponible
        cursor.execute("UPDATE libros SET disponible = FALSE WHERE id = %s", (id_libro,))
        
        self.conexion.commit()
        print("Préstamo registrado exitosamente")
        cursor.close()

    def devolver_libro(self):
        id_prestamo = int(input("ID Préstamo: "))
        
        cursor = self.conexion.cursor()
        
        # Obtener ID del libro
        cursor.execute("SELECT id_libro FROM prestamos WHERE id = %s", (id_prestamo,))
        resultado = cursor.fetchone()
        if not resultado:
            print("Préstamo no encontrado")
            cursor.close()
            return
        
        id_libro = resultado[0]
        
        # Registrar devolución
        cursor.execute("UPDATE prestamos SET fecha_devolucion = %s WHERE id = %s", 
                      (date.today(), id_prestamo))
        
        # Marcar libro como disponible
        cursor.execute("UPDATE libros SET disponible = TRUE WHERE id = %s", (id_libro,))
        
        self.conexion.commit()
        print("Libro devuelto exitosamente")
        cursor.close()

    def listar_prestamos(self):
        opcion = input("Mostrar (1)Todos (2)Activos: ")
        
        cursor = self.conexion.cursor()
        if opcion == "2":
            query = """SELECT p.id, u.nombre, l.titulo, p.fecha_prestamo 
                      FROM prestamos p 
                      JOIN usuarios u ON p.id_usuario = u.id 
                      JOIN libros l ON p.id_libro = l.id 
                      WHERE p.fecha_devolucion IS NULL"""
        else:
            query = """SELECT p.id, u.nombre, l.titulo, p.fecha_prestamo, p.fecha_devolucion 
                      FROM prestamos p 
                      JOIN usuarios u ON p.id_usuario = u.id 
                      JOIN libros l ON p.id_libro = l.id"""
        
        cursor.execute(query)
        for prestamo in cursor.fetchall():
            estado = "Activo" if prestamo[4] is None else f"Devuelto: {prestamo[4]}"
            print(f"ID: {prestamo[0]}, Usuario: {prestamo[1]}, Libro: {prestamo[2]}, Préstamo: {prestamo[3]}, Estado: {estado}")
        cursor.close()

    def menu_principal(self):
        while True:
            print("\n=== BIBLIOTECA ===")
            print("1. Libros")
            print("2. Usuarios") 
            print("3. Préstamos")
            print("4. Salir")
            
            opcion = input("Opción: ")
            
            if opcion == "1":
                self.menu_libros()
            elif opcion == "2":
                self.menu_usuarios()
            elif opcion == "3":
                self.menu_prestamos()
            elif opcion == "4":
                break

    def menu_libros(self):
        while True:
            print("\n--- LIBROS ---")
            print("1. Registrar")
            print("2. Listar")
            print("3. Buscar")
            print("4. Volver")
            
            opcion = input("Opción: ")
            if opcion == "1": self.registrar_libro()
            elif opcion == "2": self.listar_libros()
            elif opcion == "3": self.buscar_libro()
            elif opcion == "4": break

    def menu_usuarios(self):
        while True:
            print("\n--- USUARIOS ---")
            print("1. Registrar")
            print("2. Listar")
            print("3. Volver")
            
            opcion = input("Opción: ")
            if opcion == "1": self.registrar_usuario()
            elif opcion == "2": self.listar_usuarios()
            elif opcion == "3": break

    def menu_prestamos(self):
        while True:
            print("\n--- PRÉSTAMOS ---")
            print("1. Registrar préstamo")
            print("2. Devolver libro")
            print("3. Listar préstamos")
            print("4. Volver")
            
            opcion = input("Opción: ")
            if opcion == "1": self.registrar_prestamo()
            elif opcion == "2": self.devolver_libro()
            elif opcion == "3": self.listar_prestamos()
            elif opcion == "4": break

if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.menu_principal()
