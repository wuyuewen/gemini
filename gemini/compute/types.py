#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

from libcloud.compute.types import Provider

class ProviderExt(Provider):
    
    LIBVIRT_EXT = 'libvirt_ext'
    