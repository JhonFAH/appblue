from flask import Blueprint,render_template,request,redirect,url_for

admin_bp = Blueprint('admin',__name__,url_prefix='/admin',template_folder='templates')

# /admin/panel
@admin_bp.route('/panel')
def panel():
    return f"<h2> Bienvenido al panel de administracion </h2>"


