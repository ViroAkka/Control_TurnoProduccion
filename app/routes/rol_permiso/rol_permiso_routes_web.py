from flask import Blueprint, render_template, abort, request, redirect, session, url_for, flash, get_flashed_messages
from flask_login import logout_user, login_required

# Extensions
from app.api.rol.rol_service import Rol_Service
from app.core.auth.permiso_requerido_decorator import permiso_requerido
from app.extensions.db import db
from app.extensions.messages import FlashMessages

# Services
from app.api.usuario.usuario_service import Usuario_Service
from app.api.rol_permiso.rol_permiso_service import Rol_Permiso_Service
from app.api.departamento.departamento_service import Departamento_Service

rol_permiso_web_bp = Blueprint(
    "rol_permiso_web", 
    __name__, 
    template_folder="../../templates"
)

@rol_permiso_web_bp.route("/crearRol_Permiso_web", methods=["GET", "POST"])
@login_required
@permiso_requerido("rol_permiso.crear")
def crearRol_Permiso_web():
    if request.method == "POST":
        data = {
            "idRol": request.form.get("idRol"),
            "idPermiso": request.form.get("idPermiso"),
        }

        result = Rol_Permiso_Service.createRol_Permiso_service(db, data)

        if "error" in result:
            FlashMessages.flash_error(result["error"])
            return redirect(url_for(
                "rol_template.listaRoles_template",
                ))
        else:
            FlashMessages.flash_success(result["mensaje"])
            return redirect(url_for(
                "rol_template.listaRoles_template",
                ))

    return redirect(url_for(
        "rol_template.crearUsuario_template",
        ))

@rol_permiso_web_bp.route("/editarRol_Permiso_web", methods=["GET", "POST"])
@login_required
@permiso_requerido("rol_permiso.editar")
def editarRol_Permiso_web():
    if request.method == "POST":
        data = {
            "idRol": request.form.get("idRol"),
            "idPermiso": request.form.get("idPermiso"),
        }

        result = Usuario_Service.updateUsuario_service(db, data)

        if "error" in result:
            FlashMessages.flash_error(result["error"])
            return redirect(url_for(
                "rol_template.listaRoles_template", 
            ))
        else:
            FlashMessages.flash_success(result["mensaje"])
            return redirect(url_for(
                "rol_template.listaRoles_template", 
            ))

    return redirect(url_for(
        "rol_template.listaRoles_template", 
    ))    

@rol_permiso_web_bp.route("/eliminarRol_Permiso_web", methods=["GET", "POST"])
@login_required
@permiso_requerido("rol_permiso.eliminar")
def eliminarRol_Permiso_web():
    if request.method == "POST":
        data = {
            "idRol": request.form.get("idRol"),
            "idPermiso": request.form.get("idPermiso"),
        }

        result = Rol_Permiso_Service.deleteRol_Permiso_service(db, data)

        if "error" in result:
            FlashMessages.flash_error(result["error"])
            return redirect(url_for(
                "rol_template.listaRoles_template",
            ))
        else:
            FlashMessages.flash_success(result["mensaje"])
            return redirect(url_for(
                "rol_template.listaRoles_template",
            ))

    return redirect(url_for(
        "rol_template.listaRoles_template", 
    ))    