from flask import Blueprint, render_template

# Creamos el modulo blueprint.
blog_bp = Blueprint('blog', __name__, url_prefix="/blog", template_folder="templates")

# /blog/entrada/Nosotros
@blog_bp.route("/entrada/<id>")
def mostrar_entrada(id):
    return f"<h3> Titulo de blog: {id}</h3>"
