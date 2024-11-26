from sqlalchemy import Column, Integer,create_engine, String, ForeignKey,DateTime, Float
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#URL Base de datos XAMPP
DATABASE_URL = "mysql+mysqlconnector://root:@localhost/Restaurante"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Cliente(Base):
    __tablename__ = "clientes"
    id_cliente = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=True)
    correo = Column(String, unique=True ,nullable=True)

class Ingrediente(Base):
    __tablename__ = 'ingredientes'
    id_ingrediente = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    tipo = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    unidad_medida = Column(String, nullable=False)

class Menu(Base):
    __tablename__ = 'menus'
    id_menu = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(String)

class Pedido(Base):
    __tablename__ = 'pedidos'
    id_pedido = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'), nullable=False)
    fecha_creacion = Column(DateTime, null=False)
    total = Column(Float, nullable=False)
    cliente = relationship('Cliente', back_populates='pedidos')
    detalles = relationship('DetallePedido', back_populates='pedido')

class DetallePedido(Base):
    __tablename__ = 'detalle_pedido'
    id_detalle = Column(Integer, primary_key=True)
    id_pedido = Column(Integer, ForeignKey('pedidos.id_pedido'), null=False)
    id_menu = Column(Integer, ForeignKey('menus.id_menu'), null=False)
    cantidad = Column(Integer, null=False)
    pedido = relationship('Pedido', back_populates='detalles')

class IngredientesPorMenu(Base):
    __tablename__ = 'ingredientes_por_menu'
    id_menu = Column(Integer, ForeignKey('menus.id_menu'), primary_key=True)
    id_ingrediente = Column(Integer, ForeignKey('ingredientes.id_ingrediente'), primary_key=True)
    cantidad = Column(Float, nullable=False)
    unidad_medida = Column(String, null=False)

def init_db():
    Base.metadata.create_all(bind=engine)