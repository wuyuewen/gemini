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
        raise e
    return libvirt_connection

def get_all_domains_xml_desc(conn, get_all=False):
    retv = []
    all_vms = conn.listAllDomains()
    if all_vms:
        for vm in all_vms:
            if cmp(vm.ID(), 0) == 0:
                continue
            if get_all:
                retv.append(xmltodict.parse(vm.XMLDesc()))
            else:
                if cmp(vm.ID(), -1) != 0:
                    retv.append(xmltodict.parse(vm.XMLDesc()))
    return retv

def get_domains_xml_desc(conn, uuid_or_name):
    if len(uuid_or_name) == 36:
        return xmltodict.parse(conn.lookupByUUIDString(uuid_or_name).XMLDesc())
    else:
        return xmltodict.parse(conn.lookupByName(uuid_or_name).XMLDesc())
    
def create_domain(conn, json):
    xml_desc = xmltodict.unparse(json, pretty=True)
    vm = conn.defineXML(xml_desc)
    return vm.UUIDString()

def start_domain(conn, uuid_or_name, flag):
    if len(uuid_or_name) == 36:
        return conn.lookupByUUIDString(uuid_or_name).createWithFlags(flag)
    else:
        return conn.lookupByName(uuid_or_name).createWithFlags(flag)
    
def stop_domain(conn, uuid_or_name, flag):
    if len(uuid_or_name) == 36:
        return conn.lookupByUUIDString(uuid_or_name).shutdownFlags(flag)
    else:
        return conn.lookupByName(uuid_or_name).shutdownFlags(flag)
    
def restart_domain(conn, uuid_or_name, flag):
    if len(uuid_or_name) == 36:
        return conn.lookupByUUIDString(uuid_or_name).reboot(flag)
    else:
        return conn.lookupByName(uuid_or_name).reboot(flag)
    
def delete_domain(conn, uuid_or_name, flag):
    if len(uuid_or_name) == 36:
        return conn.lookupByUUIDString(uuid_or_name).undefineFlags(flag)
    else:
        return conn.lookupByName(uuid_or_name).undefineFlags(flag)
    
