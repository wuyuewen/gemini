# -*- coding: utf-8 -*- 
#=================================================================
# Copyright(c) Institute of Software, Chinsese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

import libvirt
from api import app
from flask_restful import abort
import xmltodict

log = app.logger

def _get_libvirt_connection():
    libvirt_connection = None
    try:
        libvirt_connection = libvirt.open('xen:///')
    except Exception, e:
        log.exception("Libivrt connect to xen:/// failed!")
        log.exception(e)
        abort(403, reason="Libivrt connect to xen:/// failed!")
    return libvirt_connection

def get_all_domains_xml_desc(conn):
    retv = []
    all_vms = conn.listAllDomains()
    if all_vms:
        for vm in all_vms:
            if vm.ID() != 0:
#                 root = ElementTree.XML(vm.XMLDesc())
#                 xmldict = XmlDictConfig(root)
                xmldict = xmltodict.parse(vm.XMLDesc())
                retv.append(xmldict)
    return retv

def create_domain(conn, json):
    xml_desc = xmltodict.unparse(json, pretty=True)
    return xml_desc
