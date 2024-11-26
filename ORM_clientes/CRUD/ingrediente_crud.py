from sqlalchemy.exc import IntegrityError

# Crear una sesión
def get_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

#---------Create-------------------
def crear_ingrediente(nombre, tipo, cantidad, unidad_medida, session):
    try:
        nuevo_ingrediente = Ingrediente(nombre=nombre, tipo=tipo, cantidad=cantidad, unidad_medida=unidad_medida)
        session.add(nuevo_ingrediente)
        session.commit()
        print(f"Ingrediente '{nombre}' creado con éxito.")
    except IntegrityError:
        session.rollback()
        print("Error: Ya existe un ingrediente con este nombre.")

#---------Read-------------------
def leer_ingredientes(session):
    ingredientes = session.query(Ingrediente).all()
    for ingrediente in ingredientes:
        print(f"ID: {ingrediente.id_ingrediente}, Nombre: {ingrediente.nombre}, Tipo: {ingrediente.tipo}, Cantidad: {ingrediente.cantidad} {ingrediente.unidad_medida}")

#---------Update-------------------
def actualizar_ingrediente(id_ingrediente, nueva_cantidad, session):
    ingrediente = session.query(Ingrediente).filter_by(id_ingrediente=id_ingrediente).first()
    if ingrediente:
        ingrediente.cantidad = nueva_cantidad
        session.commit()
        print(f"Ingrediente ID {id_ingrediente} actualizado.")
    else:
        print("Ingrediente no encontrado.")

#---------Delete-------------------
def eliminar_ingrediente(id_ingrediente, session):
    ingrediente = session.query(Ingrediente).filter_by(id_ingrediente=id_ingrediente).first()
    if ingrediente:
        session.delete(ingrediente)
        session.commit()
        print(f"Ingrediente ID {id_ingrediente} eliminado.")
    else:
        print("Ingrediente no encontrado.")
