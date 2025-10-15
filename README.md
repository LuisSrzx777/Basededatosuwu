<img width="1600" height="900" alt="Captura de pantalla (29)" src="https://github.com/user-attachments/assets/52975033-30d2-42ab-9b60-2f75d108fa4e" />

Sistema de Gestión de Biblioteca
Un sistema de gestión de biblioteca desarrollado en Python que permite administrar libros, usuarios y préstamos de manera eficiente.

Características

📚 Gestión de Libros
Registrar nuevos libros

Listar todos los libros disponibles

Buscar libros por título o autor

Control de disponibilidad

👥 Gestión de Usuarios

Registrar nuevos usuarios

Listar usuarios existentes

Clasificación por tipo de usuario

🔄 Gestión de Préstamos

Registrar préstamos de libros

Devolución de libros

Listar préstamos (activos y completos)

Control de fechas de préstamo y devolución

Requisitos del Sistema
Software Requerido
Python 3.6 o superior

MySQL Server

MySQL Connector/Python

Base de Datos
El sistema utiliza MySQL y requiere las siguientes tablas:

sql
CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    anio INT,
    disponible BOOLEAN DEFAULT TRUE
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    tipo VARCHAR(100)
);

CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_libro INT,
    fecha_prestamo DATE,
    fecha_devolucion DATE NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_libro) REFERENCES libros(id)
);
Instalación
Clonar o descargar el proyecto

bash
git clone <url-del-repositorio>
cd biblioteca
Instalar dependencias

bash
pip install mysql-connector-python
Configurar la base de datos

Asegúrate de que MySQL esté ejecutándose

Crea la base de datos y las tablas usando los scripts SQL proporcionados

Configura las credenciales de conexión en la clase ConexionBD:

python
self._conexion = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="biblioteca"
)
Uso
Ejecutar la aplicación
bash
python biblioteca.py


Instala las dependencias:

pip install mysql-connector-python
