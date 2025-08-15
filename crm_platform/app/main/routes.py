from __future__ import annotations

from flask import Blueprint, render_template
from flask_login import login_required


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
@login_required
def dashboard():
    return render_template("main/dashboard.html")