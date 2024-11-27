import customtkinter as ctk
from tkinter import ttk, Listbox
from database import *
from CRUD.cliente_crud import ClienteCRUD
from CRUD.ingrediente_crud import IngredienteCRUD
from CRUD.menu_crud import MenuCRUD
from CRUD.pedido_crud import PedidoCRUD

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("green")  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Clientes y Pedidos")
        self.geometry("1000x700")

        # Crear el Tabview (pestañas)
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(pady=20, padx=20, fill="both", expand=True)

        self.tab_ingredientes = self.tabview.add("Ingredientes")
        self.pestaña_de_ingredientes(self.tab_ingredientes)

        self.tab_menus = self.tabview.add("Menús")
        self.pestaña_de_menu(self.tab_menus)


    # -------------------------
    # Pestaña de Ingredientes
    # -------------------------
    def pestaña_de_ingredientes(self, pos):
        self.frame_superior_ingredientes = ctk.CTkFrame(pos)
        self.frame_superior_ingredientes.pack(pady=10, padx=10)

        ctk.CTkLabel(self.frame_superior_ingredientes, text="Nombre").grid(row=0, column=0, padx=10)
        self.entry_nombre_ingrediente = ctk.CTkEntry(self.frame_superior_ingredientes)
        self.entry_nombre_ingrediente.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(self.frame_superior_ingredientes, text="Cantidad").grid(row=0, column=2, padx=10)
        self.entry_cantidad_ingrediente = ctk.CTkEntry(self.frame_superior_ingredientes)
        self.entry_cantidad_ingrediente.grid(row=0, column=3, padx=10)

        ctk.CTkLabel(self.frame_superior_ingredientes, text="Tipo").grid(row=0, column=4, padx=10)
        self.entry_tipo_ingrediente = ctk.CTkEntry(self.frame_superior_ingredientes)
        self.entry_tipo_ingrediente.grid(row=0, column=5, padx=10)

        self.btn_crear_ingrediente = ctk.CTkButton(
            self.frame_superior_ingredientes, text="Crear Ingrediente", command=self.crear_ingrediente
        )
        self.btn_crear_ingrediente.grid(row=0, column=6, padx=10)

        self.frame_inferior_ingredientes = ctk.CTkFrame(pos)
        self.frame_inferior_ingredientes.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeview_ingredientes = ttk.Treeview(
            self.frame_inferior_ingredientes, columns=("Nombre", "Cantidad", "Tipo"), show="headings"
        )
        self.treeview_ingredientes.heading("Nombre", text="Nombre")
        self.treeview_ingredientes.heading("Cantidad", text="Cantidad")
        self.treeview_ingredientes.heading("Tipo", text="Tipo")
        self.treeview_ingredientes.pack(pady=10, padx=10, fill="both", expand=True)

        self.listar_ingredientes()

    def crear_ingrediente(self):
        nombre = self.entry_nombre_ingrediente.get().strip()
        cantidad = self.entry_cantidad_ingrediente.get().strip()
        tipo = self.entry_tipo_ingrediente.get().strip()

        if not nombre or not cantidad or not tipo:
            print("Todos los campos son obligatorios.")
            return

        try:
            cantidad = float(cantidad)
        except ValueError:
            print("La cantidad debe ser un número válido.")
            return

        db = next(get_session())
        try:
            IngredienteCRUD.crear_ingrediente(db, nombre, tipo, cantidad, "unidad")
            self.listar_ingredientes()
        except ValueError as e:
            print(e)
        finally:
            db.close()

    def listar_ingredientes(self):
        db = next(get_session())
        ingredientes = IngredienteCRUD.leer_ingredientes(db)
        self.treeview_ingredientes.delete(*self.treeview_ingredientes.get_children())
        for ing in ingredientes:
            self.treeview_ingredientes.insert("", "end", values=(ing.nombre, ing.cantidad, ing.tipo))
        db.close()

    # -------------------------
    # Pestaña de Menús
    # -------------------------
    def pestaña_de_menu(self, pos):
        self.frame_superior_menus = ctk.CTkFrame(pos)
        self.frame_superior_menus.pack(pady=10, padx=10)

        ctk.CTkLabel(self.frame_superior_menus, text="Nombre Menú").grid(row=0, column=0, padx=10)
        self.entry_nombre_menu = ctk.CTkEntry(self.frame_superior_menus)
        self.entry_nombre_menu.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(self.frame_superior_menus, text="Descripción").grid(row=0, column=2, padx=10)
        self.entry_descripcion_menu = ctk.CTkEntry(self.frame_superior_menus)
        self.entry_descripcion_menu.grid(row=0, column=3, padx=10)

        self.btn_crear_menu = ctk.CTkButton(
            self.frame_superior_menus, text="Crear Menú", command=self.crear_menu
        )
        self.btn_crear_menu.grid(row=0, column=4, padx=10)

        self.frame_inferior_menus = ctk.CTkFrame(pos)
        self.frame_inferior_menus.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeview_menus = ttk.Treeview(
            self.frame_inferior_menus, columns=("ID","Nombre", "Descripción", "Ingredientes"), show="headings"
        )
        self.treeview_menus.heading("ID", text="ID")
        self.treeview_menus.heading("Nombre", text="Nombre")
        self.treeview_menus.heading("Descripción", text="Descripción")
        self.treeview_menus.heading("Ingredientes", text="Ingredientes")
        self.treeview_menus.pack(pady=10, padx=10, fill="both", expand=True)

        self.listar_menus()

    def crear_cliente(self):

        nombre = self.entry_nombre_cliente.get().strip()
        correo = self.entry_correo_cliente.get().strip()

        if not nombre or not correo:
            print("Todos los campos son obligatorios.")
            return

        db = next(get_session())
        try:
            ClienteCRUD.crear_cliente(db, nombre, correo)
            self.listar_clientes()
        except ValueError as e:
            print(e)
        finally:
            db.close()

    def listar_clientes(self):

        db = next(get_session())
        try:
            clientes = ClienteCRUD.leer_clientes(db)
            self.treeview_clientes.delete(*self.treeview_clientes.get_children())
            for cliente in clientes:
                self.treeview_clientes.insert("", "end", values=(cliente.id_cliente, cliente.nombre, cliente.correo))
        finally:
            db.close()


    def crear_menu(self):
        nombre = self.entry_nombre_menu.get().strip()
        descripcion = self.entry_descripcion_menu.get().strip()

        if not nombre or not descripcion:
            print("Todos los campos son obligatorios.")
            return

        db = next(get_session())
        try:
            MenuCRUD.crear_menu(db, nombre, descripcion, [])
            self.listar_menus()
        except ValueError as e:
            print(e)
        finally:
            db.close()

    def listar_menus(self):
        db = next(get_session())
        try:
            menus = MenuCRUD.leer_menus(db)
            self.treeview_menus.delete(*self.treeview_menus.get_children())
            for menu in menus:
                self.treeview_menus.insert("", "end", values=(menu.id, menu.nombre, menu.descripcion))
        finally:
            db.close()

if __name__ == "__main__":
    inicializar_base_de_datos()
    app = App()
    app.mainloop()