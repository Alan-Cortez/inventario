from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)

    # Configuración
    app.config.from_object('config.Config')

    # Inicializar MySQL
    mysql.init_app(app)

    # Registrar rutas
    from .routes import main
    app.register_blueprint(main)

    return app
