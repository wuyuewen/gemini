#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

from libcloud.compute.providers import get_driver

from gemini.compute.types import ProviderExt

__all__ = [
        "to_bool",
        "to_driver"
           ]

def to_bool(data):
    if str(data) in ['0', 'False', 'false']:
        return False
    elif str(data) in ['1', 'True', 'true']:
        return True
    else:
        raise ValueError

def _to_driver_URI(driver):
    ''' Return specific driver URI. URIs are documented at http://libvirt.org/uri.html
    :param: str value: the driver name
    :return: the specific driver URI that match with the driver name
    :rtype: str
    '''
    if driver == "xen":
        return "xen:///"
    elif driver == "qemu":
        return "qemu:///system"
    elif driver == "vbox":
        return "vbox:///session"
    else:
        return None
    
def to_driver(driver):
    cls = get_driver(ProviderExt.LIBVIRT_EXT)
    return cls(_to_driver_URI(driver))     
