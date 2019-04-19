#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/4/10 15:12 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: data_processing.py
# @Software: PyCharm
# @Project DSec 
"""


from utils.kubernetes_utils import KubernetesUtils


def data_body(data):
    configs = 'server/policy/config.yaml'
    utils = KubernetesUtils(configs)
    # print(utils)
    # cidr = "172.17.0.0/16"
    cidr = data.get('cidr')
    # cidr = data
    # excepts = "172.17.1.0/24"
    excepts = data.get('excepts')
    d = {'cidr': cidr}
    d.setdefault('except', []).append(excepts)

    ip_block = {
        "ipBlock": d
    }
    # print(ip_block)
# # data.port
#     port = 1024
    port = int(data.get('port'))
    # protocol = 'UDP'
    protocol = data.get('protocol')
    # ports = [utils.V1beta1NetworkPolicyPort(port=port, protovol=protocol)]
    # pprint(ports)
    # project = "myproject"
    project = data.get('project')
    # role = "db"
    role = data.get('role')

    namespace_matchLabels = {'project': project}
    pod__matchLabels = {'role': role}
    namespace_matchLabels = {
        'matchLabels': namespace_matchLabels
    }
    namespaceSelector = {
        'namespaceSelector': namespace_matchLabels
    }
    podSelectors = {
        'matchLabels': pod__matchLabels
    }
    podSelector = {
        'podSelector': podSelectors
    }
    # print(namespaceSelector)
    # print(podSelector)
# # from && ports
    _from = []
    _from.append(ip_block)
    _from.append(namespaceSelector)
    _from.append(podSelector)
    # print(_from)
    ports = [utils.V1beta1NetworkPolicyPort(port, protocol)]
    # print(ports)
    ingre = {
        "ports": ports,
        "from": _from
    }
    # print(ingre)
#
    # ingres = utils.V1beta1NetworkPolicyIngressRule(_from=_from, ports=ports)
    # print(ingres)
    ingress = []
    ingress.append(ingre)
    # print(ingress)
    # spec_pod  = 'db'
    spec_pod  = data.get('spec_pod')
    pods_matchLabels = {
        'role': spec_pod
    }
    matchLabels = {
        'matchLabels': pods_matchLabels
    }
    pod_selector = matchLabels
#     # print(pods_matchLabels)
#     # print(matchLabels)
#     print(pod_selector)
#     policy_type = "Ingress"
    policy_type = data.get('policy_type')
    policy_types =  []
    policy_types.append(policy_type)
    spec = utils.V1beta1NetworkPolicySpec(policy_types, pod_selector, ingress)
    # print(spec)
    # name = "test-04-10-network-policy"
    name = data.get('name')
    # namespace = 'default'
    namespace = data.get('namespaces')
    print(namespace)
    metadata = utils.V1ObjectMeta(name=name, namespace=namespace)
    api_version = 'extensions/v1beta1'
    kind = 'NetworkPolicy'
    # print(metadata)
    bodys = utils.V1beta1NetworkPolicy(api_version, kind, metadata, spec)
    # print(body)
    return bodys
