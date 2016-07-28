#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

from libcloud.compute.types import Provider

__all__ = [
        "to_host_version",
        "check_uuid_or_name",
        "check_mac_or_name",
        "MemoryTypes",
        "ProviderExt",
        'HostInfo',
           ]

def check_uuid_or_name(data):
    if len(data.replace('-', '')) == 32:
        return True
    else:
        return False
    
def check_mac_or_name(data):
    if len(data.replace(':', '')) == 12 or len(data.replace('-', '')) == 12:
        return True
    else:
        return False
    
def to_host_version(version):
    version = int(version)
    major = version / 1000000
    version %= 1000000
    minor = version / 1000
    rel = version % 1000
    return '%d.%d.%d' % (major, minor, rel)
    

class Type(object):
    @classmethod
    def tostring(cls, value):
        """Return the string representation of the state object attribute
        :param str value: the state object to turn into string
        :return: the uppercase string that represents the state object
        :rtype: str
        """
        return value.upper()

    @classmethod
    def fromstring(cls, value):
        """Return the state object attribute that matches the string
        :param str value: the string to look up
        :return: the state object attribute that matches the string
        :rtype: str
        """
        return getattr(cls, value.upper(), None)
    
class MemoryTypes(Type):
    
    TARGET_MEMORY = 'target'
    MAX_MEMORY = 'max'

class ProviderExt(Provider):
    
    LIBVIRT_EXT = 'libvirt_ext'
    
class HostInfo(object):
    
    def __init__(self):
        self.model = None
        self.memory_kb = None
        self.cpus = None
        self.mhz = None
        self.numa = None
        self.sockets = None
        self.cores = None
        self.threads = None
        self.hostname = None
        self.hypervisor = None
        self.version = None
        self.lib_version = None
    
    def to_dict(self):
        return self.__dict__
