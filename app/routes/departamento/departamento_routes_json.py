from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.core.auth.permiso_requerido_decorator import permiso_requerido
from app.extensions.db import db

programacion_json_bp = Blueprint("programacion_json_pb", __name__)

