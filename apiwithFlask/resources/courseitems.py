from flask import Blueprint
from flask import abort,request
import uuid
from flask.views import MethodView
from db import specializations,course_items

blp=Blueprint("courseItems",__name__,desctiption="Operations")

@blp.route("/course_item/<string:course_item_id>")
class course_item(MethodView):
    def get(self,course_item_id):
        try:
            return course_items[course_item_id]
        except KeyError:
            abort(404, message = "Course item not found")
    def delete(self,course_item_id):
        try:
            del course_items[course_item_id]
            return{"message":"course item deleted"}
        except KeyError:
            abort(404,message="Course item not found")
    

@blp.route("/course_item")
class coureseItemlist(MethodView):
    def get_all_course_items():
         return {"course_items": list(course_items.values())}
    
    def post(self):
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