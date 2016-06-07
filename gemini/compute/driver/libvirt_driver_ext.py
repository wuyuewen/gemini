#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

import xmltodict
from gemini.compute.types import ProviderExt
from libcloud.compute.drivers.libvirt_driver import LibvirtNodeDriver 
from libcloud.compute.drivers.dummy import DummyNodeDriver

class LibvirtNodeDriverExt(LibvirtNodeDriver):
    
    type = ProviderExt.LIBVIRT_EXT
    
    def list_nodes(self, list_all=False):
        retv = []
        all_vms = self.connection.listAllDomains()
        if all_vms:
            for vm in all_vms:
                if cmp(vm.ID(), 0) == 0:
                    continue
                if list_all:
                    retv.append(xmltodict.parse(vm.XMLDesc()))
                elif cmp(vm.ID(), -1) != 0:
                    retv.append(xmltodict.parse(vm.XMLDesc()))
        return retv
    
    def inspect_node(self, uuid_or_name):
        if len(uuid_or_name) == 36:
            return xmltodict.parse(self.connection.lookupByUUIDString(uuid_or_name).XMLDesc())
        else:
            return xmltodict.parse(self.connection.lookupByName(uuid_or_name).XMLDesc())   
        
    def create_node(self, json):
        xml_desc = xmltodict.unparse(json, pretty=True)
        vm = self.connection.defineXML(xml_desc)
        return vm.UUIDString() 
          
    def start_node(self, uuid_or_name, flag):
        if len(uuid_or_name) == 36:
            return self.connection.lookupByUUIDString(uuid_or_name).createWithFlags(int(flag))
        else:
            return self.connection.lookupByName(uuid_or_name).createWithFlags(int(flag))
        
    def stop_node(self, uuid_or_name, flag):
        if len(uuid_or_name) == 36:
            return self.connection.lookupByUUIDString(uuid_or_name).shutdownFlags(int(flag))
        else:
            return self.connection.lookupByName(uuid_or_name).shutdownFlags(int(flag))
        
    def restart_node(self, uuid_or_name, flag):
        if len(uuid_or_name) == 36:
            return self.connection.lookupByUUIDString(uuid_or_name).reboot(int(flag))
        else:
            return self.connection.lookupByName(uuid_or_name).reboot(int(flag))
        
    def delete_node(self, uuid_or_name, flag):
        if len(uuid_or_name) == 36:
            return self.connection.lookupByUUIDString(uuid_or_name).undefineFlags(int(flag))
        else:
            return self.connection.lookupByName(uuid_or_name).undefineFlags(int(flag))   
