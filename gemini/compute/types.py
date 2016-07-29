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
    """
    Return the result of the data whether or not an uuid
    :param data: data to checkout whether or not an uuid
    :type data: ``str``
    :return: ``True`` if it is an uuid, ``False`` otherwise.
    :rtype: ``bool``
    """
    if len(data.replace('-', '')) == 32:
        return True
    else:
        return False
    
def check_mac_or_name(data):
    """
    Return the result of the data whether or not a MAC address
    :param data: data to checkout whether or not a MAC
    :type data: ``str``
    :return: ``True`` if it is a MAC, ``False`` otherwise.
    :rtype: ``bool``
    """
    if len(data.replace(':', '')) == 12 or len(data.replace('-', '')) == 12:
        return True
    else:
        return False
    
def to_host_version(version):
    """
    Convert the software version of Hypervisor from integer to string
    :param version: integer type of version
    :type version: ``int``
    :return: ``str`` 
    """
    version = int(version)
    major = version / 1000000
    version %= 1000000
    minor = version / 1000
    rel = version % 1000
    return '%d.%d.%d' % (major, minor, rel)
    

class Type(object):
    @classmethod
    def tostring(cls, value):
        """
        Return the string representation of the state object attribute
        :param value: the state object to turn into string
        :type value: ``str``
        :return: the uppercase string that represents the state object
        :rtype: ``str``
        """
        return value.upper()

    @classmethod
    def fromstring(cls, value):
        """
        Return the state object attribute that matches the string
        :param value: the string to look up
        :type value: ``str``
        :return: the state object attribute that matches the string
        :rtype: ``str``
        """
        return getattr(cls, value.upper(), None)
    
class MemoryTypes(Type):
    """
    Memory values in VM configuration.
    """
    
    TARGET_MEMORY = 'target'
    MAX_MEMORY = 'max'

class ProviderExt(Provider):
    """
    An extension of Apache Libcloud :class: `Provider`
    """
    
    LIBVIRT_EXT = 'libvirt_ext'
    
class HostInfo(object):
    """
    A combination of host information from multiple interfaces.
    """
    
    def __init__(self):
        """
        Host basic information of software and hardware.
        :param cores: core number of host
        :type cores: ``int``
        :param cpus: cpu number of host
        :type cpus: ``int``
        :param hostname: hostname of host
        :type hostname: ``str``
        :param hypervisor: hypervisor name
        :type hypervisor: ``str``
        :param lib_version: libvirt library version
        :type lib_version: libvirt library version
        :param memory_MB: total memory of unit KB  
        :type memory_MB: ``int``
        :param mhz: the frequency of cpu
        :type mhz: ``int``
        :param model: the model of cpu
        :type model: ``str``
        :param numa: the NUMA of cpu
        :type numa: ``int``
        :param sockets: the socket number of cpu
        :type sockets: ``int``
        :param threads: the threads of cpu
        :type threads: ``int``
        :param version: the version of hypervisor
        :type version: ``str``
        """
        self.cores = None
        self.cpus = None
        self.hostname = None
        self.hypervisor = None
        self.lib_version = None
        self.memory_MB = None
        self.mhz = None
        self.model = None
        self.numa = None
        self.sockets = None
        self.threads = None
        self.version = None
    
    def to_dict(self):
        """
        Return the dictionary type of all parameters.
        :return: dictionary of all parameters
        :rtype: ``dict``
        """
        return self.__dict__
