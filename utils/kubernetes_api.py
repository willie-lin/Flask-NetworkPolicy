#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
# @Time    : 2019/4/3 23:35 
# @Author  :  林皆醉 
# @Desc : =============================================
# @FileName: utils.py
# @Software: PyCharm
# @Project DSec 
"""

from kubernetes import client, config


class KubernetesApi:

    def __init__(self, configs):
        self.configs = configs

    # V1NetworkPolicyList
    @staticmethod
    def V1beta1NetworkPolicyList():
        v1betaNetworkPolicyList = client.V1beta1NetworkPolicyList()
        return v1betaNetworkPolicyList

    #  network_policy
    @staticmethod
    def V1beta1NetworkPolicy(api_version, kind, metadata, spec):
        v1beta1NetworkPolicy = client.V1beta1NetworkPolicy(api_version=api_version,
                                                           kind=kind,
                                                           metadata=metadata,
                                                           spec=spec)
        return v1beta1NetworkPolicy

    # network_policy_metadata
    @staticmethod
    def V1ObjectMeta(name, namespace):
        v1ObjectMeta = client.V1ObjectMeta(name=name, namespace=namespace)
        return v1ObjectMeta

    # network_policy_spec
    @staticmethod
    def V1beta1NetworkPolicySpec(policy_types, pod_selector, ingress):
        v1beta1NetworkPolicySpec = client.V1beta1NetworkPolicySpec(policy_types=policy_types,
                                                                   pod_selector=pod_selector,
                                                                   ingress=ingress)
        return v1beta1NetworkPolicySpec

    # V1NetworkPolicyIngressRule
    @staticmethod
    def V1beta1NetworkPolicyEgressRule():
        v1beta1NetworkPolicyEgressRule = client.V1beta1NetworkPolicyEgressRule()
        return v1beta1NetworkPolicyEgressRule

    # V1NetworkPolicyIngressRule
    @staticmethod
    def V1beta1NetworkPolicyIngressRule(_from=None, ports=None):
        v1beta1NetworkPolicyIngressRule = client.V1beta1NetworkPolicyIngressRule(_from=_from, ports=ports)
        return v1beta1NetworkPolicyIngressRule

    # class V1LabelSelector(object):
    @staticmethod
    def V1LabelSelector(match_expressions=None, match_labels=None):
        V1LabelSelector = client.V1LabelSelector(match_expressions=match_expressions, match_labels=match_labels)
        return V1LabelSelector

    # V1LabelSelectorRequirement
    @staticmethod
    def V1LabelSelectorRequirement(key=None, operator=None, values=None):
        v1LabelSelectorRequirement = client.V1LabelSelectorRequirement(key=key, operator=operator, values=values)
        return v1LabelSelectorRequirement

    # V1NetworkPolicyPort
    @staticmethod
    def V1beta1NetworkPolicyPort(port, protocol):
        v1beta1NetworkPolicyPort = client.V1beta1NetworkPolicyPort(port=port, protocol=protocol)
        return v1beta1NetworkPolicyPort

    # V1NetworkPolicyPee
    @staticmethod
    def V1beta1NetworkPolicyPeer(ip_block, namespace_selector, pod_selector):
        v1beta1NetworkPolicyPeer = client.V1beta1NetworkPolicyPeer(ip_block=ip_block,
                                                                   namespace_selector=namespace_selector,
                                                                   pod_selector=pod_selector)
        return v1beta1NetworkPolicyPeer

    # V1IPBlock
    @staticmethod
    def V1beta1IPBlock(excepts, cidr):
        v1beta1IPBlock = client.V1beta1IPBlock(cidr=cidr, _except=excepts)
        return v1beta1IPBlock

    @staticmethod
    def V1Namespace():
        v1Namespace = client.V1Namespace()
        return v1Namespace

    @staticmethod
    def V1NamespaceList():
        v1NamespaceList = client.V1NamespaceList()
        return v1NamespaceList

    @staticmethod
    def ExtensionsV1beta1Api():
        networkingV1Api = client.ExtensionsV1beta1Api()
        return networkingV1Api
