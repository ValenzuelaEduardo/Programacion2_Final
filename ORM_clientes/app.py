from database import inicializar_base_de_datos, get_session

from CRUD.cliente_crud import ClienteCRUD

from CRUD.ingrediente_crud import IngredienteCRUD

from CRUD.menu_crud import MenuCRUD

from CRUD.pedido_crud import PedidoCRUD

import customtkinter as ctk

from tkinter import ttk



class App:

    def __init__(self, master):

        self.master = master

        master.title("Gestión de Restaurante")



        # Botones de Navegación

        self.nav_frame = ctk.CTkFrame(master)

        self.nav_frame.pack(pady=5, padx=5, fill="x")

        

        self.btn_ingredientes = ctk.CTkButton(self.nav_frame, text="Ingredientes", command=self.mostrar_ingredientes)

        self.btn_ingredientes.pack(side="left", padx=5)



        self.btn_menu = ctk.CTkButton(self.nav_frame, text="Menú", command=self.mostrar_menu)

        self.btn_menu.pack(side="left", padx=5)



        self.btn_cliente = ctk.CTkButton(self.nav_frame, text="Cliente", command=self.mostrar_cliente)

        self.btn_cliente.pack(side="left", padx=5)



        self.btn_compra = ctk.CTkButton(self.nav_frame, text="Panel de Compra", command=self.mostrar_compra)

        self.btn_compra.pack(side="left", padx=5)



        self.btn_pedidos = ctk.CTkButton(self.nav_frame, text="Pedidos", command=self.mostrar_pedidos)

        self.btn_pedidos.pack(side="left", padx=5)



        self.btn_graficos = ctk.CTkButton(self.nav_frame, text="Gráficos", command=self.mostrar_graficos)

        self.btn_graficos.pack(side="left", padx=5)



        # Contenido Principal

        self.content_frame = ctk.CTkFrame(master)

        self.content_frame.pack(pady=10, padx=10, fill="both", expand=True)



        self.mostrar_ingredientes()  # Mostrar por defecto la gestión de ingredientes



    ### Métodos para gestionar cada sección

    def mostrar_ingredientes(self):

        self.limpiar_contenido()

        ctk.CTkLabel(self.content_frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entry_nombre_ingrediente = ctk.CTkEntry(self.content_frame, width=200)

        self.entry_nombre_ingrediente.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.content_frame, text="Tipo").grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.entry_tipo_ingrediente = ctk.CTkEntry(self.content_frame, width=200)

        self.entry_tipo_ingrediente.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkButton(self.content_frame, text="Crear Ingrediente", command=self.crear_ingrediente).grid(row=2, column=0, columnspan=2, pady=10)



    def crear_ingrediente(self):

        nombre = self.entry_nombre_ingrediente.get()

        tipo = self.entry_tipo_ingrediente.get()

        if not (nombre and tipo):

            print("Complete todos los campos para crear un ingrediente.")

            return

        try:

            with next(get_session()) as db:

                IngredienteCRUD.crear_ingrediente(db, nombre, tipo, 10, "Kg")

                print(f"Ingrediente '{nombre}' creado con éxito.")

        except ValueError as e:

            print(f"Error: {e}")



    def mostrar_menu(self):

        self.limpiar_contenido()

        ctk.CTkLabel(self.content_frame, text="Nombre del Menú").grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entry_nombre_menu = ctk.CTkEntry(self.content_frame, width=200)

        self.entry_nombre_menu.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.content_frame, text="Descripción").grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.entry_descripcion_menu = ctk.CTkEntry(self.content_frame, width=200)

        self.entry_descripcion_menu.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkButton(self.content_frame, text="Crear Menú", command=self.crear_menu).grid(row=2, column=0, columnspan=2, pady=10)



    def crear_menu(self):

        nombre = self.entry_nombre_menu.get()

        descripcion = self.entry_descripcion_menu.get()

        if not (nombre and descripcion):

            print("Complete todos los campos para crear un menú.")

            return

        try:

            with next(get_session()) as db:

                MenuCRUD.crear_menu(db, nombre, descripcion, 20.0, [])

                print(f"Menú '{nombre}' creado con éxito.")

        except ValueError as e:

            print(f"Error: {e}")



    def mostrar_cliente(self):

        self.limpiar_contenido()

        ctk.CTkLabel(self.content_frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entry_nombre_cliente = ctk.CTkEntry(self.content_frame, width=200)

        self.entry_nombre_cliente.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.content_frame, text="Correo").grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.entry_email_cliente = ctk.CTkEntry(self.content_frame, width=200)

        self.entry_email_cliente.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkButton(self.content_frame, text="Crear Cliente", command=self.crear_cliente).grid(row=2, column=0, pady=10)

        ctk.CTkButton(self.content_frame, text="Actualizar Cliente", command=self.actualizar_cliente).grid(row=2, column=1, pady=10)

        ctk.CTkButton(self.content_frame, text="Eliminar Cliente", command=self.eliminar_cliente).grid(row=3, column=0, columnspan=2, pady=10)



    def crear_cliente(self):

        nombre = self.entry_nombre_cliente.get()

        correo = self.entry_email_cliente.get()

        if not (nombre and correo):

            print("Complete todos los campos para crear un cliente.")

            return

        try:

            with next(get_session()) as db:

                ClienteCRUD.crear_cliente(db, nombre, correo)

                print(f"Cliente '{nombre}' creado con éxito.")

        except ValueError as e:

            print(f"Error: {e}")



    def actualizar_cliente(self):

        # Función de actualización

        pass



    def eliminar_cliente(self):

        # Función de eliminación

        pass



    def limpiar_contenido(self):

        for widget in self.content_frame.winfo_children():

            widget.destroy()



if __name__ == "__main__":

    root = ctk.CTk()

    inicializar_base_de_datos()

    app = App(root)

    root.mainloop()
