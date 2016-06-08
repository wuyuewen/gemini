#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

from gemini import restful_api
from gemini.restful.driver.libvirt_driver_ext import *

restful_api.add_resource(LibvirtList, '/libvirt/<string:driver>/nodes/json')
restful_api.add_resource(LibvirtCreate, '/libvirt/<string:driver>/nodes/create')
restful_api.add_resource(LibvirtInspect, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/json')
restful_api.add_resource(LibvirtStart, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/start')
restful_api.add_resource(LibvirtStop, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/stop')
restful_api.add_resource(LibvirtRestart, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/restart')
restful_api.add_resource(LibvirtDelete, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/delete')
restful_api.add_resource(LibvirtSuspend, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/suspend')
restful_api.add_resource(LibvirtResume, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/resume')
restful_api.add_resource(LibvirtAttachDevice, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/devices/attach')