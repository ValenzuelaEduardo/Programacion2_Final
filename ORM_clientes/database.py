import sqlite3
from app import *

class BaseDatos:
    def __init__(self, db_path: str = 'restaurante.db'):
        """
        Initialize the database and create all tables if they don't exist.
        
        Args:
            db_path (str): Path to the SQLite database file
        """
        self.db_path = db_path
        self._create_tables()

    def _create_tables(self):
        """
        Create all necessary tables if they don't exist.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            
            # Crear tabla de menús
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS menus (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    precio REAL NOT NULL,
                    disponible INTEGER NOT NULL DEFAULT 1
                )
            ''')

            # Crear tabla pedidos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id INTEGER NOT NULL,
                    menu_id INTEGER NOT NULL,
                    total REAL NOT NULL,
                    fecha TEXT NOT NULL,
                    FOREIGN KEY (cliente_id) REFERENCES clientes (id),
                    FOREIGN KEY (menu_id) REFERENCES menus (id)
                )
            ''')

            # Crear tabla ingredientes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ingredientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE,
                    tipo TEXT NOT NULL,
                    cantidad REAL NOT NULL,
                    unidad_medida TEXT NOT NULL
                )
            ''')

            # Crear tabla clientes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    correo_electronico TEXT UNIQUE NOT NULL
                )
            ''')

            conn.commit()

if __name__ == "__main__":
    bd = BaseDatos('restaurante.db')
    app=App()
    app.mainloop()
