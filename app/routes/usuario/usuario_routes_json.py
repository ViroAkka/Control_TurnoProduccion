from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.api.usuario.usuario_service import Usuario_Service
from app.core.auth.permiso_requerido_decorator import permiso_requerido
from app.extensions.db import db

usuario_json_bp = Blueprint("usuario_json_bp", __name__)

@usuario_json_bp.route("/get_usuarios", methods=["GET"])
@login_required
def get_usuarios():
    data = Usuario_Service.getUsuarios_service(db)
    if not data:
        return jsonify([]), 200

    return jsonify(data), 200

