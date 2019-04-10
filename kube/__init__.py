#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/4/10 16:34 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: __init__.py
# @Software: PyCharm
# @Project Flask-NetworkPolicy 
"""
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

network_policy = Flask(__name__)
network_policy.config.from_object(Config)
db = SQLAlchemy(network_policy)
migrate = Migrate(network_policy, db)
bootstrap = Bootstrap(network_policy)
from kube import routes, models
