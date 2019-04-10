#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/4/10 15:08 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: kubernetes_data_processing.py
# @Software: PyCharm
# @Project DSec 
"""

from utils.kubernetes_api import KubernetesApi


class KubernetesUtils:

    def __init__(self, configs):
        self.clients = KubernetesApi(configs)

    def V1beta1IPBlock(self, cidr, excepts):
        v1IPBlock = self.clients.V1beta1IPBlock(cidr=cidr, excepts=excepts)
        return v1IPBlock

    def V1LabelSelectorRequirement(self, key, operator, values):
        v1LabelSelectorRequirement = self.clients.V1LabelSelectorRequirement(key=key, operator=operator, values=values)
        return v1LabelSelectorRequirement

    def V1beta1NetworkPolicyPort(self, port, protovol):
        v1NetworkPolicyPort = self.clients.V1beta1NetworkPolicyPort(port=port, protocol=protovol)
        return v1NetworkPolicyPort

    def V1LabelSelector(self, match_expressions, match_labels):
        v1LabelSelector = self.clients.V1LabelSelector(match_expressions=match_expressions, match_labels=match_labels)
        return v1LabelSelector

    def V1beta1NetworkPolicyPeer(self, ip_block, namespace_selector, pod_selector):
        v1NetworkPolicyPeer = self.clients.V1beta1NetworkPolicyPeer(ip_block=ip_block,
                                                                    namespace_selector=namespace_selector,
                                                                    pod_selector=pod_selector)
        return v1NetworkPolicyPeer

    def V1beta1NetworkPolicyIngressRule(self, _from, ports):
        v1NetworkPolicyIngressRule = self.clients.V1beta1NetworkPolicyIngressRule(_from=_from, ports=ports)
        return v1NetworkPolicyIngressRule

    def V1beta1NetworkPolicySpec(self, policy_types, pod_selector, ingress):
        v1NetworkPolicySpec = self.clients.V1beta1NetworkPolicySpec(policy_types=policy_types,
                                                                   pod_selector=pod_selector,
                                                                   ingress=ingress)
        return v1NetworkPolicySpec

    def V1ObjectMeta(self, name, namespace):
        v1ObjectMeta = self.clients.V1ObjectMeta(name=name, namespace=namespace)
        return v1ObjectMeta

    def V1beta1NetworkPolicy(self, api_version, kind, metadata, spec):
        v1NetworkPolicy = self.clients.V1beta1NetworkPolicy(api_version=api_version,
                                                            kind=kind,
                                                            metadata=metadata,
                                                            spec=spec)
        return v1NetworkPolicy

    def V1Namespace(self):
        v1Namespace = self.clients.V1Namespace()
        return v1Namespace

    def ExtensionsV1beta1Api(self):
        extensionsV1beta1Api = self.clients.ExtensionsV1beta1Api()
        return extensionsV1beta1Api

    def V1NamespaceList(self):
        v1NamespaceList = self.clients.V1NamespaceList()
        # print(v1NamespaceList)
        return v1NamespaceList