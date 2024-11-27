from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Definir la base de datos
Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    correo_electronico = Column(String, unique=True, nullable=False)

class Ingrediente(Base):
    __tablename__ = 'ingredientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, unique=True, nullable=False)
    tipo = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    unidad_medida = Column(String, nullable=False)

class Menu(Base):
    __tablename__ = 'menus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text)
    precio = Column(Float, nullable=False)
    disponible = Column(Integer, default=1)

class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    menu_id = Column(Integer, ForeignKey('menus.id'), nullable=False)
    total = Column(Float, nullable=False)
    fecha = Column(Text, nullable=False)
    
    cliente = relationship("Cliente", back_populates="pedidos")
    menu = relationship("Menu", back_populates="pedidos")

Cliente.pedidos = relationship("Pedido", order_by=Pedido.id, back_populates="cliente")
Menu.pedidos = relationship("Pedido", order_by=Pedido.id, back_populates="menu")

# Clase para manejar la base de datos
class BaseDatos:
    def __init__(self, db_path: str = 'sqlite:///restaurante.db'):
        """
        Initialize the database and create all tables if they don't exist.
        
        Args:
            db_path (str): Path to the SQLite database file
        """
        self.db_path = db_path
        self.engine = create_engine(self.db_path, echo=True)  # Crear engine de SQLAlchemy
        self.Session = sessionmaker(bind=self.engine)  # Crear un sessionmaker para la interacción con la base de datos
        self._create_tables()

    def _create_tables(self):
        """
        Create all necessary tables if they don't exist.
        """
        Base.metadata.create_all(self.engine)

    def get_session(self):
        """Devuelve una nueva sesión de base de datos."""
        return self.Session()
