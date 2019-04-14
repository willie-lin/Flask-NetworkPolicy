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
# from flask import Blueprint

from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# network_policy = Flask(__name__)

# network_policy.config.from_object(Config)
# db = SQLAlchemy(network_policy)
db = SQLAlchemy()
# migrate = Migrate(network_policy, db)
migrate = Migrate()
bootstrap = Bootstrap()
# from kube import routes, models
# from kube.api import bp as api_bp
# network_policy.register_blueprint(api_bp, url_prefix='/api')


def create_app(config_class=Config):
    network_policy = Flask(__name__)
    network_policy.config.from_object(config_class)
    db.init_app(network_policy)
    migrate.init_app(network_policy, db)
    bootstrap.init_app(network_policy)

    from kube.api import bp as api_bp
    network_policy.register_blueprint(api_bp, url_prefix='/api')

    return network_policy


from kube import models