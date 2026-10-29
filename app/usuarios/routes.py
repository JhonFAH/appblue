from flask import Blueprint, render_template

usuarios_bp = Blueprint('usuarios', __name__, url_prefix="/usuarios", template_folder="templates")

# /usuarios
@usuarios_bp.route("/")
def lista_usuarios():
    return render_template('lista.html')
    # return "<h2>Lista de usuarios </h2>"

# /usuarios/perfil/Bruno
@usuarios_bp.route("/perfil/<nombre>")
def perfil(nombre):
    return render_template('perfil.html',nombre=nombre)
    # return f"<h3> Perfil del usuario: {nombre}</h3>"
