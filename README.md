<img width="1600" height="900" alt="Captura de pantalla (29)" src="https://github.com/user-attachments/assets/52975033-30d2-42ab-9b60-2f75d108fa4e" />
# 📚 Sistema de Gestión de Biblioteca en Python

Este es un sistema de gestión de biblioteca desarrollado en Python que permite registrar libros y usuarios, gestionar préstamos y devoluciones, y consultar información almacenada en una base de datos MySQL.

## 🚀 Características

- Registro de libros y usuarios.
- Búsqueda de libros por título o autor.
- Registro y devolución de préstamos.
- Consulta de préstamos activos o históricos.
- Menús interactivos por consola.

## 🛠️ Requisitos

- Python 3.6 o superior
- MySQL Server
- Biblioteca `mysql-connector-python`

Instalación del conector MySQL para Python:

```bash
pip install mysql-connector-python
🗃️ Estructura de la Base de Datos
Asegúrate de crear una base de datos llamada biblioteca con las siguientes tablas:

CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    autor VARCHAR(255),
    anio INT,
    disponible BOOLEAN
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    tipo VARCHAR(100)
);

CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_libro INT,
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_libro) REFERENCES libros(id)
);

⚙️ Configuración
Modifica la clase ConexionBD si tus credenciales de base de datos son diferentes:

python
Copiar código
self._conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="biblioteca"
)

📂 Estructura del Código
ConexionBD: Maneja la conexión con MySQL.

Libro, Usuario: Modelos para representar los objetos del sistema.

Biblioteca: Clase principal que contiene los menús y la lógica del programa.

menu_principal(): Punto de entrada para interactuar con el sistema desde consola.

