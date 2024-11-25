import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("green")  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestión de Clientes y Pedidos")
        self.geometry("750x600")

        # Crear el Tabview (pestañas)
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(pady=20, padx=20, fill="both", expand=True)

        self.tab_ingredientes = self.tabview.add("Ingredientes")
        self.pestaña_de_ingredientes(self.tab_ingredientes)

        self.tab_menus = self.tabview.add("Menus")
        self.pestaña_de_menu(self.tab_menus)

        self.tab_clientes = self.tabview.add("Clientes")
        self.pestaña_de_clientes(self.tab_clientes)

        self.tab_panel_de_compra = self.tabview.add("Panel de Compra")
        self.pestaña_de_panel_de_compra(self.tab_panel_de_compra)

        self.tab_pedidos = self.tabview.add("Pedidos")
        self.pestaña_de_pedidos(self.tab_pedidos)

    def pestaña_de_ingredientes(self, pos):
        # Gestión de Ingredientes
        self.frame_superior = ctk.CTkFrame(pos)
        self.frame_superior.pack(pady=0,padx=0)

        ctk.CTkLabel(self.frame_superior, text="Nombre Ingrediente").grid(row=0,column=0, pady=0,padx=10)
        ctk.CTkLabel(self.frame_superior, text="Cantidad").grid(row=0,column=1, pady=0,padx=10)
        ctk.CTkLabel(self.frame_superior, text="Tipo").grid(row=0,column=2, pady=0,padx=10)

        self.entry_nombre = ctk.CTkEntry(self.frame_superior)
        self.entry_nombre.grid(row=1,column=0, pady=10,padx=10)

        self.entry_cantidad = ctk.CTkEntry(self.frame_superior)
        self.entry_cantidad.grid(row=1,column=1, pady=10,padx=10)

        self.entry_tipo = ctk.CTkEntry(self.frame_superior)
        self.entry_tipo.grid(row=1,column=2, pady=10,padx=10)

        self.btn_crear_ingrediente = ctk.CTkButton(self.frame_superior, text="Crear Ingrediente")
        self.btn_crear_ingrediente.grid(row=1,column=3)

        self.btn_añadir_ing_existente = ctk.CTkButton(self.frame_superior, text="Añadir Ing. Existente")
        self.btn_añadir_ing_existente.grid(row=2,column=1, pady=20,padx=10)

        self.btn_listar_ingredientes = ctk.CTkButton(self.frame_superior, text="Listar Ingrediente")
        self.btn_listar_ingredientes.grid(row=2,column=2, pady=20,padx=10)

        # Visualizacion de Ingredientes
        self.frame_inferior = ctk.CTkFrame(pos)
        self.frame_inferior.pack(pady=0,padx=0)

        self.treeview_ingredientes = ttk.Treeview(self.frame_inferior, columns=("Nombre", "Cantidad", "Tipo"), show="headings")
        self.treeview_ingredientes.heading("Nombre", text="Nombre")
        self.treeview_ingredientes.heading("Cantidad", text="Cantidad")
        self.treeview_ingredientes.heading("Tipo", text="Tipo")
        self.treeview_ingredientes.pack(pady=10, padx=10, fill="both", expand=True)

    def pestaña_de_menu(self, pos):
        # Gestión de Meenu
        self.frame_superior = ctk.CTkFrame(pos)
        self.frame_superior.pack(pady=0,padx=0)

        self.btn_crear_menu = ctk.CTkButton(self.frame_superior, text="Crear Nuevo Menu")
        self.btn_crear_menu.grid(row=0,column=0,pady=10,padx=10)

        self.btn_ver_menus = ctk.CTkButton(self.frame_superior, text="Listar Menu")
        self.btn_ver_menus.grid(row=0,column=1,pady=10,padx=10)

        # Visualizacion de Meny
        self.frame_inferior = ctk.CTkFrame(pos)
        self.frame_inferior.pack(pady=0,padx=0)

        self.treeview_ingredientes = ttk.Treeview(self.frame_inferior, columns=("Nombre", "Descripción", "Ingredientes"), show="headings")
        self.treeview_ingredientes.heading("Nombre", text="Nombre")
        self.treeview_ingredientes.heading("Descripción", text="Descripción")
        self.treeview_ingredientes.heading("Ingredientes", text="Ingredientes")
        self.treeview_ingredientes.pack(pady=10, padx=10, fill="both", expand=True)

    def pestaña_de_clientes(self, pos):
        # Gestion de Clientes
        self.frame_superior = ctk.CTkFrame(pos)
        self.frame_superior.pack(pady=0,padx=0)

        ctk.CTkLabel(self.frame_superior, text="Nombre").grid(row=0, column=0, pady=10, padx=10)
        self.entry_nombre = ctk.CTkEntry(self.frame_superior)
        self.entry_nombre.grid(row=0, column=1, pady=10, padx=10)

        ctk.CTkLabel(self.frame_superior, text="Email").grid(row=0, column=2, pady=10, padx=10)
        self.entry_email = ctk.CTkEntry(self.frame_superior)
        self.entry_email.grid(row=0, column=3, pady=10, padx=10)

        self.btn_crear_cliente = ctk.CTkButton(self.frame_superior, text="Crear Cliente")
        self.btn_crear_cliente.grid(row=1, column=0, pady=10, padx=10)

        self.btn_actualizar_cliente = ctk.CTkButton(self.frame_superior, text="Actualizar Cliente")
        self.btn_actualizar_cliente.grid(row=1, column=1, pady=10, padx=10)

        self.btn_eliminar_cliente = ctk.CTkButton(self.frame_superior, text="Eliminar Cliente")
        self.btn_eliminar_cliente.grid(row=1, column=2, pady=10, padx=10)

        # Visualización de Clientes
        self.frame_inferior = ctk.CTkFrame(pos)
        self.frame_inferior.pack(pady=0,padx=0)

        self.treeview_clientes = ttk.Treeview(self.frame_inferior, columns=("Nombre", "Email"), show="headings")
        self.treeview_clientes.heading("Nombre", text="Nombre")
        self.treeview_clientes.heading("Email", text="Email")
        self.treeview_clientes.pack(pady=10, padx=10, fill="both", expand=True)

    def pestaña_de_panel_de_compra(self, pos):
        # Gestionar venta
        self.frame_superior = ctk.CTkFrame(pos)
        self.frame_superior.pack(pady=0,padx=0)

        ctk.CTkLabel(self.frame_superior, text="Cliente").grid(row=0,column=0, pady=10,padx=10)
        self.combo_cliente = ctk.CTkComboBox(self.frame_superior)
        self.combo_cliente.grid(row=0,column=1, pady=10,padx=10)

        ctk.CTkLabel(self.frame_superior, text="Menu").grid(row=1,column=0, pady=10,padx=10)
        self.combo_cliente = ctk.CTkComboBox(self.frame_superior)
        self.combo_cliente.grid(row=1,column=1, pady=10,padx=10)
        
        self.btn_agregar_menu = ctk.CTkButton(self.frame_superior, text="Agregar Menu")
        self.btn_agregar_menu.grid(row=2,column=1)

        # Visualizar Venta
        self.frame_inferior = ctk.CTkFrame(pos)
        self.frame_inferior.pack(pady=0,padx=0)

        self.treeview_venta = ttk.Treeview(self.frame_inferior, columns=("Cliente", "Menus", "Total"), show="headings")
        self.treeview_venta.heading("Cliente", text="Cliente")
        self.treeview_venta.heading("Menus", text="Menus")
        self.treeview_venta.heading("Total", text="Total")
        self.treeview_venta.pack(pady=10, padx=10, fill="both", expand=True)

        self.btn_realizar_compra = ctk.CTkButton(self.frame_inferior, text="Realizar Compra / Generar Boleta")
        self.btn_realizar_compra.pack(pady=10,padx=10)

    def pestaña_de_pedidos(self, pos):
        self.frame_superior = ctk.CTkFrame(pos)
        self.frame_superior.pack(pady=0,padx=0)

        ctk.CTkLabel(self.frame_superior, text="Cliente").grid(row=0,column=0, pady=10,padx=10)
        self.combo_cliente = ctk.CTkComboBox(self.frame_superior)
        self.combo_cliente.grid(row=0,column=1, pady=10,padx=10)

        self.btn_buscar_xcliente = ctk.CTkButton(self.frame_superior, text="Buscar por Cliente")
        self.btn_buscar_xcliente.grid(row=0,column=2,pady=10,padx=10)

        ctk.CTkLabel(self.frame_superior, text="Id").grid(row=1,column=0, pady=10,padx=10)
        self.entry_id = ctk.CTkEntry(self.frame_superior)
        self.entry_id.grid(row=1,column=1, pady=10,padx=10)

        self.btn_buscar_xid = ctk.CTkButton(self.frame_superior, text="Buscar por Id")
        self.btn_buscar_xid.grid(row=1,column=2,pady=10,padx=10)

        # Visualizar Pedido
        self.frame_inferior = ctk.CTkFrame(pos)
        self.frame_inferior.pack(pady=0,padx=0)
        
        self.treeview_pedido = ttk.Treeview(self.frame_inferior, columns=("Id","Cliente", "Menus", "Total", "Fecha"), show="headings")
        self.treeview_pedido.heading("Id", text="Id")
        self.treeview_pedido.heading("Cliente", text="Cliente")
        self.treeview_pedido.heading("Menus", text="Menus")
        self.treeview_pedido.heading("Total", text="Total")
        self.treeview_pedido.heading("Fecha", text="Fecha")
        self.treeview_pedido.pack(pady=10, padx=10, fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()