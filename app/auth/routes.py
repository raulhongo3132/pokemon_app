from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from ..models.models import Usuario
from .. import db

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    return "Login aquí"

@auth.route("/register", methods=["GET", "POST"])
def register():
    return "Registro aquí"

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))
