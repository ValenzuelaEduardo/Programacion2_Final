from sqlalchemy.orm import Session
from models import Pedido, DetallePedido, Menu

def crear_pedido(session: Session, id_cliente: int, menus: list[dict], total: float):
    nuevo_pedido = Pedido(id_cliente=id_cliente, total=total)
    session.add(nuevo_pedido)
    session.flush()  
    for menu in menus:
        detalle = DetallePedido(
            id_pedido=nuevo_pedido.id_pedido,
            id_menu=menu["id_menu"],
            cantidad=menu["cantidad"]
        )
        session.add(detalle)
    session.commit()
    return nuevo_pedido

def leer_pedidos(session: Session):
    pedidos = session.query(Pedido).all()
    return [{
        "id_pedido": pedido.id_pedido,
        "id_cliente": pedido.id_cliente,
        "total": pedido.total,
        "fecha_creacion": pedido.fecha_creacion,
        "detalles": [
            {"id_menu": detalle.id_menu, "cantidad": detalle.cantidad}
            for detalle in pedido.detalles
        ]
    } for pedido in pedidos]

def actualizar_pedido(session: Session, id_pedido: int, menus: list[dict], total: float):
    pedido = session.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()
    if not pedido:
        raise ValueError(f"Pedido con ID {id_pedido} no encontrado.")
    pedido.total = total
    session.query(DetallePedido).filter(DetallePedido.id_pedido == id_pedido).delete()
    for menu in menus:
        detalle = DetallePedido(
            id_pedido=id_pedido,
            id_menu=menu["id_menu"],
            cantidad=menu["cantidad"]
        )
        session.add(detalle)
    session.commit()
    return pedido

def eliminar_pedido(session: Session, id_pedido: int):
    pedido = session.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()
    if not pedido:
        raise ValueError(f"Pedido con ID {id_pedido} no encontrafo.")
    session.query(DetallePedido).filter(DetallePedido.id_pedido == id_pedido).delete()
    session.delete(pedido)
    session.commit()
