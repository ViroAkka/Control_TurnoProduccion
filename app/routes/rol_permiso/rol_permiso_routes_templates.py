from flask import Blueprint, render_template, abort, request, redirect, url_for
from flask_login import login_required

from app.extensions.db import db
from app.extensions.messages import FlashMessages

rol_permiso_template_bp = Blueprint(
    "rol_permiso_template",
    __name__,
    template_folder="../../templates"
)

""" Los templates para esta tabla se manejaron por medio de modales en el /templates/listaRoles.html """