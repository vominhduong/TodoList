import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    """Application Factory: tạo và cấu hình Flask app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # Đảm bảo thư mục instance/ tồn tại (nơi chứa file SQLite)
    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    with app.app_context():
        from app import models  # noqa: F401  (đăng ký model trước khi tạo bảng)
        db.create_all()

    return app
