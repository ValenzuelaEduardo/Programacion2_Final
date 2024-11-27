
from sqlalchemy.orm import Session
from models import Cliente

class ClienteCRUD:
    @staticmethod
    def crear_Cliente(db: Session, nombre: str, correo: str):
        if not nombre or not correo:
            raise ValueError("El nombre y el correo no pueden estar vacíos.")
        cliente_existente = db.query(Cliente).filter(Cliente.correo == correo).first()
        if cliente_existente:
            raise ValueError(f"El cliente con correo '{correo}' ya existe.")

    @staticmethod
    def leer_Clientes(db: Session):
        return db.query(Cliente).all()

    @staticmethod
    def actualizar_Cliente(db: Session, id_cliente: int, nombre: str = None, tipo: str = None, cantidad: float = None, unidad: str = None):
        Cliente = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
        if not Cliente:
            raise ValueError(f"Cliente con ID {id_cliente} no encontrado.")
        if nombre:
            Cliente.nombre = nombre
        if tipo:
            Cliente.tipo = tipo
        if cantidad is not None:
            Cliente.cantidad = cantidad
        if unidad:
            Cliente.unidad = unidad
        
        db.commit()
        db.refresh(Cliente)
        return Cliente

    @staticmethod
    def borrar_Cliente(db: Session, id_cliente: int):
        Cliente = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
        if not Cliente:
            raise ValueError(f"Cliente con ID {id_cliente} no encontrado.")
        
        db.delete(Cliente)
        db.commit()
        return Cliente
