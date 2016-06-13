#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

from gemini import restful_api
from gemini.restful.driver.libvirt_driver_ext import *

restful_api.add_resource(LibvirtNodesList, '/libvirt/<string:driver>/nodes/json')
restful_api.add_resource(LibvirtNodesCreate, '/libvirt/<string:driver>/nodes/create')
restful_api.add_resource(LibvirtNodesInspect, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/json')
restful_api.add_resource(LibvirtNodesStart, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/start')
restful_api.add_resource(LibvirtNodesStop, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/stop')
restful_api.add_resource(LibvirtNodesDestroy, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/destroy')
restful_api.add_resource(LibvirtNodesRestart, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/restart')
restful_api.add_resource(LibvirtNodesDelete, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/delete')
restful_api.add_resource(LibvirtNodesSuspend, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/suspend')
restful_api.add_resource(LibvirtNodesResume, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/resume')
restful_api.add_resource(LibvirtNodesAttachDevice, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/devices/attach')
restful_api.add_resource(LibvirtNodesResizeMemory, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/memory/resize')
restful_api.add_resource(LibvirtNodesResizeVcpu, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/vcpu/resize')
# restful_api.add_resource(LibvirtSwitchToTemplate, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/template/switch')

restful_api.add_resource(LibvirtHostSystemInspect, '/libvirt/<string:driver>/host/system/json')
restful_api.add_resource(LibvirtHostInterfaceInspect, '/libvirt/<string:driver>/host/interfaces/<string:mac_or_name>/json')
