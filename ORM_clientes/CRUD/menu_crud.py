from sqlalchemy.orm import Session

from models import Menu, Ingrediente, menu_ingrediente



class MenuCRUD:

    @staticmethod

    def crear_menu(db: Session, nombre: str, descripcion: str, precio: float, ingredientes: list):

        if not nombre or not descripcion:

            raise ValueError("El nombre y la descripción del menú son obligatorios.")

        if precio <= 0:

            raise ValueError("El precio debe ser mayor a cero.")

        menu_existente = db.query(Menu).filter(Menu.nombre == nombre).first()

        if menu_existente:

            raise ValueError(f"El menú '{nombre}' ya existe.")

        nuevo_menu = Menu(nombre=nombre, descripcion=descripcion, precio=precio)

        db.add(nuevo_menu)

        db.commit()

        db.refresh(nuevo_menu)



        for ingrediente in ingredientes:

            ingrediente_obj = db.query(Ingrediente).filter(Ingrediente.id_ingrediente == ingrediente['id']).first()

            if not ingrediente_obj:

                raise ValueError(f"Ingrediente con ID {ingrediente['id']} no encontrado.")

            db.execute(

                menu_ingrediente.insert().values(

                    menu_id=nuevo_menu.id_menu,

                    ingrediente_id=ingrediente_obj.id_ingrediente,

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

            menu_existente = db.query(Menu).filter(Menu.nombre == nombre, Menu.id_menu != id_menu).first()

            if menu_existente:

                raise ValueError(f"Otro menú con el nombre '{nombre}' ya existe.")

            menu.nombre = nombre

        if descripcion:

            menu.descripcion = descripcion

        if precio is not None:

            if precio <= 0:

                raise ValueError("El precio debe ser mayor a cero.")

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
