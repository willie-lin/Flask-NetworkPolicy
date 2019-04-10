#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/4/10 16:34 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: config.py
# @Software: PyCharm
# @Project Flask-NetworkPolicy 
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'kubernetes.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False