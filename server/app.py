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
        groups_dict = [group.to_dict(only=("id","name","meetings.id","meetings.topic","members.id","members.name")) for group in groups]
        return make_response(groups_dict, 200)
    
    def post(Resource):
        data = request.get_json()
        try:
            new_group = Group(name=data.get("name"))
            if new_group.validation_errors:
                raise Exception(new_group.validation_errors)
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
                    errors = group.validation_errors
                    group.clear_validation_errors()
                    raise Exception(errors)
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
                errors = new_meeting.validation_errors
                new_meeting.clear_validation_errors()
                raise Exception(errors)
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
                    errors = meeting.validation_errors
                    meeting.clear_validation_errors()
                    raise Exception(errors)
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


class Questions(Resource):
    def get(self):
        questions = Question.query.all()
        questions_dict = [question.to_dict() for question in questions]
        return make_response(questions_dict, 200)
    
    def post(Resource):
        data = request.get_json()
        new_question = Question(description=data["description"])
        if new_question.validation_errors:
                errors = new_question.validation_errors
                new_question.clear_validation_errors()
                raise Exception(errors)
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
                    errors = question.validation_errors
                    question.clear_validation_errors()
                    raise Exception(errors)
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


class Responses(Resource):
    def get(self):
        responses = Response.query.all()
        responses_dict = [response.to_dict() for response in responses]
        return make_response(responses_dict, 200)
    
    def post(Resource):
        data = request.get_json()
        new_response = Response(content=data["content"], user_id=data["user_id"])
        if new_response.validation_errors:
                errors = new_response.validation_errors
                new_response.clear_validation_errors()
                raise Exception(errors)
        try:  
            db.session.add(new_response)
            db.session.commit()
            response_dict = new_response.to_dict()
            return make_response(response_dict, 201)
        except:
            errors = new_response.validation_errors
            new_response.clear_validation_errors()
            return make_response({"errors": errors},422)
        
class Responses_By_Id(Resource):
    def get(self, id):
        response = Response.query.filter(Response.id == id).first()
        if response:
            response_dict = response.to_dict()
            return make_response(response_dict, 200)
        else:
            return make_response({"error": "Response not found."},404)

    def patch(self,id):
        response = Response.query.filter(Response.id == id).first()
        if response:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(response, attr, data[attr]) 
                if response.validation_errors:
                    errors = response.validation_errors
                    response.clear_validation_errors()
                    raise Exception(errors)
                db.session.add(response)
                db.session.commit()
                response_dict = response.to_dict()
                return make_response(response_dict, 202)
            except:
                errors = response.validation_errors
                response.clear_validation_errors()
                return make_response({"error": errors}, 422)
        else:
            return make_response({"error": "Response not found."},404)
    
    def delete(self, id):
        response = Response.query.filter(Response.id == id).first()
        if response:
            db.session.delete(response)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "Response not found"}, 404)

class ToDoLists(Resource):
    def get(self):
        tdlists = ToDoList.query.all()
        lists_dict = [list.to_dict() for list in tdlists]
        return make_response(lists_dict, 200)
    
    def post(Resource):
        data = request.get_json()
        new_list = ToDoList(description=data["description"])
        if new_list.validation_errors:
                errors = new_list.validation_errors
                new_list.clear_validation_errors()
                raise Exception(errors)
        try:  
            db.session.add(new_list)
            db.session.commit()
            list_dict = new_list.to_dict()
            return make_response(list_dict, 201)
        except:
            errors = new_list.validation_errors
            new_list.clear_validation_errors()
            return make_response({"errors": errors},422)
        
class ToDoLists_By_Id(Resource):
    def get(self, id):
        list = ToDoList.query.filter(ToDoList.id == id).first()
        
        if list:
            list_dict = list.to_dict()
            return make_response(list_dict, 200)
        else:
            return make_response({"error": "List not found."},404)

    def patch(self,id):
        list = ToDoList.query.filter(ToDoList.id == id).first()
        if list:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(list, attr, data[attr]) 
                if list.validation_errors:
                    errors = list.validation_errors
                    list.clear_validation_errors()
                    raise Exception(errors)
                db.session.add(list)
                db.session.commit()
                list_dict = list.to_dict()
                return make_response(list_dict, 202)
            except:
                errors = list.validation_errors
                list.clear_validation_errors()
                return make_response({"error": errors}, 422)
        else:
            return make_response({"error": "List not found."},404)
    
    def delete(self, id):
        list = ToDoList.query.filter(Response.id == id).first()
        if list:
            db.session.delete(list)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "List not found"}, 404)

class ToDos(Resource):
    def get(self):
        tds = ToDo.query.all()
        td_dict = [td.to_dict() for td in tds]
        return make_response(td_dict, 200)
    
    def post(Resource):
        data = request.get_json()
        new_td = ToDo(description=data["description"], completed="False", list_id=data["list_id"])
        if new_td.validation_errors:
                errors = new_td.validation_errors
                new_td.clear_validation_errors()
                raise Exception(errors)
        try:  
            db.session.add(new_td)
            db.session.commit()
            todo_dict = new_td.to_dict()
            return make_response(todo_dict, 201)
        except:
            errors = new_td.validation_errors
            new_td.clear_validation_errors()
            return make_response({"errors": errors},422)
        
class ToDos_By_Id(Resource):
    def get(self, id):
        td = ToDo.query.filter(ToDo.id == id).first()
        if td:
            td_dict = td.to_dict()
            return make_response(td_dict, 200)
        else:
            return make_response({"error": " not found."},404)

    def patch(self,id):
        td = ToDo.query.filter(ToDo.id == id).first()
        if td:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(td, attr, data[attr]) 
                if td.validation_errors:
                    errors = td.validation_errors
                    td.clear_validation_errors()
                    raise Exception(errors)
                db.session.add(td)
                db.session.commit()
                td_dict = td.to_dict()
                return make_response(td_dict, 202)
            except:
                errors = td.validation_errors
                td.clear_validation_errors()
                return make_response({"error": errors}, 422)
        else:
            return make_response({"error": " not found."},404)
    
    def delete(self, id):
        td = ToDo.query.filter(ToDo.id == id).first()
        if td:
            db.session.delete(td)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "ToDo item not found"}, 404)

class DiscussionTopics(Resource):
    def get(self):
        dts = DiscussionTopic.query.all()
        dt_dict = [dt.to_dict() for dt in dts]
        return make_response(dt_dict, 200)
    
    def post(Resource):
        data = request.get_json()
        new_dt = DiscussionTopic(content=data["content"], rating=data["rating"])
        if new_dt.validation_errors:
                errors = new_dt.validation_errors
                new_dt.clear_validation_errors()
                raise Exception(errors)
        try:  
            db.session.add(new_dt)
            db.session.commit()
            discussion_topic_dict = new_dt.to_dict()
            return make_response(discussion_topic_dict, 201)
        except:
            errors = new_dt.validation_errors
            new_dt.clear_validation_errors()
            return make_response({"errors": errors},422)
        
class DiscussionTopics_By_Id(Resource):
    def get(self, id):
        dt = DiscussionTopic.query.filter(DiscussionTopic.id == id).first()
        if dt:
            dt_dict = dt.to_dict()
            return make_response(dt_dict, 200)
        else:
            return make_response({"error": "Discussion topic not found."},404)

    def patch(self,id):
        dt = DiscussionTopic.query.filter(DiscussionTopic.id == id).first()
        if dt:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(dt, attr, data[attr]) 
                if dt.validation_errors:
                    errors = dt.validation_errors
                    dt.clear_validation_errors()
                    raise Exception(errors)
                db.session.add(dt)
                db.session.commit()
                dt_dict = dt.to_dict()
                return make_response(dt_dict, 202)
            except:
                errors = dt.validation_errors
                dt.clear_validation_errors()
                return make_response({"error": errors}, 422)
        else:
            return make_response({"error": "Discussion topic not found."},404)
    
    def delete(self, id):
        dt = DiscussionTopic.query.filter(DiscussionTopic.id == id).first()
        if dt:
            db.session.delete(dt)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "Discussion topic item not found"}, 404)

class DiscussionResponses(Resource):
    def get(self):
        drs = DiscussionTopic.query.all()
        dr_dict = [dr.to_dict() for dr in drs]
        return make_response(dr_dict, 200)
    
    def post(Resource):
        data = request.get_json()
        new_dr = DiscussionResponse(content=data["content"], user_id=data["user_id"], discussion_topic_id=data["discussion_topic_id"])
        if new_dr.validation_errors:
                errors = new_dr.validation_errors
                new_dr.clear_validation_errors()
                raise Exception(errors)
        try:  
            db.session.add(new_dr)
            db.session.commit()
            discussion_response_dict = new_dr.to_dict()
            return make_response(discussion_response_dict, 201)
        except:
            errors = new_dr.validation_errors
            new_dr.clear_validation_errors()
            return make_response({"errors": errors},422)
        
class DiscussionResponses_By_Id(Resource):
    def get(self, id):
        dr = DiscussionResponse.query.filter(DiscussionResponse.id == id).first()
        if dr:
            dr_dict = dr.to_dict()
            return make_response(dr_dict, 200)
        else:
            return make_response({"error": "Discussion response not found."},404)

    def patch(self,id):
        dr = DiscussionResponse.query.filter(DiscussionResponse.id == id).first()
        if dr:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(dr, attr, data[attr]) 
                if dr.validation_errors:
                    errors = dr.validation_errors
                    dr.clear_validation_errors()
                    raise Exception(errors)
                db.session.add(dr)
                db.session.commit()
                dr_dict = dr.to_dict()
                return make_response(dr_dict, 202)
            except:
                errors = dr.validation_errors
                dr.clear_validation_errors()
                return make_response({"error": errors}, 422)
        else:
            return make_response({"error": "Discussion response not found."},404)
    
    def delete(self, id):
        dr = DiscussionResponse.query.filter(DiscussionResponse.id == id).first()
        if dr:
            db.session.delete(dr)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "Discussion response item not found"}, 404)



class Users(Resource):
    def get(self):
        users = User.query.all()
        users_dict = [user.to_dict() for user in users]
        return make_response(users_dict, 200)
    
    def post(Resource):
        data = request.get_json()
        try:
            new_user = User(name=data["name"], email=data["email"])
            if new_user.validation_errors:
              errors = new_user.validation_errors
              new_user.clear_validation_errors()                
              raise Exception(errors)
            else: 
                db.session.add(new_user)
                db.session.commit()
                user_dict = new_user.to_dict()
                return make_response(user_dict, 201)
        except:
            errors = new_user.validation_errors
            new_user.clear_validation_errors()
            return make_response({"errors": errors},422)
        
class Users_By_Id(Resource):
    def get(self,id):
        user = User.query.filter(User.id == id).first()
        if user:
            user_dict = user.to_dict()
            return make_response(user_dict, 200)
        else:
            return make_response({"error": "User not found."},404)

    def patch(self,id):
        user = User.query.filter(User.id == id).first()
        if user:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(user, attr, data[attr]) 
                if user.validation_errors:
                    errors = user.validation_errors
                    user.clear_validation_errors()
                    raise Exception(errors)
                db.session.add(user)
                db.session.commit()
                user_dict = user.to_dict()
                return make_response(user_dict, 202)
            except:
                errors = user.validation_errors
                user.clear_validation_errors()
                return make_response({"error": errors}, 422)
        else:
            return make_response({"error": "User not found."},404)
    
    def delete(self, id):
        user = User.query.filter(User.id == id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response({}, 204)
        else:
            return make_response({"error": "User not found"}, 404)


api.add_resource(Groups, "/groups")
api.add_resource(Groups_By_Id, "/groups/<int:id>")
api.add_resource(Meetings, "/meetings")
api.add_resource(Meetings_By_Id, "/meetings/<int:id>")
api.add_resource(Questions, "/questions")
api.add_resource(Questions_By_Id, "/questions/<int:id>")
api.add_resource(Responses, "/responses")
api.add_resource(Responses_By_Id, "/responses/<int:id>")
api.add_resource(ToDoLists, "/todolists")
api.add_resource(ToDoLists_By_Id, "/todolists/<int:id>")
api.add_resource(ToDos, "/todos")
api.add_resource(ToDos_By_Id, "/todos/<int:id>")
api.add_resource(DiscussionTopics, "/discussion_topics")
api.add_resource(DiscussionTopics_By_Id, "/discussion_topics/<int:id>")
api.add_resource(DiscussionResponses, "/discussion_responses")
api.add_resource(DiscussionResponses_By_Id, "/discussion_responses/<int:id>")
api.add_resource(Users, "/users")
api.add_resource(Users_By_Id, "/users/<int:id>")





if __name__ == '__main__':
    app.run(port=5555, debug=True)

