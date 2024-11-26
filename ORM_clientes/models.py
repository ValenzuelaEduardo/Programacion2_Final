from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Cliente:
    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.pedidos = []  

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)


class Pedido:
    def __init__(self, id_pedido, cliente, fecha_creacion, total):
        self.id_pedido = id_pedido
        self.cliente = cliente 
        self.fecha_creacion = fecha_creacion
        self.total = total
        self.detalles = []  

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)


class DetallePedido:
    def __init__(self, id_detalle, pedido, menu, cantidad):
        self.id_detalle = id_detalle
        self.pedido = pedido  
        self.menu = menu  
        self.cantidad = cantidad


class Ingrediente:
    def __init__(self, id_ingrediente, nombre, tipo, cantidad, unidad_medida):
        self.id_ingrediente = id_ingrediente
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida


class IngredientePorMenu:
    def __init__(self, menu, ingrediente, cantidad, unidad_medida):
        self.menu = menu  
        self.ingrediente = ingrediente 
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida


class Menu:
    def __init__(self, id_menu, nombre, descripcion):
        self.id_menu = id_menu
        self.nombre = nombre
        self.descripcion = descripcion
        self.ingredientes = [] 
        self.detalles_pedido = [] 

    def agregar_ingrediente(self, ingrediente_por_menu):
        self.ingredientes.append(ingrediente_por_menu)

    def agregar_detalle_pedido(self, detalle_pedido):
        self.detalles_pedido.append(detalle_pedido)
