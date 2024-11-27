from sqlalchemy.orm import Session
from models import Ingrediente
from models import Menu
from models import menu_ingrediente

class MenuCRUD:
    @staticmethod
    def crear_menu(db: Session, nombre: str, descripcion: str, precio: float, ingredientes: list[dict]):
        if not nombre or precio <= 0:
            raise ValueError("Datos inválidos para crear un menú.")
        
        nuevo_menu = Menu(nombre=nombre, descripcion=descripcion, precio=precio)
        db.add(nuevo_menu)
        db.commit()
        
        # Insertar ingredientes en la tabla intermedia
        for ingrediente in ingredientes:
            db.execute(
                menu_ingrediente.insert().values(
                    menu_id=nuevo_menu.id_menu,
                    ingrediente_id=ingrediente['id'],
                    cantidad=ingrediente['cantidad']
                )
            )
        db.commit()
        return nuevo_menu

    @staticmethod
    def leer_menus(db: Session):
        return db.query(Menu).all()

    @staticmethod
    def actualizar_menu(db: Session, id_menu: int, nombre: str = None, descripcion: str = None, precio: float = None):
        menu = db.query(Menu).filter(Menu.id_menu == id_menu).first()
        if not menu:
            raise ValueError(f"Menú con ID {id_menu} no encontrado.")
        
        if nombre:
            menu.nombre = nombre
        if descripcion:
            menu.descripcion = descripcion
        if precio is not None:
            menu.precio = precio
        
        db.commit()
        db.refresh(menu)
        return menu

    @staticmethod
    def borrar_menu(db: Session, id_menu: int):
        menu = db.query(Menu).filter(Menu.id_menu == id_menu).first()
        if not menu:
            raise ValueError(f"Menú con ID {id_menu} no encontrado.")
        
        db.delete(menu)
        db.commit()
        return menu
