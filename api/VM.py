#=================================================================
# Copyright(c) Institute of Software, Chinsese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25
from flask_restful.representations.json import output_json
from flask_restful import reqparse
from flask_restful import Resource
from api.utils.libvirtutils import _get_libvirt_connection

class List(Resource):
    
    def __init__(self):
        self.conn = _get_libvirt_connection()
    
    def get(self):
        all_vms = self.conn.listAllDomains()
        return output_json(all_vms, 201)

class Create(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('uuid', type = str, required = True, help = 'No uuid provided', location = 'json')
        self.reqparse.add_argument('name', type = str, location = 'json')
        super(Create, self).__init__()
        
    def post(self):
        args = self.reqparse.parse_args()
        return output_json(args, 201)

        
