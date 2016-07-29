#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

import xmltodict
from libcloud.compute.drivers.libvirt_driver import LibvirtNodeDriver 

from gemini.compute.types import *
from gemini import app

log = app.logger

class LibvirtNodeDriverExt(LibvirtNodeDriver):
    """
    An extension of Apache Libcloud :class: `LibvirtNodeDriver`.
    """
    
    type = ProviderExt.LIBVIRT_EXT
    
    def list_nodes(self, flag, list_all):
        """
        List all nodes.
        :param flag: options in showing XML description (optional)
        :type flag: ``int`` 
        :param list_all: ``True`` list all domains, ``False`` only running domains (default)
        :type list_all: ``str`` 
        :return: all nodes' XML description
        :rtype: ``list`` of ``str``
        """
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
        """
        Inspect node's XML description.
        :param uuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :param flag: options in showing XML description (optional)
        :type flag: ``int``
        :return: node's XML description
        :rtype: ``str``
        """
        if check_uuid_or_name(uuid_or_name):
            return xmltodict.parse(self.connection.lookupByUUIDString(uuid_or_name).XMLDesc(flag))
        else:
            return xmltodict.parse(self.connection.lookupByName(uuid_or_name).XMLDesc(flag))   
        
    def create_node(self, json):
        """
        Create node from json string.
        :param json: json string of node configuration
        :type json: ``str``
        :return: node's uuid
        :rtype: ``str``
        """
        xml_desc = xmltodict.unparse(json, pretty=True)
        vm = self.connection.defineXML(xml_desc)
        return vm.UUIDString() 
          
    def start_node(self, uuid_or_name, flag):
        """
        Start a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :param flag: options in starting node (optional)
        :type flag: ``int``
        :return: None
        """
        if check_uuid_or_name(uuid_or_name):
            if flag == 0:
                return self.connection.lookupByUUIDString(uuid_or_name).create()
            return self.connection.lookupByUUIDString(uuid_or_name).createWithFlags(flag)
        else:
            if flag == 0:
                return self.connection.lookupByName(uuid_or_name).create()
            return self.connection.lookupByName(uuid_or_name).createWithFlags(flag)
        
    def stop_node(self, uuid_or_name, flag):
        """
        Stop a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :param flag: options in stopping node (optional)
        :type flag: ``int``
        :return: None
        """
        if check_uuid_or_name(uuid_or_name):
            if flag == 0:
                return self.connection.lookupByUUIDString(uuid_or_name).shutdown()
            return self.connection.lookupByUUIDString(uuid_or_name).shutdownFlags(flag)
        else:
            if flag == 0:
                return self.connection.lookupByName(uuid_or_name).shutdown()
            return self.connection.lookupByName(uuid_or_name).shutdownFlags(flag)
        
    def destroy_node(self, uuid_or_name, flag):
        """
        Destroy a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :param flag: options in destroying node (optional)
        :type flag: ``int``
        :return: None
        """
        if check_uuid_or_name(uuid_or_name):
            if flag == 0:
                return self.connection.lookupByUUIDString(uuid_or_name).destroy()
            return self.connection.lookupByUUIDString(uuid_or_name).destroyFlags(flag)
        else:
            if flag == 0:
                return self.connection.lookupByName(uuid_or_name).destroy()
            return self.connection.lookupByName(uuid_or_name).destroyFlags(flag)
        
    def restart_node(self, uuid_or_name, flag):
        """
        Restart a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :param flag: options in restarting node (optional)
        :type flag: ``int``
        :return: None
        """
        if check_uuid_or_name(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).reboot(flag)
        else:
            return self.connection.lookupByName(uuid_or_name).reboot(flag)
        
    def delete_node(self, uuid_or_name, flag):
        """
        Delete a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :param flag: options in deleting node (optional)
        :type flag: ``int``
        :return: None
        """
        if check_uuid_or_name(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).undefineFlags(flag)
        else:
            return self.connection.lookupByName(uuid_or_name).undefineFlags(flag)  
        
    def suspend_node(self, uuid_or_name):
        """
        Suspend a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :return: None
        """
        if check_uuid_or_name(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).suspend()
        else:
            return self.connection.lookupByName(uuid_or_name).suspend()

    def resume_node(self, uuid_or_name):
        """
        Resume a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :return: None
        """
        if check_uuid_or_name(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).resume()
        else:
            return self.connection.lookupByName(uuid_or_name).resume()        
        
    def node_attach_device(self, uuid_or_name, json, flag):
        """
        Attach a virtual device to a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :param json: device detail of json string
        :type json: ``str``
        :param flag: options in attaching device (optional)
        :type flag: ``int``
        :return: None
        """
        xml_desc = xmltodict.unparse(json, pretty=True)
        if check_uuid_or_name(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).attachDeviceFlags(xml_desc, flag)
        else:
            return self.connection.lookupByName(uuid_or_name).attachDeviceFlags(xml_desc, flag)

    def node_detach_device(self, uuid_or_name, json, flag):
        """
        Detach a virtual device from a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :param json: device detail of json string
        :type json: ``str``
        :param flag: options in detaching device (optional)
        :type flag: ``int``
        :return: None
        """
        xml_desc = xmltodict.unparse(json, pretty=True)
        if check_uuid_or_name(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).detachDeviceFlags(xml_desc, flag)
        else:
            return self.connection.lookupByName(uuid_or_name).detachDeviceFlags(xml_desc, flag)
        
    def node_update_device(self, uuid_or_name, json, flag):
        """
        Update a virtual device to a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :param json: device detail of json string
        :type json: ``str``
        :param flag: options in updating device (optional)
        :type flag: ``int``
        :return: None
        """
        xml_desc = xmltodict.unparse(json, pretty=True)
        if check_uuid_or_name(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).updateDeviceFlags(xml_desc, flag)
        else:
            return self.connection.lookupByName(uuid_or_name).updateDeviceFlags(xml_desc, flag)
        
    def node_resize_memory(self, uuid_or_name, memory, memory_type, flag):
        """
        Resize memory to a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :param memory: memory KB value to set
        :type memory: ``int``
        :param memory_type: memory type to be resize
        :type memory_type: ``str``
        :param flag: options in resizing memory (optional)
        :type flag: ``int``
        :return: None
        """
        if check_uuid_or_name(uuid_or_name):
            if memory_type == MemoryTypes.TARGET_MEMORY:
                return self.connection.lookupByUUIDString(uuid_or_name).setMemoryFlags(memory, flag)
            elif memory_type == MemoryTypes.MAX_MEMORY:
                return self.connection.lookupByUUIDString(uuid_or_name).setMaxMemory(memory)
            else:
                raise ValueError
        else:
            if memory_type == MemoryTypes.TARGET_MEMORY:
                return self.connection.lookupByName(uuid_or_name).setMemoryFlags(memory, flag) 
            elif memory_type == MemoryTypes.MAX_MEMORY:    
                return self.connection.lookupByName(uuid_or_name).setMaxMemory(memory)
            else:
                raise ValueError
            
    def node_resize_cpu(self, uuid_or_name, vcpu_num, flag):
        """
        Resize cpu to a node.
        :param uuuid_or_name: uuid or name of node
        :type uuid_or_name: ``str``
        :param vcpu_num: cpu number to set
        :type vcpu_num: ``int``
        :param flag: options in resizing cpu (optional)
        :type flag: ``int``
        :return: None
        """
        if check_uuid_or_name(uuid_or_name):
            return self.connection.lookupByUUIDString(uuid_or_name).setVcpusFlags(vcpu_num, flag)
        else:
            return self.connection.lookupByName(uuid_or_name).setVcpusFlags(vcpu_num, flag) 
        
#     def switch_to_template(self, uuid_or_name, flag):
#         if check_uuid_or_name(uuid_or_name):
#             return self.connection.lookupByUUIDString(uuid_or_name).setMetadata(1, "template", None, None, flag)
#         else:
#             return self.connection.lookupByName(uuid_or_name).setMetadata(1, "template", None, None, flag)

    def inspect_host_system(self):
        """
        Inspect host details.
        :return: host details of software and hardware
        :rtype: ``dict``
        """
        host_info = HostInfo()
        info = self.connection.getInfo()
        if info:
            (host_info.model, host_info.memory_MB, host_info.cpus, host_info.mhz, host_info.numa, 
             host_info.sockets, host_info.cores, host_info.threads) = info
        host_info.hostname = self.connection.getHostname()
        host_info.hypervisor = self.connection.getType()
        host_info.version = to_host_version(self.connection.getVersion())
        host_info.lib_version = to_host_version(self.connection.getLibVersion())
        return host_info.to_dict()
    
    def list_host_interfaces(self, flag, list_all):
        """
        List all host interfaces
        :param flag: options in getting interfaces XML description (optional)
        :type flag: ``int``
        :param list_all: ``True`` list all interfaces, ``False`` only enabled interfaces (default)
        :type list_all: ``str`` 
        :return: list of interfaces
        :rtype: ``list``
        """
        retv = []
        interfaces = self.connection.listAllInterfaces()
        if interfaces:
            for interface in interfaces:
                if list_all:
                    retv.append(xmltodict.parse(interface.XMLDesc(flag)))
                elif interface.isActive():
                    retv.append(xmltodict.parse(interface.XMLDesc(flag)))
        return retv
    
    def inspect_host_interface(self, mac_or_uuid, flag):
        """
        Inspect host interface's XML description
        :param mac_or_uuid: mac address or uuid of interface
        :type mac_or_uuid: ``str``
        :param flag: options in getting interfaces XML description (optional)
        :type flag: ``int``
        :return: description of interface
        :rtype: ``str``
        """
        if check_mac_or_name(mac_or_uuid):
            return xmltodict.parse(self.connection.interfaceLookupByMACString(mac_or_uuid).XMLDesc(flag))
        else:
            return xmltodict.parse(self.connection.interfaceLookupByName(mac_or_uuid).XMLDesc(flag))         
        
        