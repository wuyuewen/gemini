#=================================================================
# Copyright(c) Institute of Software, Chinese Academy of Sciences
#=================================================================
# Author : wuyuewen@otcaix.iscas.ac.cn
# Date   : 2016/05/25
from flask_restful.representations.json import output_json
from flask import request
from flask_restful import Resource, abort
from gemini.restful.types import *
from gemini import app


log = app.logger

__all__ = [
        "LibvirtNodesList",
        "LibvirtNodesCreate",
        "LibvirtNodesInspect",
        "LibvirtNodesStop",
        "LibvirtNodesDestroy",
        "LibvirtNodesStart",
        "LibvirtNodesRestart",
        "LibvirtNodesDelete",
        "LibvirtNodesSuspend",
        "LibvirtNodesResume",
        "LibvirtNodesAttachDevice",
        "LibvirtNodesResizeMemory",
        "LibvirtNodesResizeVcpu",
#         "LibvirtSwitchToTemplate",
        "LibvirtHostSystemInspect",
        "LibvirtHostInterfacesList",
        "LibvirtHostInterfacesInspect",
           ]

class LibvirtNodesList(Resource):
    
    def get(self, driver):
        try:
            driver = to_driver(driver) 
            list_all = to_bool(request.args.get('all', False))
            flag = int(request.args.get('flag', 0))
            return output_json(driver.list_nodes(flag, list_all), 200)
        except ValueError:
            abort(400, message="bad parameter")

class LibvirtNodesCreate(Resource):
          
    def post(self, driver):
        driver = to_driver(driver)
        json_data = request.get_json(force=True)
        vm_uuid = driver.create_node(json_data)
        return output_json({"Uuid": vm_uuid, "Warnings": []}, 201)
       
class LibvirtNodesInspect(Resource):
           
    def get(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            flag = int(request.args.get('flag', 0))
            return output_json(driver.inspect_node(uuid_or_name, flag), 200)
        except ValueError:
            abort(400, message="bad parameter")
               
class LibvirtNodesStart(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            flag = int(request.args.get('flag', 0))
            return output_json(driver.start_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
               
class LibvirtNodesStop(Resource):
    
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver) 
            flag = int(request.args.get('flag', 0))
            return output_json(driver.stop_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
            
class LibvirtNodesDestroy(Resource):
    
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver) 
            flag = int(request.args.get('flag', 0))
            return output_json(driver.destroy_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
   
class LibvirtNodesRestart(Resource):
    
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            flag = int(request.args.get('flag', 0))
            return output_json(driver.restart_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
               
class LibvirtNodesDelete(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            flag = int(request.args.get('flag', 0))
            return output_json(driver.delete_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")        

class LibvirtNodesSuspend(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            return output_json(driver.suspend_node(uuid_or_name), 204)
        except ValueError:
            abort(400, message="bad parameter")       
            
class LibvirtNodesResume(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            return output_json(driver.resume_node(uuid_or_name), 204)
        except ValueError:
            abort(400, message="bad parameter")   
            
class LibvirtNodesAttachDevice(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            json_data = request.get_json(force=True)
            flag = int(request.args.get('flag', 0))
            return output_json(driver.node_attach_device(uuid_or_name, json_data, flag), 201)
        except ValueError:
            abort(400, message="bad parameter") 
            
class LibvirtNodesResizeMemory(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            memory = int(request.args.get('size', 0))
            memory_type = request.args.get('type', None)
            flag = int(request.args.get('flag', 0))
            if not memory or not memory_type:
                abort(400, message="bad parameter")
            return output_json(driver.node_resize_memory(uuid_or_name, memory, memory_type, flag), 204)
        except ValueError:
            abort(400, message="bad parameter") 
            
class LibvirtNodesResizeVcpu(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            vcpu = int(request.args.get('size', 0))
            flag = int(request.args.get('flag', 0))
            if not vcpu:
                abort(400, message="bad parameter")
            return output_json(driver.node_resize_cpu(uuid_or_name, vcpu, flag), 204)
        except ValueError:
            abort(400, message="bad parameter") 

# class LibvirtSwitchToTemplate(Resource):
#            
#     def post(self, driver, uuid_or_name):
#         try:
#             driver = to_driver(driver)
#             flag = int(request.args.get('flag', 0))
#             return output_json(driver.switch_to_template(uuid_or_name, flag), 204)
#         except ValueError:
#             abort(400, message="bad parameter") 

class LibvirtHostSystemInspect(Resource):
           
    def get(self, driver):
        try:
            driver = to_driver(driver)
            return output_json(driver.inspect_host_system(), 200)
        except ValueError:
            abort(400, message="bad parameter")
            
class LibvirtHostInterfacesList(Resource):
           
    def get(self, driver):
        try:
            driver = to_driver(driver)
            list_all = to_bool(request.args.get('all', False))
            flag = int(request.args.get('flag', 0))
            return output_json(driver.list_host_interfaces(flag, list_all), 200)
        except ValueError:
            abort(400, message="bad parameter")    
            
class LibvirtHostInterfacesInspect(Resource):
           
    def get(self, driver, mac_or_name):
        try:
            driver = to_driver(driver)
            flag = int(request.args.get('flag', 0))
            return output_json(driver.inspect_host_interface(mac_or_name, flag), 200)
        except ValueError:
            abort(400, message="bad parameter")
