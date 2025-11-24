from app import create_app, db

app = create_app()

with app.app_context():
    print("Creando tablas en la base de datos...")
    db.create_all()
    print("Listo. Tablas creadas correctamente.")
