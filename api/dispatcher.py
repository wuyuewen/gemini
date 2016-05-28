# -*- coding: utf-8 -*- 
#=================================================================
# Copyright(c) Institute of Software, Chinsese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

from api import app, restful_api
from api.VM import Create, List

restful_api.add_resource(Create, '/vms/create')
restful_api.add_resource(List, '/vms/json')