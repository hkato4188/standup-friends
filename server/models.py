from config import db
from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.ext.associationproxy import association_proxy
# from sqlalchemy.ext.hybrid import hybrid_property
# from sqlalchemy.orm import validates
# from sqlalchemy import func
# from datetime import datetime
# import re



# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    def __repr__(self):
        return f'<User: "{self.name}">'
    


class Group(db.Model, SerializerMixin):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        return f'<Group: "{self.name}">'



class Assignment(db.Model, SerializerMixin):
    __tablename__ = "assignments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    completed = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        return f'<Assignment: "{self.name} | ">'


class Task(db.Model, SerializerMixin):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    status = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        return f'<Task: "{self.description} | ">'


class ToDo(db.Model, SerializerMixin):
    __tablename__ = "toDos"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    status = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        return f'<ToDo: "{self.description} | ">'
    

class DiscussionQuestion(db.Model, SerializerMixin):
    __tablename__ = "discussion_questions"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    rating = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        return f'<DiscussionQuestion: "{self.description} | ">'

class DiscussionResponse(db.Model, SerializerMixin):
    __tablename__ = "discussion_responses"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        return f'<DiscussionResponse: "{self.description} | ">'


class StandupQuestion(db.Model, SerializerMixin):
    __tablename__ = "standup_questions"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        return f'<StandupQuestion: "{self.description} | ">'


class StandupResponse(db.Model, SerializerMixin):
    __tablename__ = "standup_responses"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        return f'<StandupResponse: "{self.description} | ">'

