#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

from gemini import restful_api
from gemini.restful.driver.libvirt_driver_ext import *

restful_api.add_resource(LibvritList, '/libvirt/<string:driver>/nodes/json')
restful_api.add_resource(LibvritCreate, '/libvirt/<string:driver>/nodes/create')
restful_api.add_resource(LibvritInspect, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/json')
restful_api.add_resource(LibvritStart, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/start')
restful_api.add_resource(LibvritStop, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/stop')
restful_api.add_resource(LibvritRestart, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/restart')
restful_api.add_resource(LibvritDelete, '/libvirt/<string:driver>/nodes/<string:uuid_or_name>/delete')