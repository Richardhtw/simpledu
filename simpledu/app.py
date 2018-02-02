#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
simpledu
"""

from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from simpledu.config import configs
from simpledu.models import db, User


def create_app(config):
    """
    APP 工厂
    可以根据传入的 config 名称，加载不同的配置
    :param config:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(configs.get(config))

    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    from .handler import front, course, admin, user
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)
    app.register_blueprint(user)

    return app


def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)

    login_manager.login_view = 'front.login'


if __name__ == '__main__':
    pass
