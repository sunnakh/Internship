import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# SQLAlchemy database instance
db = SQLAlchemy()

# Flask-Login manager
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app() -> Flask:
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "../templates"), static_folder=os.path.join(os.path.dirname(__file__), "../static"))

    # Basic configuration
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-change-me")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///crm.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Init extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from .auth import auth_bp  # noqa: WPS433
    from .routes import main_bp  # noqa: WPS433
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    # Setup user loader for Flask-Login
    from .models import User  # noqa: WPS433, WPS300

    @login_manager.user_loader
    def load_user(user_id: str):  # type: ignore[override]
        try:
            return db.session.get(User, int(user_id))
        except Exception:
            return None

    # Create tables on first run
    with app.app_context():
        db.create_all()

    return app