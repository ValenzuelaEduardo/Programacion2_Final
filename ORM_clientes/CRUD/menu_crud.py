import sqlite3
from typing import List, Tuple, Optional

class MenuCRUD:
    def __init__(self, db_path: str = 'restaurante.db'):
        """
        Initialize the MenuCRUD with a database connection.
        
        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path

    def crear_menu(self, nombre: str, descripcion: str, precio: float, disponible: int = 1) -> int:
        """
        Create a new menu in the database.
        
        Args:
            nombre (str): Menu name.
            descripcion (str): Description of the menu.
            precio (float): Price of the menu.
            disponible (int): Availability status (1 for available, 0 for unavailable).
        
        Returns:
            int: ID of the newly created menu.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO menus (nombre, descripcion, precio, disponible)
                VALUES (?, ?, ?, ?)
            ''', (nombre, descripcion, precio, disponible))
            conn.commit()
            return cursor.lastrowid

    def listar_menus(self) -> List[Tuple[int, str, str, float, int]]:
        """
        List all menus in the database.
        
        Returns:
            List[Tuple[int, str, str, float, int]]: List of menu details.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, nombre, descripcion, precio, disponible FROM menus')
            return cursor.fetchall()

    def obtener_menu(self, id: int) -> Optional[Tuple[int, str, str, float, int]]:
        """
        Retrieve a menu by its ID.
        
        Args:
            id (int): Menu ID.
        
        Returns:
            Optional[Tuple[int, str, str, float, int]]: Menu details or None if not found.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, nombre, descripcion, precio, disponible FROM menus WHERE id = ?', (id,))
            return cursor.fetchone()

    def actualizar_menu(self, id: int, nombre: str = None, descripcion: str = None, precio: float = None, disponible: int = None):
        """
        Update menu information.
        
        Args:
            id (int): Menu ID.
            nombre (str, optional): New name.
            descripcion (str, optional): New description.
            precio (float, optional): New price.
            disponible (int, optional): New availability status.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            updates = []
            params = []

            if nombre:
                updates.append('nombre = ?')
                params.append(nombre)
            
            if descripcion:
                updates.append('descripcion = ?')
                params.append(descripcion)
            
            if precio:
                updates.append('precio = ?')
                params.append(precio)
            
            if disponible is not None:
                updates.append('disponible = ?')
                params.append(disponible)
            
            if updates:
                query = f'UPDATE menus SET {", ".join(updates)} WHERE id = ?'
                params.append(id)
                cursor.execute(query, tuple(params))
                conn.commit()

    def eliminar_menu(self, id: int):
        """
        Delete a menu from the database.
        
        Args:
            id (int): Menu ID.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM menus WHERE id = ?', (id,))
            conn.commit()
