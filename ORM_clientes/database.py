from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

# Configuración del motor de base de datos
DATABASE_URL = "sqlite:///restaurante.db"  # Cambiar a otro motor si se requiere (e.g., PostgreSQL, MySQL)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Base declarativa para los modelos
Base = declarative_base()

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Inicialización del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("database")

def inicializar_base_de_datos():
    """
    Inicializa la base de datos creando todas las tablas definidas en los modelos.
    """
    try:
        logger.info("Inicializando la base de datos...")
        Base.metadata.create_all(bind=engine)
        logger.info("Base de datos inicializada correctamente.")
    except Exception as e:
        logger.error(f"Error al inicializar la base de datos: {e}")

def get_session():
    """
    Provee una sesión para interactuar con la base de datos.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
