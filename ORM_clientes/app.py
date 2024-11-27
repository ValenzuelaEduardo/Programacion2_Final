from database import inicializar_base_de_datos, get_session
from models import Cliente, Pedido, Ingrediente, Menu
from CRUD.ingrediente_crud import IngredienteCRUD
from CRUD.menu_crud import MenuCRUD
from CRUD.cliente_crud import ClienteCRUD
from CRUD.pedido_crud import PedidoCRUD
import customtkinter as ctk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Gestión de Restaurante")

        self.tab_control = ctk.CTkTabview(master)
        self.tab_control.pack(pady=10, padx=10, fill="both", expand=True)

        # Pestaña para gestionar clientes
        self.tab_clientes = self.tab_control.add("Clientes")
        self.frame_clientes = ctk.CTkFrame(self.tab_clientes)
        self.frame_clientes.pack(pady=10, padx=10, fill="both", expand=True)

        self.label_nombre = ctk.CTkLabel(self.frame_clientes, text="Nombre del Cliente")
        self.label_nombre.pack(pady=5)
        self.entry_nombre = ctk.CTkEntry(self.frame_clientes)
        self.entry_nombre.pack(pady=5)

        self.label_correo = ctk.CTkLabel(self.frame_clientes, text="Correo del Cliente")
        self.label_correo.pack(pady=5)
        self.entry_correo = ctk.CTkEntry(self.frame_clientes)
        self.entry_correo.pack(pady=5)

        self.button_crear_cliente = ctk.CTkButton(self.frame_clientes, text="Crear Cliente", command=self.crear_cliente)
        self.button_crear_cliente.pack(pady=5)

        self.button_mostrar_clientes = ctk.CTkButton(self.frame_clientes, text="Mostrar Clientes", command=self.mostrar_clientes)
        self.button_mostrar_clientes.pack(pady=5)

        self.text_clientes = ctk.CTkTextbox(self.frame_clientes, width=400, height=200)
        self.text_clientes.pack(pady=5)

        # Pestaña para gestionar ingredientes
        self.tab_ingredientes = self.tab_control.add("Ingredientes")
        self.frame_ingredientes = ctk.CTkFrame(self.tab_ingredientes)
        self.frame_ingredientes.pack(pady=10, padx=10, fill="both", expand=True)

        self.label_nombre_ingrediente = ctk.CTkLabel(self.frame_ingredientes, text="Nombre del Ingrediente")
        self.label_nombre_ingrediente.pack(pady=5)
        self.entry_nombre_ingrediente = ctk.CTkEntry(self.frame_ingredientes)
        self.entry_nombre_ingrediente.pack(pady=5)

        self.label_tipo_ingrediente = ctk.CTkLabel(self.frame_ingredientes, text="Tipo del Ingrediente")
        self.label_tipo_ingrediente.pack(pady=5)
        self.entry_tipo_ingrediente = ctk.CTkEntry(self.frame_ingredientes)
        self.entry_tipo_ingrediente.pack(pady=5)

        self.label_cantidad_ingrediente = ctk.CTkLabel(self.frame_ingredientes, text="Cantidad del Ingrediente")
        self.label_cantidad_ingrediente.pack(pady=5)
        self.entry_cantidad_ingrediente = ctk.CTkEntry(self.frame_ingredientes)
        self.entry_cantidad_ingrediente.pack(pady=5)

        self.label_unidad_ingrediente = ctk.CTkLabel(self.frame_ingredientes, text="Unidad del Ingrediente")
        self.label_unidad_ingrediente.pack(pady=5)
        self.entry_unidad_ingrediente = ctk.CTkEntry(self.frame_ingredientes)
        self.entry_unidad_ingrediente.pack(pady=5)

        self.button_crear_ingrediente = ctk.CTkButton(self.frame_ingredientes, text="Crear Ingrediente", command=self.crear_ingrediente)
        self.button_crear_ingrediente.pack(pady=5)

        self.button_mostrar_ingredientes = ctk.CTkButton(self.frame_ingredientes, text="Mostrar Ingredientes", command=self.mostrar_ingredientes)
        self.button_mostrar_ingredientes.pack(pady=5)

        self.text_ingredientes = ctk.CTkTextbox(self.frame_ingredientes, width=400, height=200)
        self.text_ingredientes.pack(pady=5)

        # Pestaña para gestionar menús
        self.tab_menus = self.tab_control.add("Menús")
        self.frame_menus = ctk.CTkFrame(self.tab_menus)
        self.frame_menus.pack(pady=10, padx=10, fill="both", expand=True)

        self.label_nombre_menu = ctk.CTkLabel(self.frame_menus, text="Nombre del Menú")
        self.label_nombre_menu.pack(pady=5)
        self.entry_nombre_menu = ctk.CTkEntry(self.frame_menus)
        self.entry_nombre_menu.pack(pady=5)

        self.label_descripcion_menu = ctk.CTkLabel(self.frame_menus, text="Descripción del Menú")
        self.label_descripcion_menu.pack(pady=5)
        self.entry_descripcion_menu = ctk.CTkEntry(self.frame_menus)
        self.entry_descripcion_menu.pack(pady=5)

        self.button_crear_menu = ctk.CTkButton(self.frame_menus, text="Crear Menú", command=self.crear_menu)
        self.button_crear_menu.pack(pady=5)

        self.button_mostrar_menus = ctk.CTkButton(self.frame_menus, text="Mostrar Menús", command=self.mostrar_menus)
        self.button_mostrar_menus.pack(pady=5)

        self.text_menus = ctk.CTkTextbox(self.frame_menus, width=400, height=200)
        self.text_menus.pack(pady=5)

        # Pestaña para gestionar pedidos
        self.tab_pedidos = self.tab_control.add("Pedidos")
        self.frame_pedidos = ctk.CTkFrame(self.tab_pedidos)
        self.frame_pedidos.pack(pady=10, padx=10, fill="both", expand=True)

        self.label_cliente_pedido = ctk.CTkLabel(self.frame_pedidos, text="Correo del Cliente para el Pedido")
        self.label_cliente_pedido.pack(pady=5)
        self.entry_cliente_pedido = ctk.CTkEntry(self.frame_pedidos)
        self.entry_cliente_pedido.pack(pady=5)

        self.label_descripcion_pedido = ctk.CTkLabel(self.frame_pedidos, text="Descripción del Pedido")
        self.label_descripcion_pedido.pack(pady=5)
        self.entry_descripcion_pedido = ctk.CTkEntry(self.frame_pedidos)
        self.entry_descripcion_pedido.pack(pady=5)

        self.button_crear_pedido = ctk.CTkButton(self.frame_pedidos, text="Crear Pedido", command=self.crear_pedido)
        self.button_crear_pedido.pack(pady=5)

        self.button_mostrar_pedidos = ctk.CTkButton(self.frame_pedidos, text="Mostrar Pedidos", command=self.mostrar_pedidos)
        self.button_mostrar_pedidos.pack(pady=5)

        self.text_pedidos = ctk.CTkTextbox(self.frame_pedidos, width=400, height=200)
        self.text_pedidos.pack(pady=5)

    def crear_cliente(self):
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        if nombre and correo:
            with next(get_session()) as db:
                try:
                    ClienteCRUD.crear_Cliente(db, nombre, correo)
                    self.text_clientes.insert("end", f"Cliente '{nombre}' creado con éxito.\n")
                except ValueError as e:
                    self.text_clientes.insert("end", f"Error: {str(e)}\n")
        else:
            self.text_clientes.insert("end", "Por favor, ingrese un nombre y un correo válidos.\n")

    def mostrar_clientes(self):
        with next(get_session()) as db:
            clientes = ClienteCRUD.leer_Clientes(db)
            self.text_clientes.delete("1.0", "end")
            if clientes:
                for cliente in clientes:
                    self.text_clientes.insert("end", f"- {cliente.nombre} ({cliente.correo})\n")
            else:
                self.text_clientes.insert("end", "No hay clientes registrados.\n")

    def crear_ingrediente(self):
        nombre = self.entry_nombre_ingrediente.get()
        tipo = self.entry_tipo_ingrediente.get()
        cantidad = self.entry_cantidad_ingrediente.get()
        unidad = self.entry_unidad_ingrediente.get()
        if nombre and tipo and cantidad and unidad:
            with next(get_session()) as db:
                try:
                    IngredienteCRUD.crear_ingrediente(db, nombre, tipo, float(cantidad), unidad)
                    self.text_ingredientes.insert("end", f"Ingrediente '{nombre}' creado con éxito.\n")
                except ValueError as e:
                    self.text_ingredientes.insert("end", f"Error: {str(e)}\n")
        else:
            self.text_ingredientes.insert("end", "Por favor, ingrese todos los campos del ingrediente correctamente.\n")

    def mostrar_ingredientes(self):
        with next(get_session()) as db:
            ingredientes = IngredienteCRUD.leer_ingredientes(db)
            self.text_ingredientes.delete("1.0", "end")
            if ingredientes:
                for ingrediente in ingredientes:
                    self.text_ingredientes.insert("end", f"- {ingrediente.nombre} ({ingrediente.tipo}, {ingrediente.cantidad} {ingrediente.unidad})\n")
            else:
                self.text_ingredientes.insert("end", "No hay ingredientes registrados.\n")

    def crear_menu(self):
        nombre = self.entry_nombre_menu.get()
        descripcion = self.entry_descripcion_menu.get()
        if nombre and descripcion:
            with next(get_session()) as db:
                try:
                    MenuCRUD.crear_menu(db, nombre, descripcion, [])  # Se debe seleccionar ingredientes en la interfaz
                    self.text_menus.insert("end", f"Menú '{nombre}' creado con éxito.\n")
                except ValueError as e:
                    self.text_menus.insert("end", f"Error: {str(e)}\n")
        else:
            self.text_menus.insert("end", "Por favor, ingrese el nombre y la descripción del menú.\n")

    def mostrar_menus(self):
        with next(get_session()) as db:
            menus = MenuCRUD.leer_menus(db)
            self.text_menus.delete("1.0", "end")
            if menus:
                for menu in menus:
                    self.text_menus.insert("end", f"- {menu.nombre}: {menu.descripcion}\n")
            else:
                self.text_menus.insert("end", "No hay menús registrados.\n")

    def crear_pedido(self):
        cliente_correo = self.entry_cliente_pedido.get()
        descripcion = self.entry_descripcion_pedido.get()
        if cliente_correo and descripcion:
            with next(get_session()) as db:
                try:
                    PedidoCRUD.crear_pedido(db, cliente_correo, descripcion, [])  # Se debe seleccionar menús en la interfaz
                    self.text_pedidos.insert("end", f"Pedido para '{cliente_correo}' creado con éxito.\n")
                except ValueError as e:
                    self.text_pedidos.insert("end", f"Error: {str(e)}\n")
        else:
            self.text_pedidos.insert("end", "Por favor, ingrese el correo del cliente y la descripción del pedido.\n")

    def mostrar_pedidos(self):
        with next(get_session()) as db:
            pedidos = PedidoCRUD.leer_pedidos(db)
            self.text_pedidos.delete("1.0", "end")
            if pedidos:
                for pedido in pedidos:
                    self.text_pedidos.insert("end", f"- {pedido['descripcion']} para {pedido['cliente']}\n")
            else:
                self.text_pedidos.insert("end", "No hay pedidos registrados.\n")

if __name__ == "__main__":
    inicializar_base_de_datos()
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
