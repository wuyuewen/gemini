#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

from gemini.compute.types import ProviderExt
from libcloud.compute.providers import set_driver

DRIVERS_EXT = ({
        ProviderExt.LIBVIRT_EXT: 
        ('gemini.compute.driver.libvirt_driver_ext', 'LibvirtNodeDriverExt')
        })

set_driver(ProviderExt.LIBVIRT_EXT, DRIVERS_EXT[ProviderExt.LIBVIRT_EXT][0], DRIVERS_EXT[ProviderExt.LIBVIRT_EXT][1])
