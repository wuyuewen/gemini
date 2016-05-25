#=================================================================
# Copyright(c) Institute of Software, Chinsese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25

from api import app
from utils.LazyView import LazyView

def url(url_rule, import_name, **options):
    view = LazyView('api.' + import_name)
    app.add_url_rule(url_rule, view_func=view, **options)

url('/vms/json', 'VM.get_all', methods=['GET'])
url('/vms/create', 'VM.create', methods=['Post'])
