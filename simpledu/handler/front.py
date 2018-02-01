#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
front 蓝图，负责首页，注册，登录等页面
"""

from flask import Blueprint, render_template
from simpledu.models import Course

# 省略了 url_prefix，那么默认就是 '/'
front = Blueprint('front', __name__)


@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)


if __name__ == '__main__':
    pass
