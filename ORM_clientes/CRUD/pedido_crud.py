from sqlalchemy.orm import Session
from models import Pedido, Cliente, Menu, pedido_menu
from datetime import datetime


class PedidoCRUD:
    @staticmethod

    def crear_pedido(db: Session, cliente_id: int, descripcion: str, menus: list):

        if not descripcion or not menus:

            raise ValueError("La descripción y los menús son obligatorios para crear un pedido.")



        cliente = db.query(Cliente).filter(Cliente.id_cliente == cliente_id).first()

        if not cliente:

            raise ValueError(f"Cliente con ID {cliente_id} no encontrado.")



        total = 0

        for menu_id in menus:

            menu = db.query(Menu).filter(Menu.id_menu == menu_id).first()

            if not menu:

                raise ValueError(f"Menú con ID {menu_id} no encontrado.")

            total += menu.precio



        nuevo_pedido = Pedido(descripcion=descripcion, cliente_id=cliente_id, total=total, fecha_creacion=datetime.now())

        db.add(nuevo_pedido)

        db.commit()

        db.refresh(nuevo_pedido)



        for menu_id in menus:

            db.execute(

                pedido_menu.insert().values(

                    pedido_id=nuevo_pedido.id_pedido,

                    menu_id=menu_id

                )

            )



        db.commit()

        return nuevo_pedido


    @staticmethod
    def leer_pedidos(db: Session):
        return db.query(Pedido).all()



    @staticmethod
    def borrar_pedido(db: Session, pedido_id: int):
        pedido = db.query(Pedido).filter(Pedido.id_pedido == pedido_id).first()
        if not pedido:
            raise ValueError(f"Pedido con ID {pedido_id} no encontrado.")
        db.delete(pedido)
        db.commit()
        return pedido
