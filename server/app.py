#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, jsonify, make_response, session
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import *


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Groups(Resource):
    def get(self):
        groups = Group.query.all()
        groups_dict = [group.to_dict() for group in groups]
        return make_response(groups_dict, 200)
    
    def post(Resource):
        data = request.get_json()
        try:
            new_group = Group(name=data.get("name"))
            if new_group.validation_errors:
                raise ValueError 
            else: 
                db.session.add(new_group)
                db.session.commit()
                group_dict = new_group.to_dict()
                return make_response(group_dict, 201)
        except:
            errors = new_group.validation_errors
            new_group.clear_validation_errors()
            return make_response({"errors": errors},422)
        
class Groups_By_Id(Resource):
    def get(self,id):
        group = Group.query.filter(Group.id == id).first()
        if group:
            group_dict = group.to_dict()
            return make_response(group_dict, 200)
        else:
            return make_response({"error": "Group not found."},404)

    def patch(self,id):
        group = Group.query.filter(Group.id == id).first()
        if group:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(group, attr, data[attr]) 
                if group.validation_errors:
                    raise ValueError
                db.session.add(group)
                db.session.commit()
                group_dict = group.to_dict()
                return make_response(group_dict, 202)
            except:
                errors = group.validation_errors
                group.clear_validation_errors()
                return make_response({"error": errors}, 422)
        else:
            return make_response({"error": "Group not found."},404)
    
    def delete(self, id):
        group = Group.query.filter(Group.id == id).first()
        if group:
            db.session.delete(group)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "Group not found"}, 404)


class Meetings(Resource):
    def get(self):
        meetings = Meeting.query.all()
        meetings_dict = [meeting.to_dict() for meeting in meetings]
        return make_response(meetings_dict, 200)
    
    def post(Resource):
        data = request.get_json()
        new_meeting = Meeting(topic=data["topic"], group_id=data["group_id"])
        try:  
            if new_meeting.validation_errors:
                raise ValueError 
            db.session.add(new_meeting)
            db.session.commit()
            meeting_dict = new_meeting.to_dict()
            return make_response(meeting_dict, 201)
        except:
            errors = new_meeting.validation_errors
            new_meeting.clear_validation_errors()
            return make_response({"errors": errors},422)
        
class Meetings_By_Id(Resource):
    def get(self,id):
        meeting = Meeting.query.filter(Meeting.id == id).first()
        if meeting:
            meeting_dict = meeting.to_dict()
            return make_response(meeting_dict, 200)
        else:
            return make_response({"error": "Meeting not found."},404)

    def patch(self,id):
        meeting = Meeting.query.filter(Meeting.id == id).first()
        if meeting:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(meeting, attr, data[attr]) 
                if meeting.validation_errors:
                    raise ValueError
                db.session.add(meeting)
                db.session.commit()
                meeting_dict = meeting.to_dict()
                return make_response(meeting_dict, 202)
            except:
                errors = meeting.validation_errors
                meeting.clear_validation_errors()
                return make_response({"error": errors}, 422)
        else:
            return make_response({"error": "Meeting not found."},404)
    
    def delete(self, id):
        meeting = Meeting.query.filter(Meeting.id == id).first()
        if meeting:
            db.session.delete(meeting)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "Meeting not found"}, 404)




api.add_resource(Groups, "/groups")
api.add_resource(Groups_By_Id, "/groups/<int:id>")
api.add_resource(Meetings, "/meetings")
api.add_resource(Meetings_By_Id, "/meetings/<int:id>")







class Questions(Resource):
    def get(self):
        questions = Question.query.all()
        questions_dict = [question.to_dict() for question in questions]
        return make_response(questions_dict, 200)
    
    def post(Resource):
        data = request.get_json()
        new_question = Question(description=data["description"])
        if new_question.validation_errors:
                raise ValueError 
        try:  
            db.session.add(new_question)
            db.session.commit()
            question_dict = new_question.to_dict()
            return make_response(question_dict, 201)
        except:
            errors = new_question.validation_errors
            new_question.clear_validation_errors()
            return make_response({"errors": errors},422)
        
class Questions_By_Id(Resource):
    def get(self, id):
        question = Question.query.filter(Question.id == id).first()
        if question:
            question_dict = question.to_dict()
            return make_response(question_dict, 200)
        else:
            return make_response({"error": "Question not found."},404)

    def patch(self,id):
        question = Question.query.filter(Question.id == id).first()
        if question:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(question, attr, data[attr]) 
                if question.validation_errors:
                    raise ValueError
                db.session.add(question)
                db.session.commit()
                question_dict = question.to_dict()
                return make_response(question_dict, 202)
            except:
                errors = question.validation_errors
                question.clear_validation_errors()
                return make_response({"error": errors}, 422)
        else:
            return make_response({"error": "Question not found."},404)
    
    def delete(self, id):
        question = Question.query.filter(Question.id == id).first()
        if question:
            db.session.delete(question)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "Question not found"}, 404)


api.add_resource(Questions, "/questions")
api.add_resource(Questions_By_Id, "/questions/<int:id>")


















if __name__ == '__main__':
    app.run(port=5555, debug=True)

