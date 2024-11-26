from sqlalchemy.orm import Session
from models import Cliente

def crear_cliente(session: Session, nombre: str, correo: str):
    nuevo_cliente = Cliente(nombre=nombre, correo=correo)
    session.add(nuevo_cliente)
    session.commit()
    return nuevo_cliente

def leer_clientes(session: Session):
    return session.query(Cliente).all()

def actualizar_cliente(session: Session, id_cliente: int, nombre: str = None, correo: str = None):
    cliente = session.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
    if not cliente:
        raise ValueError(f"Cliente con ID {id_cliente} no encontrado.")
    if nombre:
        cliente.nombre = nombre
    if correo:
        cliente.correo = correo
    session.commit()
    return cliente
def eliminar_cliente(session: Session, id_cliente: int):
    cliente = session.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
    if not cliente:
        raise ValueError(f"Cliente con id {id_cliente} no encontrado.")
    session.delete(cliente)
    session.commit()
