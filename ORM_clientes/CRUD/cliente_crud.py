from sqlalchemy.orm import Session
from models import Cliente



class ClienteCRUD:
    @staticmethod
    def crear_cliente(db: Session, nombre: str, correo: str):
        if not nombre or not correo:
            raise ValueError("El nombre y el correo son obligatorios.")
        cliente_existente = db.query(Cliente).filter(Cliente.correo == correo).first()
        if cliente_existente:
            raise ValueError(f"El cliente con correo '{correo}' ya existe.")
        nuevo_cliente = Cliente(nombre=nombre, correo=correo)
        db.add(nuevo_cliente)
        db.commit()
        db.refresh(nuevo_cliente)
        return nuevo_cliente



    @staticmethod
    def leer_clientes(db: Session):
        return db.query(Cliente).all()



    @staticmethod
    def actualizar_cliente(db: Session, id_cliente: int, nombre: str = None, correo: str = None):
        cliente = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
        if not cliente:
            raise ValueError(f"Cliente con ID {id_cliente} no encontrado.")
        if nombre:
            cliente.nombre = nombre
        if correo:
            cliente_existente = db.query(Cliente).filter(Cliente.correo == correo, Cliente.id_cliente != id_cliente).first()
            if cliente_existente:
                raise ValueError(f"Otro cliente con correo '{correo}' ya existe.")
            cliente.correo = correo
        db.commit()
        db.refresh(cliente)
        return cliente



    @staticmethod
    def borrar_cliente(db: Session, id_cliente: int):
        cliente = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
        if not cliente:
            raise ValueError(f"Cliente con ID {id_cliente} no encontrado.")
        db.delete(cliente)
        db.commit()
        return cliente
