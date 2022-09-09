from flask import request
from ..modelos import db, Usuario, UsuarioSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token

usuario_schema = UsuarioSchema()


class VistaLogIn(Resource):
    def post(self):
            u_nombre = request.json["nombre"]
            u_contrasena = request.json["contrasena"]
            usuario = Usuario.query.filter_by(nombre=u_nombre, contrasena = u_contrasena).all()
            if usuario:
                token_de_acceso = create_access_token(identity=usuario[0].id)
                return {'mensaje':'Inicio de sesión exitoso', "token": token_de_acceso}
            else:
                return {'mensaje':'Nombre de usuario o contraseña incorrectos'}, 401


class VistaSignIn(Resource):
    
    def post(self):
        nuevo_usuario = Usuario(nombre=request.json["nombre"], contrasena=request.json["contrasena"])
        token_de_acceso = create_access_token(identity=request.json["nombre"])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return {"mensaje":'Usuario creado exitosamente', "token_de_acceso": token_de_acceso}

