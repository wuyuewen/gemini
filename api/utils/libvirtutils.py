#=================================================================
# Copyright(c) Institute of Software, Chinsese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

import libvirt
from api import app
from flask_restful import abort

def _get_libvirt_connection():
    libvirt_connection = None
    try:
        libvirt_connection = libvirt.open('xen:///')
    except Exception, e:
        app.logger.exception("Libivrt connect to xen:/// failed!")
        app.logger.exception(e)
        abort(403, reason="Libivrt connect to xen:/// failed!")
    return libvirt_connection