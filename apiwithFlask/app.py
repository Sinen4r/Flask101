from flask import *
import uuid
from db import *

app = Flask(__name__)

#specializations = [{"name": "IT", "course_items": [{"name": "Web Services", "type": "Mandatory"}]}]

#updated
@app.get("/specialization")
def get_specializations():
    return {"specializations": list(specializations.values())}

#updated
@app.post("/specialization")
def create_specialization():
    specialization_data = request.get_json()
    if "name" not in specialization_data:
        abort(400, message = "BAD REQUEST, Ensure 'name' is included is included in the JSON file")
    for specialization in specializations.values():
        if specialization_data["name"] == specialization["name"]:
            abort(400, message = "Specialization Already Exists")
    
    specialization_id = uuid.uuid4().hex
    specialization = {**specialization_data, "id":specialization_id}
    specializations[specialization_id] = specialization
    #new_specialization = {"name": request_data["name"], "course_items": []}
    #specializations.append(new_specialization)
    return specialization, 201

#updated
#@app.post("/specialization/<string:name>/course_item")
@app.post("/course_item")
def create_course_item():
    course_item_data = request.get_json()
    if(
        "type" not in course_item_data or "name" not in course_item_data or "specialization_id" not in course_item_data
    ):
        abort(400, message = "BAD REQUEST. Ensure 'Type', 'name', and 'id' are included in the JSON file")
    for course_item in course_items.values():
        if(course_item_data["name"] == course_item["name"] and course_item_data["specialization_id"] == course_item["specialization_id"] ):
            abort(400, message = "This Course Item Already Exists")
    course_item_id = uuid.uuid4().hex
    if course_item_data["specialization_id"] not in specializations:
        #return {"message": "Specialization not found"}, 404
        abort(404, message = "Specialization not found")
    course_item = {**course_item_data, "id": course_item_id}
    course_items[course_item_id] = course_item
    return course_item, 201
    #for specialization in specializations:
        #if specialization["name"] == name:
            #new_course_item = {"name": request_data["name"], "type": request_data["type"]}
            #specialization["course_items"].append(new_course_item)
            #return new_course_item, 201
    #return {"message": "Specialization not found"}, 404

#updated
@app.get("/specialization/<string:specialization_id>")
def get_specialization(specialization_id):
    try: 
        return specializations[specialization_id]
    except KeyError:
        #return {"message": "Specialization not found"}, 404
        abort(404, message = "Specialization not found")
    #for specialization in specializations:
        #if specialization["name"] == name:
            #return specialization
    #return {"message": "Specialization not found"}, 404

#newly created
@app.get("/course_item")
def get_all_course_items():
    return {"course_items": list(course_items.values())}

#updated
@app.get("/course_item/<string:course_item_id>")
#def get_course_item_in_specialization(name):
def get_course_item(course_item_id):
    try:
        return course_items[course_item_id]
    except KeyError:
        abort(404, message = "Course item not found")
        #return {"message": "Course item not found"}, 404
# @app.get("/course_item/<specilazation_id>")
# def get_all_course_items_of_Specialization(specilazation_id):
#     try:
#         t={}
#         for id in course_items:
#             if course_items[specilazation_id]==id:
#                 t[id["name"]]=id["name"]
#         return t
            
            
    except KeyError:
        abort(404,message="specialization not found")
    #for specialization in specializations:
        #if specialization["name"] == name:
            #return {"course_items": specialization["course_items"]}
    

@app.delete("/course_item/<string:corse_item_id>")
def delete_course_item(corse_item_id):
    try:
        del course_items[corse_item_id]
        return{"message":"course item deleted"}
    except KeyError:
        abort(404,message="Course item not found")




if __name__== "__main__":
    app.run(debug=True)