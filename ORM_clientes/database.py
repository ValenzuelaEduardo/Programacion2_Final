# database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("database")

# Obtener la ruta del directorio donde está ubicado este archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Definir la URL de la base de datos con una ruta absoluta
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'restaurante.db')}"

try:
    engine = create_engine(DATABASE_URL, echo=True)
    logger.info("Motor de base de datos inicializado correctamente.")
except Exception as e:
    logger.error(f"Error al inicializar el motor de base de datos: {e}")
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_session():
    db = SessionLocal()
    try:
        logger.info("Sesión de base de datos creada.")
        yield db
    except Exception as e:
        logger.error(f"Error durante la sesión: {e}")
        raise
    finally:
        db.close()
        logger.info("Sesión de base de datos cerrada.")

def inicializar_base_de_datos():
    try:
        logger.info("Inicializando las tablas...")
        Base.metadata.drop_all(bind=engine)  # Borra todas las tablas existentes
        Base.metadata.create_all(bind=engine)  # Crea todas las tablas
        logger.info("Tablas creadas correctamente.")
    except Exception as e:
        logger.error(f"Error al inicializar las tablas: {e}")
        raise
