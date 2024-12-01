from sqlalchemy.orm import Session
from models import Ingrediente

class IngredienteCRUD:
    @staticmethod
    def crear_ingrediente(db: Session, nombre: str, tipo: str, cantidad: float, unidad: str):

        if not nombre or not tipo:

            raise ValueError("El nombre y el tipo del ingrediente son obligatorios.")

        if cantidad <= 0:

            raise ValueError("La cantidad debe ser mayor a cero.")

        ingrediente_existente = db.query(Ingrediente).filter(Ingrediente.nombre == nombre).first()

        if ingrediente_existente:

            raise ValueError(f"El ingrediente '{nombre}' ya existe.")

        nuevo_ingrediente = Ingrediente(nombre=nombre, tipo=tipo, cantidad=cantidad, unidad=unidad)

        db.add(nuevo_ingrediente)

        db.commit()

        db.refresh(nuevo_ingrediente)

        return nuevo_ingrediente



    @staticmethod

    def leer_ingredientes(db: Session):

        return db.query(Ingrediente).all()



    @staticmethod

    def actualizar_ingrediente(db: Session, id_ingrediente: int, nombre: str = None, tipo: str = None, cantidad: float = None, unidad: str = None):

        ingrediente = db.query(Ingrediente).filter(Ingrediente.id_ingrediente == id_ingrediente).first()

        if not ingrediente:

            raise ValueError(f"Ingrediente con ID {id_ingrediente} no encontrado.")

        if nombre:

            ingrediente.nombre = nombre

        if tipo:

            ingrediente.tipo = tipo

        if cantidad is not None:

            if cantidad <= 0:

                raise ValueError("La cantidad debe ser mayor a cero.")

            ingrediente.cantidad = cantidad

        if unidad:

            ingrediente.unidad = unidad

        db.commit()

        db.refresh(ingrediente)

        return ingrediente



    @staticmethod
    def borrar_ingrediente(db: Session, id_ingrediente: int):
        ingrediente = db.query(Ingrediente).filter(Ingrediente.id_ingrediente == id_ingrediente).first()
        if not ingrediente:
            raise ValueError(f"Ingrediente con ID {id_ingrediente} no encontrado.")
        db.delete(ingrediente)
        db.commit()
        return ingrediente