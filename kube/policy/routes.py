#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/4/15 10:30 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: routes.py
# @Software: PyCharm
# @Project Flask-NetworkPolicy 
"""
from pprint import pprint

import kubernetes
from flask import request, render_template
from kubernetes import client
from kubernetes.client.rest import ApiException

from kube import db
from kube.models import NetworkPolicy
from kube.policy import bp
from kube.policy.forms import NetworkPolicyForm
from utils.data_processing import data_body


@bp.route('/')
@bp.route('/index')
def index():
    return 'Hello World!'


@bp.route('/create_network_policy', methods=['GET', 'POST'])
def create_network_policy():
    API_Server = 'https://172.19.19.18:6443'
    TOKEN = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tY2M5OHIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjQ5NTQwNDkwLTRjY2UtMTFlOS04Y2ZhLTAwNTA1NmJiYjk5ZiIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.OI9Fqzt9MZ1d9pHRLdYauL6Kw0VZWiey7uzv_1PMpAF0Bs71Kf2Tid067FYAmQtKcbEi249nRWFVictAHEN3LWmB51YbBDty3b9YI1lGNJtAaMK5ks0kv84ksewwcRV-eOZ1yBMEB12u6qjYwWH6kMa7aqNXNFa1d85hakC09peedkFot5a3gKKV3EvL2wkRl8kTa9Upya7oi_xLI48YysmCR2q4nBKHoxezj6e6YekyH_kwW4vE7wVJTygu22lB2bUnyBcZzOSdp_h8AoYzsLySA3Dqpciud_1YsBcX1ZM_dZSNtvY5t0bqJKEzz17cpV7Bh6Lsv9RdJdIgBKz61A'
    API_KEY = {"authorization": "Bearer " + TOKEN}
    configuration = client.Configuration()
    configuration.host = API_Server
    configuration.verify_ssl = False
    configuration.api_key = API_KEY
    # client.Configuration.set_default(configuration)
    api_instance = kubernetes.client.ExtensionsV1beta1Api(kubernetes.client.ApiClient(configuration))
    form = NetworkPolicyForm()
    data = request.form.to_dict()
    if form.validate_on_submit():
        policy = NetworkPolicy(name=form.name.data, namespace=form.namespaces.data,
                               cidr=form.cidr.data, excepts=form.excepts.data,
                               port=form.port.data, protocol=form.protocol.data,
                               project=form.project.data, role=form.role.data,
                               spec_pod=form.spec_pod.data, policy_type=form.policy_type.data)
        db.session.add(policy)
        db.session.commit()
        namespace = form.namespaces.data   # str | object name and auth scope, such as for teams and projects
        body = data_body(data) # V1NetworkPolicy |
        print(body)
        try:
            api_response = api_instance.create_namespaced_network_policy(namespace, body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling NetworkingV1Api->create_namespaced_network_policy: %s\n" % e)
    return render_template('index.html', title='NetworkPolicy', form=form)