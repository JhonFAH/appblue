
# Ejecucion de la aplicacion.
from app import create_app

# Instanciamos la aplicacion.
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
