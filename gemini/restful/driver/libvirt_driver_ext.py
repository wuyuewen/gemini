#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25
from flask_restful.representations.json import output_json
from flask import request
from flask_restful import Resource, abort
from gemini.restful.types import to_bool
from gemini import app

from gemini.compute.types import ProviderExt
from libcloud.compute.providers import get_driver

log = app.logger

__all__ = [
        "LibvritList",
        "LibvritCreate",
        "LibvritInspect",
        "LibvritStop",
        "LibvritStart",
        "LibvritRestart",
        "LibvritDelete",
           ]

def _driver_URI(driver):
    ''' Return specific driver URI. URIs are documented at http://libvirt.org/uri.html
    :param: str value: the driver name
    :return: the specific driver URI that match the driver name
    :rtype: str
    '''
    if driver == "xen":
        return "xen:///"
    elif driver == "qemu":
        return "qemu:///system"
    elif driver == "vbox":
        return "vbox:///session"
    else:
        return None

class LibvritList(Resource):
    
    def get(self, driver):
        try:
            cls = get_driver(ProviderExt.LIBVIRT_EXT)
            driver = cls(_driver_URI(driver))  
            list_all = to_bool(request.args.get('all', False))
            return output_json(driver.list_nodes(list_all), 200)
        except ValueError:
            abort(400, message="bad parameter")

class LibvritCreate(Resource):
#     def __init__(self):
#         self.reqparse = reqparse.RequestParser()
#         self.reqparse.add_argument('domain', type = str, required = True, help = 'No domain provided', location = 'json')
#         self.reqparse.add_argument('name', type = str, required = True, help = 'No name provided', location = 'json')
#         self.reqparse.add_argument('memory', type = str, required = True, help = 'No memory provided', location = 'json')
#         self.reqparse.add_argument('cpu', type = str, required = True, help = 'No name provided', location = 'json')
#         super(Create, self).__init__()
          
    def post(self, driver):
#         args = self.reqparse.parse_args()
        cls = get_driver(ProviderExt.LIBVIRT_EXT)
        driver = cls(_driver_URI(driver)) 
        json_data = request.get_json(force=True)
        vm_uuid = driver.create_node(json_data)
        return output_json({"Uuid": vm_uuid, "Warnings": []}, 201)
       
class LibvritInspect(Resource):
           
    def get(self, driver, uuid_or_name):
        try:
            cls = get_driver(ProviderExt.LIBVIRT_EXT)
            driver = cls(_driver_URI(driver)) 
            return output_json(driver.inspect_node(uuid_or_name), 200)
        except ValueError:
            abort(400, message="bad parameter")
               
class LibvritStart(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            cls = get_driver(ProviderExt.LIBVIRT_EXT)
            driver = cls(_driver_URI(driver)) 
            flag = request.args.get('flag', 0)
            return output_json(driver.start_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
               
class LibvritStop(Resource):
    
    def post(self, driver, uuid_or_name):
        try:
            cls = get_driver(ProviderExt.LIBVIRT_EXT)
            driver = cls(_driver_URI(driver)) 
            flag = request.args.get('flag', 0)
            return output_json(driver.stop_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
   
class LibvritRestart(Resource):
    
    def post(self, driver, uuid_or_name):
        try:
            cls = get_driver(ProviderExt.LIBVIRT_EXT)
            driver = cls(_driver_URI(driver))
            flag = request.args.get('flag', 0)
            return output_json(driver.restart_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
               
class LibvritDelete(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            cls = get_driver(ProviderExt.LIBVIRT_EXT)
            driver = cls(_driver_URI(driver))
            flag = request.args.get('flag', 0)
            return output_json(driver.delete_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")        
