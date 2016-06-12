#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

from libcloud.compute.types import Provider


__all__ = [
        "check_uuid",
        "Memory",
        "ProviderExt",
           ]

def check_uuid(data):
    if len(data.replace('-', '')) == 32:
        return True
    else:
        return False

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
    
class Memory(Type):
    
    TARGET_MEMORY = 'target'
    MAX_MEMORY = 'max'

class ProviderExt(Provider):
    
    LIBVIRT_EXT = 'libvirt_ext'