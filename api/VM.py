#=================================================================
# Copyright(c) Institute of Software, Chinsese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25
from flask import request
from flask import make_response

def get_all():
    return "OK"

def create(vm_struct):
    return make_response(vm_struct)

        
