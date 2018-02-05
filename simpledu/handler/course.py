#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
course 蓝图，负责课程相关页面
"""

from flask import Blueprint, render_template
from simpledu.models import Course

course = Blueprint('course', __name__, url_prefix='/courses')


@course.route('/<int:course_id>')
def detail(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('course/detail.html', course=course)


if __name__ == '__main__':
    pass
