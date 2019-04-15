#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/4/15 10:20 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: __init__.py.py
# @Software: PyCharm
# @Project Flask-NetworkPolicy 
"""
from flask import Blueprint

bp = Blueprint('policy', __name__)

from kube.policy import routes