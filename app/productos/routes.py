from flask import Blueprint, render_template

# Creamos el modulo blueprint.
productos_bp = Blueprint('productos', __name__, url_prefix="/productos", template_folder="templates")

# /productos
@productos_bp.route("/") # ruta principal.
def lista_productos():
    return render_template('index.html')
    #return "<h2>Lista de productos </h2>"

# /productos/categorias/alimentos
@productos_bp.route("/categorias/<categoria>")
def mostrar_categorias(categoria):
    return f"<h3> Lista de produtos de la categoria: {categoria}</h3>"
