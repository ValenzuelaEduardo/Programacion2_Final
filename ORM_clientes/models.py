# models.py
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import *

# Tabla intermedia entre Menu e Ingrediente
menu_ingrediente = Table(
    'menu_ingrediente',
    Base.metadata,
    Column('menu_id', Integer, ForeignKey('menus.id_menu'), primary_key=True),
    Column('ingrediente_id', Integer, ForeignKey('ingredientes.id_ingrediente'), primary_key=True),
    Column('cantidad', Float, nullable=False)
)

# Tabla intermedia entre Pedido y Menu
pedido_menu = Table(
    'pedido_menu',
    Base.metadata,
    Column('pedido_id', Integer, ForeignKey('pedidos.id_pedido'), primary_key=True),
    Column('menu_id', Integer, ForeignKey('menus.id_menu'), primary_key=True)
)

# Modelo de Cliente
class Cliente(Base):
    __tablename__ = 'clientes'

    id_Cliente = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)

    pedidos = relationship("Pedido", back_populates="cliente")

# Modelo de Ingrediente
class Ingrediente(Base):
    __tablename__ = 'ingredientes'

    id_ingrediente = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    unidad = Column(String, nullable=False)

    menus = relationship("Menu", secondary=menu_ingrediente, back_populates="ingredientes")

# Modelo de Menu
class Menu(Base):
    __tablename__ = 'menus'

    id_menu = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    precio = Column(Float, nullable=False)

    ingredientes = relationship("Ingrediente", secondary=menu_ingrediente, back_populates="menus")
    pedidos = relationship("Pedido", secondary=pedido_menu, back_populates="menus")

# Modelo de Pedido
class Pedido(Base):
    __tablename__ = 'pedidos'

    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id_cliente'), nullable=False)
    total = Column(Float, nullable=False)

    cliente = relationship("Cliente", back_populates="pedidos")
    menus = relationship("Menu", secondary=pedido_menu, back_populates="pedidos")
