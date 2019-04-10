#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/4/10 16:59 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: models.py
# @Software: PyCharm
# @Project Flask-NetworkPolicy 
"""

from kube import db


class NetworkPolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    namespace = db.Column(db.String(64), index=True, unique=True)
    cidr = db.Column(db.String(64), index=True, unique=True)
    excepts = db.Column(db.String(64), index=True, unique=True)
    port = db.Column(db.Integer(), index=True, unique=True)
    protocol = db.Column(db.String(64), index=True, unique=True)
    project = db.Column(db.String(64), index=True, unique=True)
    role = db.Column(db.String(64), index=True, unique=True)
    spec_pod = db.Column(db.String(64), index=True, unique=True)
    policy_type = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<NetworkPolicy {}>'.format(self.name)