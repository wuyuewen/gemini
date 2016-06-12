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
        "LibvirtList",
        "LibvirtCreate",
        "LibvirtInspect",
        "LibvirtStop",
        "LibvirtDestroy",
        "LibvirtStart",
        "LibvirtRestart",
        "LibvirtDelete",
        "LibvirtSuspend",
        "LibvirtResume",
        "LibvirtAttachDevice",
        "LibvirtResizeMemory",
        "LibvirtResizeVcpu",
           ]

class LibvirtList(Resource):
    
    def get(self, driver):
        try:
            driver = to_driver(driver) 
            list_all = to_bool(request.args.get('all', False))
            flag = int(request.args.get('flag', 0))
            return output_json(driver.list_nodes(flag, list_all), 200)
        except ValueError:
            abort(400, message="bad parameter")

class LibvirtCreate(Resource):
          
    def post(self, driver):
        driver = to_driver(driver)
        json_data = request.get_json(force=True)
        vm_uuid = driver.create_node(json_data)
        return output_json({"Uuid": vm_uuid, "Warnings": []}, 201)
       
class LibvirtInspect(Resource):
           
    def get(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            flag = int(request.args.get('flag', 0))
            return output_json(driver.inspect_node(uuid_or_name, flag), 200)
        except ValueError:
            abort(400, message="bad parameter")
               
class LibvirtStart(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            flag = int(request.args.get('flag', 0))
            return output_json(driver.start_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
               
class LibvirtStop(Resource):
    
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver) 
            flag = int(request.args.get('flag', 0))
            return output_json(driver.stop_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
            
class LibvirtDestroy(Resource):
    
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver) 
            flag = int(request.args.get('flag', 0))
            return output_json(driver.stop_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
   
class LibvirtRestart(Resource):
    
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            flag = int(request.args.get('flag', 0))
            return output_json(driver.restart_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")
               
class LibvirtDelete(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            flag = int(request.args.get('flag', 0))
            return output_json(driver.delete_node(uuid_or_name, flag), 204)
        except ValueError:
            abort(400, message="bad parameter")        

class LibvirtSuspend(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            return output_json(driver.suspend_node(uuid_or_name), 204)
        except ValueError:
            abort(400, message="bad parameter")       
            
class LibvirtResume(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            return output_json(driver.resume_node(uuid_or_name), 204)
        except ValueError:
            abort(400, message="bad parameter")   
            
class LibvirtAttachDevice(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            json_data = request.get_json(force=True)
            flag = int(request.args.get('flag', 0))
            return output_json(driver.attach_device(uuid_or_name, json_data, flag), 201)
        except ValueError:
            abort(400, message="bad parameter") 
            
class LibvirtResizeMemory(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            memory = int(request.args.get('size', 0))
            memory_type = request.args.get('type', None)
            flag = int(request.args.get('flag', 0))
            if not memory or not memory_type:
                abort(400, message="bad parameter")
            return output_json(driver.resize_memory(uuid_or_name, memory, memory_type, flag), 204)
        except ValueError:
            abort(400, message="bad parameter") 
            
class LibvirtResizeVcpu(Resource):
           
    def post(self, driver, uuid_or_name):
        try:
            driver = to_driver(driver)
            vcpu = int(request.args.get('size', 0))
            flag = int(request.args.get('flag', 0))
            if not vcpu:
                abort(400, message="bad parameter")
            return output_json(driver.resize_cpu(uuid_or_name, vcpu, flag), 204)
        except ValueError:
            abort(400, message="bad parameter") 
