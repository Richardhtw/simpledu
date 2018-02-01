#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
user 蓝图，负责用户相关页面
"""

from flask import Blueprint, render_template
from simpledu.models import User

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/<username>')
def user_index(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


if __name__ == '__main__':
    pass
