#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
admin 蓝图，负责后台管理相关页面
"""

from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/admin')
def admin_index():
    return 'admin'


if __name__ == '__main__':
    pass
