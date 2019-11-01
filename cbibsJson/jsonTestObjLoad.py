# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:26:42 2019

@author: Charles.Pellerin
"""

import json
from vo.CbibsStation import CbibsStation
import jsonpickle
import json

def load_data(file_name):
  with open(file_name, 'r') as file_data:
    return file_data.read()


def to_json(obj):
    return jsonpickle.encode(obj)

def jsonpickle_class_patch():
    old_processor = jsonpickle.unpickler.loadclass

    def loadclass(module_and_name, classes=None):
        ret = old_processor(module_and_name, classes)
        if ret is None:
            target_module, target_name = module_and_name.rsplit('.', 1)
            for class_path in classes:
                current_module, current_name = class_path.rsplit('.', 1)
                if current_name == target_name:
                    return classes[class_path]
        return ret

    jsonpickle.unpickler.loadclass = loadclass
    

# jsonpickle.encode will transform and object into a json string

def from_json2(class_type, json_str):
    #Get the class type from py/type
    type_dict_str = to_json(class_type)
    json_type_dict = json.loads(type_dict_str)
    print(json_type_dict)
    # Set the py/object with py/type from passed class
    json_dict = json.loads(json_str)
    json_dict.update({"py/object":json_type_dict}) # json_type_dict["py/type"]})
    return jsonpickle.decode(json.dumps(json_dict))

print("Starting \n");
jsonpickle_class_patch()
cbibsStationJson = load_data("rawJsonTest.txt")
# print(cbibsStationJson);
jsonic = json.loads(cbibsStationJson)
stationJson = jsonic['stations'][0];
print (stationJson)
# json_dict.update({"py/object": "module.Class"})
obj = CbibsStation()
testCbibsStation = from_json2(objp,json.dumps(stationJson))
print("Loaded the file \n");
print(type(testCbibsStation))
    
    