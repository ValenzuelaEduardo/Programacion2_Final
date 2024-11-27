<<<<<<< HEAD
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from models import Ingrediente
from typing import List, Dict, Optional

class IngredienteCRUD:
    @staticmethod
    def crear_ingrediente(
        session: Session, nombre: str, tipo: str, cantidad: float, unidad_medida: str
    ) -> Ingrediente:
        """
        Crea un nuevo ingrediente en la base de datos.
        """
        try:
            nuevo_ingrediente = Ingrediente(
                nombre=nombre, tipo=tipo, cantidad=cantidad, unidad_medida=unidad_medida
            )
            session.add(nuevo_ingrediente)
            session.commit()
            session.refresh(nuevo_ingrediente)
            return nuevo_ingrediente
        except IntegrityError:
            session.rollback()
            raise ValueError(f"Error: Ya existe un ingrediente con el nombre '{nombre}'.")
        except SQLAlchemyError as e:
            session.rollback()
            raise ValueError(f"Error al guardar el ingrediente: {str(e)}")

    @staticmethod
    def leer_ingredientes(session: Session, limite: int = 10, offset: int = 0) -> List[Dict[str, Optional[str]]]:
        """
        Lee una lista de ingredientes desde la base de datos.
        """
        ingredientes = session.query(Ingrediente).offset(offset).limit(limite).all()
        return [
            {
                "id_ingrediente": ingrediente.id,
                "nombre": ingrediente.nombre,
                "tipo": ingrediente.tipo,
                "cantidad": ingrediente.cantidad,
                "unidad_medida": ingrediente.unidad_medida,
            }
            for ingrediente in ingredientes
        ]

    @staticmethod
    def actualizar_ingrediente(
        session: Session, id_ingrediente: int, nueva_cantidad: Optional[float] = None
    ) -> Ingrediente:
        """
        Actualiza la cantidad de un ingrediente existente.
        """
        ingrediente = session.query(Ingrediente).filter_by(id=id_ingrediente).first()
        if not ingrediente:
            raise ValueError(f"Ingrediente con ID {id_ingrediente} no encontrado.")
        if nueva_cantidad is not None:
            if nueva_cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            ingrediente.cantidad = nueva_cantidad

        try:
            session.commit()
            session.refresh(ingrediente)
            return ingrediente
        except SQLAlchemyError as e:
            session.rollback()
            raise ValueError(f"Error al actualizar el ingrediente: {str(e)}")

    @staticmethod
    def eliminar_ingrediente(session: Session, id_ingrediente: int) -> Ingrediente:
        """
        Elimina un ingrediente de la base de datos.
        """
        ingrediente = session.query(Ingrediente).filter_by(id=id_ingrediente).first()
        if not ingrediente:
            raise ValueError(f"Ingrediente con ID {id_ingrediente} no encontrado.")
        
        try:
            session.delete(ingrediente)
            session.commit()
            return ingrediente
        except SQLAlchemyError as e:
            session.rollback()
            raise ValueError(f"Error al eliminar el ingrediente: {str(e)}")
=======
from sqlalchemy.orm import Session
from models import Ingrediente

class IngredienteCRUD:
    @staticmethod
    def crear_ingrediente(db: Session, nombre: str, tipo: str, cantidad: float, unidad: str):
        if not nombre or not tipo or cantidad <= 0:
            raise ValueError("Datos inválidos para crear un ingrediente.")
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
>>>>>>> Renè
