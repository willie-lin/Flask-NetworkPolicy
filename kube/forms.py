#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/4/10 16:57 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: forms.py
# @Software: PyCharm
# @Project Flask-NetworkPolicy 
"""

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, FloatField, PasswordField, RadioField
from wtforms.validators import DataRequired


class NetworkPolicyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    namespaces = StringField('namespaces', validators=[DataRequired()])
    cidr = StringField('cidr', validators=[DataRequired()])
    excepts = StringField('excepts', validators=[DataRequired()])
    port = StringField('port', validators=[DataRequired()])
    protocol = StringField('protocol', validators=[DataRequired()])
    project = StringField('project', validators=[DataRequired()])
    role = StringField('role', validators=[DataRequired()])
    spec_pod = StringField('spec_pod', validators=[DataRequired()])
    policy_type = StringField('policy_type', validators=[DataRequired()])
    submit = SubmitField('Submit')