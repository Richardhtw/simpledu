#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
course 蓝图，负责课程相关页面
"""

from flask import Blueprint

course = Blueprint('course', __name__, url_prefix='/courses')

if __name__ == '__main__':
    pass
