#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

import xmltodict
from gemini.compute.types import *
from libcloud.compute.drivers.libvirt_driver import LibvirtNodeDriver 


class LibvirtNodeDriverExt(LibvirtNodeDriver):
    
    type = ProviderExt.LIBVIRT_EXT
    
    def list_nodes(self, flag, list_all=False):
        retv = []
        all_vms = self.connection.listAllDomains()
        if all_vms:
            for vm in all_vms:
                if cmp(vm.ID(), 0) == 0:
                    continue
                if list_all:
                    retv.append(xmltodict.parse(vm.XMLDesc(flag)))
                elif cmp(vm.ID(), -1) != 0:
                    retv.append(xmltodict.parse(vm.XMLDesc(flag)))
        return retv
    
    def inspect_node(self, uuid_or_name, flag):
        if check_uuid(uuid_or_name):
            return xmltodict.parse(self.connection.lookupByUUIDString(uuid_or_name).XMLDesc(flag))
        else:
            return xmltodict.parse(self.connection.lookupByName(uuid_or_name).XMLDesc(flag))   
        
    def create_node(self, json):
        xml_desc = xmltodict.unparse(json, pretty=True)
        vm = self.connection.defineXML(xml_desc)
        return vm.UUIDString() 
          
    def start_node(self, uuid_or_name, flag):
        if check_uuid(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).createWithFlags(flag)
        else:
            return self.connection.lookupByName(uuid_or_name).createWithFlags(flag)
        
    def stop_node(self, uuid_or_name, flag):
        if check_uuid(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).shutdownFlags(flag)
        else:
            return self.connection.lookupByName(uuid_or_name).shutdownFlags(flag)
        
    def destroy_node(self, uuid_or_name, flag):
        if check_uuid(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).destroyFlags(flag)
        else:
            return self.connection.lookupByName(uuid_or_name).destroyFlags(flag)
        
    def restart_node(self, uuid_or_name, flag):
        if check_uuid(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).reboot(flag)
        else:
            return self.connection.lookupByName(uuid_or_name).reboot(flag)
        
    def delete_node(self, uuid_or_name, flag):
        if check_uuid(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).undefineFlags(flag)
        else:
            return self.connection.lookupByName(uuid_or_name).undefineFlags(flag)  
        
    def suspend_node(self, uuid_or_name):
        if check_uuid(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).suspend()
        else:
            return self.connection.lookupByName(uuid_or_name).suspend()

    def resume_node(self, uuid_or_name):
        if check_uuid(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).resume()
        else:
            return self.connection.lookupByName(uuid_or_name).resume()        
        
    def attach_device(self, uuid_or_name, json, flag):
        xml_desc = xmltodict.unparse(json, pretty=True)
        if check_uuid(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).attachDeviceFlags(xml_desc, flag)
        else:
            return self.connection.lookupByName(uuid_or_name).attachDeviceFlags(xml_desc, flag)
        
    def resize_memory(self, uuid_or_name, memory, memory_type, flag):
        if check_uuid(uuid_or_name):
            if memory_type == Memory.TARGET_MEMORY:
                return self.connection.lookupByUUIDString(uuid_or_name).setMemoryFlags(memory, flag)
            elif memory_type == Memory.MAX_MEMORY:
                return self.connection.lookupByUUIDString(uuid_or_name).setMaxMemory(memory)
            else:
                raise ValueError
        else:
            if memory_type == Memory.TARGET_MEMORY:
                return self.connection.lookupByName(uuid_or_name).setMemoryFlags(memory, flag) 
            elif memory_type == Memory.MAX_MEMORY:    
                return self.connection.lookupByName(uuid_or_name).setMaxMemory(memory)
            else:
                raise ValueError
            
    def resize_cpu(self, uuid_or_name, vcpu_num, flag):
        if check_uuid(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).setVcpusFlags(vcpu_num, flag)
        else:
            return self.connection.lookupByName(uuid_or_name).setVcpusFlags(vcpu_num, flag) 
        