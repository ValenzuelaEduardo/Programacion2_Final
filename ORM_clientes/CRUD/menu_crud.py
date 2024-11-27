<<<<<<< HEAD
=======
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from models import Menu
from typing import Dict, List, Tuple, Optional
>>>>>>> parent of 855b773 (Merge branch 'Renè' into Eduardo)

        session: Session, nombre: str, descripcion: str, precio: float, disponible: int = 1
    ) -> Menu:
        """
        Create a new menu in the database.
        
        Args:
            nombre (str): Menu name.
            descripcion (str): Description of the menu.
            precio (float): Price of the menu.
            disponible (int): Availability status (1 for available, 0 for unavailable).
        
        Returns:
            Menu: The newly created Menu object.
        """
        try:
            nuevo_menu = Menu(
                nombre=nombre, descripcion=descripcion, precio=precio, disponible=disponible
            )
            session.add(nuevo_menu)
            session.commit()
            session.refresh(nuevo_menu)
            return nuevo_menu
        except SQLAlchemyError as e:
            session.rollback()
            raise ValueError(f"Error al guardar el menú: {str(e)}")

    @staticmethod
    def listar_menus(session: Session) -> List[Dict[str, Optional[str]]]:
        """
        List all menus in the database.
        
        Returns:
            List[Dict[str, Optional[str]]]: List of menu details.
        """
        menus = session.query(Menu).all()
        return [
            {
                "id": menu.id,
                "nombre": menu.nombre,
                "descripcion": menu.descripcion,
                "precio": menu.precio,
                "disponible": menu.disponible,
            }
            for menu in menus
        ]

    @staticmethod
    def obtener_menu(session: Session, id: int) -> Optional[Dict[str, Optional[str]]]:
        """
        Retrieve a menu by its ID.
        
        Args:
            id (int): Menu ID.
        
        Returns:
            Optional[Dict[str, Optional[str]]]: Menu details or None if not found.
        """
        menu = session.query(Menu).filter_by(id=id).first()
        if menu:
            return {
                "id": menu.id,
                "nombre": menu.nombre,
                "descripcion": menu.descripcion,
                "precio": menu.precio,
                "disponible": menu.disponible,
            }
        return None

    @staticmethod
    def actualizar_menu(
        session: Session,
        id: int,
        nombre: Optional[str] = None,
        descripcion: Optional[str] = None,
        precio: Optional[float] = None,
        disponible: Optional[int] = None,
    ) -> Menu:
        """
        Update menu information.
        
        Args:
            id (int): Menu ID.
            nombre (str, optional): New name.
            descripcion (str, optional): New description.
            precio (float, optional): New price.
            disponible (int, optional): New availability status.
        
        Returns:
            Menu: The updated Menu object.
        """
        menu = session.query(Menu).filter_by(id=id).first()
        if not menu:
            raise ValueError(f"Menú con ID {id} no encontrado.")
        
        if nombre:
            menu.nombre = nombre
        if descripcion:
            menu.descripcion = descripcion
        if precio:
            menu.precio = precio
        if disponible is not None:
            menu.disponible = disponible
        
        try:
            session.commit()
            session.refresh(menu)
            return menu
        except SQLAlchemyError as e:
            session.rollback()
            raise ValueError(f"Error al actualizar el menú: {str(e)}")

    @staticmethod
    def eliminar_menu(session: Session, id: int) -> Menu:
        """
        Delete a menu from the database.
        
        Args:
            id (int): Menu ID.
        
        Returns:
            Menu: The deleted Menu object.
        """
        menu = session.query(Menu).filter_by(id=id).first()
        if not menu:
            raise ValueError(f"Menú con ID {id} no encontrado.")
        
        try:
            session.delete(menu)
            session.commit()
            return menu
        except SQLAlchemyError as e:
            session.rollback()
            raise ValueError(f"Error al eliminar el menú: {str(e)}")
