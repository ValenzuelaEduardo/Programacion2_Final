from database import inicializar_base_de_datos, get_session
from models import Cliente, Pedido, Ingrediente, Menu
from CRUD.ingrediente_crud import IngredienteCRUD
from CRUD.menu_crud import MenuCRUD
from CRUD.cliente_crud import ClienteCRUD
from CRUD.pedido_crud import PedidoCRUD

def registrar_clientes(db):
    print("Registrando clientes...")
    ClienteCRUD.crear_Cliente(db, "Juan Pérez", "juan@example.com", 30)
    ClienteCRUD.crear_Cliente(db, "María Gómez", "maria@example.com", 25)
    print("Clientes registrados.")

def gestionar_ingredientes(db):
    print("Gestionando ingredientes...")
    IngredienteCRUD.crear_ingrediente(db, "Tomate", "Vegetal", 50, "kg")
    IngredienteCRUD.crear_ingrediente(db, "Carne", "Proteína", 100, "kg")
    IngredienteCRUD.crear_ingrediente(db, "Pan", "Carbohidrato", 200, "unidades")
    print("Ingredientes registrados.")

def gestionar_menus(db):
    print("Gestionando menús...")
    ingredientes = IngredienteCRUD.leer_ingredientes(db)
    if len(ingredientes) < 2:
        print("No hay suficientes ingredientes para crear un menú.")
        return

    MenuCRUD.crear_menu(
        db,
        "Hamburguesa Completa",
        "Hamburguesa con carne, tomate y pan",
        [ingredientes[0].id_ingrediente, ingredientes[1].id_ingrediente]
    )
    print("Menús registrados.")

def generar_pedidos(db):
    print("Generando pedidos...")
    cliente = ClienteCRUD.leer_clientes(db)[0]
    menu = MenuCRUD.leer_menus(db)[0]
    
    if cliente and menu:
        PedidoCRUD.crear_pedido(db, Cliente.correo, "Pedido 1", [menu.id_menu])
    print("Pedidos generados.")

def mostrar_estadisticas(db):
    print("Mostrando estadísticas...")
    pedidos = PedidoCRUD.leer_pedidos(db)
    print(f"Total de pedidos realizados: {len(pedidos)}")
    
    ingredientes = IngredienteCRUD.leer_ingredientes(db)
    print(f"Ingredientes disponibles: {len(ingredientes)}")
    
    menus = MenuCRUD.leer_menus(db)
    print(f"Menús disponibles: {len(menus)}")

def main():
    # Inicializar la base de datos
    inicializar_base_de_datos()

    # Crear una sesión
    with next(get_session()) as db:
        # Simular el flujo del sistema
        registrar_clientes(db)
        gestionar_ingredientes(db)
        gestionar_menus(db)
        generar_pedidos(db)
        mostrar_estadisticas(db)

if __name__ == "__main__":
    main()
