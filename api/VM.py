# -*- coding: utf-8 -*- 
#=================================================================
# Copyright(c) Institute of Software, Chinsese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25
from flask_restful.representations.json import output_json
from flask import request
from flask_restful import Resource, abort
from api.utils import libvirtutils
from api.utils import httputils
from api import app

log = app.logger

class List(Resource):
    
    def __init__(self):
        self.conn = libvirtutils._get_libvirt_connection()
    
    def get(self):
        try:
            get_all = httputils.to_bool(request.args.get('all', False))
            return output_json(libvirtutils.get_all_domains_xml_desc(self.conn, get_all), 200)
        except ValueError:
            abort(400, message="bad parameter")

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
        vm_uuid = libvirtutils.create_domain(self.conn, json_data)
        return output_json({"Uuid": vm_uuid, "Warnings": []}, 201)
    
class Inspect(Resource):
    def __init__(self):
        self.conn = libvirtutils._get_libvirt_connection()
        
    def get(self, uuid_or_name):
        try:
            return output_json(libvirtutils.get_domains_xml_desc(self.conn, uuid_or_name), 200)
        except ValueError:
            abort(400, message="bad parameter")
            
class Start(Resource):
    def __init__(self):
        self.conn = libvirtutils._get_libvirt_connection()
        
    def post(self, uuid_or_name):
        try:
            flag = request.args.get('flag', 0)
            return output_json(libvirtutils.start_domain(self.conn, uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
            
class Stop(Resource):
    def __init__(self):
        self.conn = libvirtutils._get_libvirt_connection()
        
    def post(self, uuid_or_name):
        try:
            flag = request.args.get('flag', 0)
            return output_json(libvirtutils.stop_domain(self.conn, uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")

class Restart(Resource):
    def __init__(self):
        self.conn = libvirtutils._get_libvirt_connection()
        
    def post(self, uuid_or_name):
        try:
            flag = request.args.get('flag', 0)
            return output_json(libvirtutils.restart_domain(self.conn, uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
            
class Delete(Resource):
    def __init__(self):
        self.conn = libvirtutils._get_libvirt_connection()
        
    def post(self, uuid_or_name):
        try:
            flag = request.args.get('flag', 0)
            return output_json(libvirtutils.delete_domain(self.conn, uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")        
