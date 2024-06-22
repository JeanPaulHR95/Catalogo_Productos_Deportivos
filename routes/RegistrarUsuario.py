from flask import Blueprint
from flask import request, make_response
from flask import jsonify
from models.Usuario import Usuario
from models.UsuarioTipo import UsuarioTipo
from schemas.Usuario_schema import Usuario_Schema
from werkzeug.security import generate_password_hash
import secrets
import string
from db import db

usuario = Blueprint('usuarios',__name__)

@usuario.route('/RegistrarUsuario', methods = ['POST']) #cambiar el nombre del CUS
def Guardar_datos():
    nombres = request.json.get('nombres') 
    apellidos = request.json.get('apellidos')
    correoinstitucional = request.json.get('correoinstitucional')
    edad = request.json.get('edad')
    sexo = request.json.get('sexo')
    estadocivil = request.json.get('estadocivil')
    ocupacion = request.json.get('ocupacion')

    new_usuario = Usuario(nombres, apellidos, correoinstitucional, edad, sexo, estadocivil, ocupacion)
   
    db.session.add(new_usuario)
    db.session.commit()

    
    result = Usuario_Schema.dump(new_usuario)
    data = {
        'codigo': "201",
        'mensaje': "Usuario Registrado",
        'data': result
    }
    
    return make_response(jsonify(data),201)


@usuario.route('/Buscarusuario/<string:correoinstitucional>',methods = ['GET'])
def Buscar_usuario(correoinstitucional):
    usuario = Usuario.query.filter_by(correoinstitucional = correoinstitucional).first()

    if not usuario:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = Usuario_Schema.dump(usuario)

    data = {
        'message': 'Usuario encontrado',
        'status': 200,
        'data': result       
    }
    return make_response(jsonify(data), 200)

@usuario.route('/EnviarContrasenia', methods = ['POST'])
def Generar_contrasenia():
    id_tipo = request.json.get('id_tipo') 
    id_usu = request.json.get('id_usu')
    sesion = request.json.get('sesion')
    fechasesion = request.json.get('fechasesion')
    condiciones = request.json.get('condiciones')
    terminos = request.json.get('terminos')

    # Genera una contraseña aleatoria segura
    alphabet = string.ascii_letters + string.digits + string.punctuation
    pre_contrasenia = ''.join(secrets.choice(alphabet) for i in range(12))  # Longitud de 12 caracteres

    # Hashea la contraseña generada
    contraseña = generate_password_hash(pre_contrasenia)    

    new_usuarioTipo = UsuarioTipo(id_tipo, id_usu, sesion, fechasesion, contraseña, condiciones, terminos)
    db.session.add(new_usuarioTipo)
    db.session.commit()

    data = {
        'message': 'Usuario Tipo registrado',
        'status': 201
    }

    return make_response(jsonify(data),201)



