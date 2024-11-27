from sqlalchemy.orm import Session
from models import Pedido, DetallePedido, Cliente, Menu

class PedidoCRUD:
    @staticmethod
    def crear_pedido(db: Session, cliente_id: int, menus: list[dict], total: float):
        cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not cliente:
            raise ValueError(f"Cliente con ID {cliente_id} no encontrado.")
        nuevo_pedido = Pedido(id_cliente=cliente_id, total=total)
        db.add(nuevo_pedido)
        db.flush()  

        for menu in menus:
            menu_obj = db.query(Menu).filter(Menu.id == menu["id_menu"]).first()
            if not menu_obj:
                raise ValueError(f"Menú con ID {menu['id_menu']} no encontrado.")
            detalle = DetallePedido(
                id_pedido=nuevo_pedido.id_pedido,
                id_menu=menu["id_menu"],
                cantidad=menu["cantidad"]
            )
            db.add(detalle)
        db.commit()
        db.refresh(nuevo_pedido)
        return nuevo_pedido

    @staticmethod
    def leer_pedidos(db: Session):
        pedidos = db.query(Pedido).all()
        return [
            {
                "id_pedido": pedido.id_pedido,
                "id_cliente": pedido.id_cliente,
                "total": pedido.total,
                "fecha_creacion": pedido.fecha_creacion,
                "detalles": [
                    {"id_menu": detalle.id_menu, "cantidad": detalle.cantidad}
                    for detalle in pedido.detalles
                ]
            }
            for pedido in pedidos
        ]

    @staticmethod
    def actualizar_pedido(db: Session, pedido_id: int, menus: list[dict], total: float):
        pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id).first()
        if not pedido:
            raise ValueError(f"Pedido con ID {pedido_id} no encontrado.")

        pedido.total = total

        db.query(DetallePedido).filter(DetallePedido.id_pedido == pedido_id).delete()
        for menu in menus:
            menu_obj = db.query(Menu).filter(Menu.id == menu["id_menu"]).first()
            if not menu_obj:
                raise ValueError(f"Menú con ID {menu['id_menu']} no encontrado.")
            detalle = DetallePedido(
                id_pedido=pedido_id,
                id_menu=menu["id_menu"],
                cantidad=menu["cantidad"]
            )
            db.add(detalle)
        db.commit()
        db.refresh(pedido)
        return pedido

    @staticmethod
    def borrar_pedido(db: Session, pedido_id: int):
        pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id).first()
        if not pedido:
            raise ValueError(f"Pedido con ID {pedido_id} no encontrado.")
        db.query(DetallePedido).filter(DetallePedido.id_pedido == pedido_id).delete()
        db.delete(pedido)
        db.commit()
        return pedido
