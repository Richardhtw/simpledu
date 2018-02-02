#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
simpledu
"""

from flask import Flask
from flask_migrate import Migrate
from simpledu.config import configs
from simpledu.models import db


def create_app(config):
    """
    APP 工厂
    可以根据传入的 config 名称，加载不同的配置
    :param config:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    # SQLAlchemy 的初始化方式改为使用 init_app
    db.init_app(app)
    Migrate(app, db)
    register_blueprints(app)

    return app


def register_blueprints(app):
    from .handler import front, course, admin, user
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)
    app.register_blueprint(user)

    return app


if __name__ == '__main__':
    pass
