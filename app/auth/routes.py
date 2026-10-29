from flask import Blueprint,render_template,request,redirect,url_for

auth_bp = Blueprint('auth',__name__,url_prefix='/auth',template_folder='templates')

# /auth/login
@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':
        usuario = request.form['usuario']
        return redirect(url_for('usuarios.perfil',nombre=usuario)) # Para las rutas usamos el nombre del blueprint.

    return render_template('login.html')


