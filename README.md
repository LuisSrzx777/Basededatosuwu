<img width="1600" height="900" alt="Captura de pantalla (29)" src="https://github.com/user-attachments/assets/52975033-30d2-42ab-9b60-2f75d108fa4e" />

 
# 📚 Sistema de Gestión de Biblioteca

Este proyecto es una **aplicación de consola en Python** que permite gestionar una biblioteca, incluyendo libros, usuarios y préstamos, utilizando **MySQL** como base de datos.

---

## 🚀 Funcionalidades

- 📘 Registrar, listar y buscar libros.
- 👤 Registrar y listar usuarios.
- 🔁 Registrar préstamos de libros.
- ✅ Devolver libros y actualizar disponibilidad.
- 📄 Ver todos los préstamos o solo los activos.
- Menú interactivo por consola para una navegación intuitiva.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **MySQL** (motor de base de datos relacional)
- **mysql-connector-python** (librería de conexión a MySQL)

---

## 🗃️ Estructura de la base de datos

Asegúrate de tener una base de datos llamada `biblioteca` con las siguientes tablas:

```sql
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    anio INT,
    disponible BOOLEAN DEFAULT TRUE
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50)
);

CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_libro INT,
    fecha_prestamo DATE,
    fecha_devolucion DATE DEFAULT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_libro) REFERENCES libros(id)
);

Dependencias faltantes
pip install mysql-connector-python
