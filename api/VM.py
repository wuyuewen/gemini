# -*- coding: utf-8 -*- 
#=================================================================
# Copyright(c) Institute of Software, Chinsese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25
from flask_restful.representations.json import output_json
from flask import request
from flask_restful import Resource
from api.utils import libvirtutils

class List(Resource):
    
    def __init__(self):
        self.conn = libvirtutils._get_libvirt_connection()
    
    def get(self):
        return output_json(libvirtutils.get_all_domains_xml_desc(self.conn), 201)

class Create(Resource):
    def __init__(self):
        self.conn = libvirtutils._get_libvirt_connection()
#         self.reqparse = reqparse.RequestParser()
#         self.reqparse.add_argument('domain', type = str, required = True, help = 'No domain provided', location = 'json')
#         self.reqparse.add_argument('name', type = str, required = True, help = 'No name provided', location = 'json')
#         self.reqparse.add_argument('memory', type = str, required = True, help = 'No memory provided', location = 'json')
#         self.reqparse.add_argument('cpu', type = str, required = True, help = 'No name provided', location = 'json')
#         super(Create, self).__init__()
        
    def post(self):
        json_data = request.get_json(force=True)
#         args = self.reqparse.parse_args()
        xml_data = libvirtutils.create_domain(self.conn, json_data)
        return output_json(xml_data, 201)

        
