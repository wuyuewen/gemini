# -*- coding: utf-8 -*- 
#=================================================================
# Copyright(c) Institute of Software, Chinsese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

from api import app, restful_api
from api.VM import Create, List, Inspect, Start, Stop, Restart, Delete

restful_api.add_resource(Create, '/vms/create')
restful_api.add_resource(List, '/vms/json')
restful_api.add_resource(Inspect, '/vms/<string:uuid_or_name>/json')
restful_api.add_resource(Start, '/vms/<string:uuid_or_name>/start')
restful_api.add_resource(Stop, '/vms/<string:uuid_or_name>/stop')
restful_api.add_resource(Restart, '/vms/<string:uuid_or_name>/restart')
restful_api.add_resource(Delete, '/vms/<string:uuid_or_name>/delete')