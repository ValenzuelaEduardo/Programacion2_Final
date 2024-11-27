from database import inicializar_base_de_datos, get_session
from CRUD.cliente_crud import ClienteCRUD
from CRUD.ingrediente_crud import IngredienteCRUD
from CRUD.menu_crud import MenuCRUD
from CRUD.pedido_crud import PedidoCRUD


def pruebas_funcionales():
    inicializar_base_de_datos()
    print("Base de datos inicializada.")

    with next(get_session()) as db:
        print("Creando cliente...")
        cliente = ClienteCRUD.crear_cliente(db, nombre="Juan Pérez", correo="juan@example.com")
        print(f"Cliente creado: {cliente}")
        print("Leyendo clientes...")
        clientes = ClienteCRUD.leer_clientes(db)
        print(f"Clientes: {clientes}")
        print("Actualizando cliente...")

        cliente_actualizado = ClienteCRUD.actualizar_cliente(db, cliente.id_cliente, nombre="Juan Actualizado")
        print(f"Cliente actualizado: {cliente_actualizado}")
        print("Eliminando cliente...")
        ClienteCRUD.borrar_cliente(db, cliente.id_cliente)
        print(f"Cliente con ID {cliente.id_cliente} eliminado.")
        print("Creando ingrediente...")

        ingrediente = IngredienteCRUD.crear_ingrediente(db, nombre="Tomate", tipo="Vegetal", cantidad=10, unidad="Kg")
        print(f"Ingrediente creado: {ingrediente}")
        print("Leyendo ingredientes...")
        ingredientes = IngredienteCRUD.leer_ingredientes(db)

        print(f"Ingredientes: {ingredientes}")



        # Prueba CRUD de Menú

        print("Creando menú...")

        menu = MenuCRUD.crear_menu(db, nombre="Ensalada Mixta", descripcion="Ensalada con tomate y lechuga", precio=15.0, ingredientes=[{"id": ingrediente.id_ingrediente, "cantidad": 2}])

        print(f"Menú creado: {menu}")



        print("Leyendo menús...")

        menus = MenuCRUD.leer_menus(db)

        print(f"Menús: {menus}")



        # Prueba CRUD de Pedido

        print("Creando pedido...")

        pedido = PedidoCRUD.crear_pedido(db, cliente_id=cliente.id_cliente, descripcion="Pedido de prueba", menus=[menu.id_menu])

        print(f"Pedido creado: {pedido}")



        print("Leyendo pedidos...")

        pedidos = PedidoCRUD.leer_pedidos(db)

        print(f"Pedidos: {pedidos}")



        print("Eliminando pedido...")

        PedidoCRUD.borrar_pedido(db, pedido.id_pedido)

        print(f"Pedido con ID {pedido.id_pedido} eliminado.")


if __name__ == "__main__":

    pruebas_funcionales()
