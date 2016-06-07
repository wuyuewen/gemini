#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

__all__ = [
        "to_bool",
           ]

def to_bool(data):
    if str(data) in ['0', 'False', 'false']:
        return False
    elif str(data) in ['1', 'True', 'true']:
        return True
    else:
        raise ValueError
