from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from . import db
from .forms import LoginForm, SignupForm
from .models import User


auth_bp = Blueprint("auth", __name__, url_prefix="")


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    form = SignupForm()
    if form.validate_on_submit():
        existing = User.query.filter_by(email=form.email.data.lower()).first()
        if existing:
            flash("Email is already registered.", "warning")
            return render_template("signup.html", form=form)

        user = User(email=form.email.data.lower())
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created. You can now sign in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("signup.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if not user or not user.check_password(form.password.data):
            flash("Invalid email or password.", "danger")
            return render_template("login.html", form=form)

        login_user(user, remember=form.remember.data)
        next_url = request.args.get("next")
        return redirect(next_url or url_for("main.dashboard"))

    return render_template("login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been signed out.", "info")
    return redirect(url_for("auth.login"))