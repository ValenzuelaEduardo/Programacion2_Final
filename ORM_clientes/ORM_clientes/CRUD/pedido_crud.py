from sqlalchemy.orm import Session
from models import Pedido, Cliente, Menu

class PedidoCRUD:
    @staticmethod
    def crear_pedido(db: Session, cliente_correo: str, descripcion: str, menus_ids: list[int]):
        if not cliente_correo or not descripcion or not menus_ids:
            raise ValueError("El cliente, la descripción y los menús son obligatorios.")
    
        cliente = db.query(Cliente).filter(Cliente.correo == cliente_correo).first()
        if not cliente:
            raise ValueError(f"Cliente con correo '{cliente_correo}' no encontrado.")

        menus = db.query(Menu).filter(Menu.id_menu.in_(menus_ids)).all()
        if not menus:
            raise ValueError("No se encontraron menús válidos para este pedido.")
    
        total = sum(menu.precio for menu in menus) 
        nuevo_pedido = Pedido(
            descripcion=descripcion,
            cliente_id=cliente.id_cliente,  # Si la relación en Pedido usa 'cliente_id'
            total=total,
            menus=menus
        )
        db.add(nuevo_pedido)
        db.commit()
        db.refresh(nuevo_pedido)
        return nuevo_pedido
    

    @staticmethod
    def leer_pedidos(db: Session):
        pedidos = db.query(Pedido).all()
        if not pedidos:
            return []  # Devuelve una lista vacía si no hay pedidos

        return [
            {
                "id": pedido.id_pedido,  # Asegúrate de que 'id_pedido' esté en el modelo Pedido
                "descripcion": pedido.descripcion,
                "cliente": pedido.cliente.nombre,  # Asegúrate de que 'cliente' esté relacionado
                "menus": [menu.nombre for menu in pedido.menus],
                "total": pedido.total
            }
            for pedido in pedidos
        ]

    @staticmethod
    def actualizar_pedido(db: Session, pedido_id: int, descripcion: str = None, menus_ids: list[int] = None):
        pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id).first()
        if not pedido:
            raise ValueError(f"Pedido con ID {pedido_id} no encontrado.")

        if descripcion:
            pedido.descripcion = descripcion
        
        if menus_ids:
            menus = db.query(Menu).filter(Menu.id_menu.in_(menus_ids)).all()
            if not menus:
                raise ValueError("No se encontraron menús válidos para este pedido.")
            pedido.menus = menus
            pedido.total = sum(menu.precio for menu in menus)  # Recalcula el total

        db.commit()
        db.refresh(pedido)
        return pedido


    @staticmethod
    def borrar_pedido(db: Session, pedido_id: int):
        pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id).first()
        if not pedido:
            raise ValueError(f"Pedido con ID {pedido_id} no encontrado.")
        
        db.delete(pedido)
        db.commit()
        return pedido
