from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy import func
from datetime import datetime
import re



# Models go here!

user_group = db.Table(
    "user_group",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id")),
)

meeting_question = db.Table(
    "meeting_question",
    db.Column("meeting_id", db.Integer, db.ForeignKey("meetings.id")),
    db.Column("standup_question_id", db.Integer, db.ForeignKey("standup_questions.id")),
)

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    groups = db.relationship("Group", secondary=user_group, backref="members")
    serialize_rules = ("-groups.members",)
    # answers = db.relationship("StandupResponse", backref="submitter")
    # serialize_rules = ("-groups.users", "-standup_responses.user")
    
    def __repr__(self):
        return f'<User: "{self.name}">'
    

class Group(db.Model, SerializerMixin):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    meetings = db.relationship("Meeting", backref="group_host")
    
    serialize_rules = ("-members.groups", "-questions.groups")
    def __repr__(self):
        return f'<Group: "{self.name}">'


class Meeting(db.Model, SerializerMixin):
    __tablename__ = "meetings"

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    standup_questions = db.relationship("StandupQuestion", secondary=meeting_question, backref="standup_meetings")
    serialize_rules = ("-group_host.meetings","-meeting.questions")
    
    def __repr__(self):
        return f'<Group: "{self.topic}">'


class StandupQuestion(db.Model, SerializerMixin):
    __tablename__ = "standup_questions"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # su_responses = db.relationship("StandupResponse", backref="su_question")
    serialize_rules=("-standup_meetings.standup_questions",)

    def __repr__(self):
        return f'<StandupQuestion: "{self.description}">'


# class StandupResponse(db.Model, SerializerMixin):
#     __tablename__ = "standup_responses"

#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     standup_question_id = db.Column(db.Integer, db.ForeignKey("standup_questions.id"))
    
#     serialize_rules = ("-user.standup_responses", "-standup_questions.standup_responses")


#     def __repr__(self):
#         return f'<StandupResponse: "{self.content} | ">'
















# class Assignment(db.Model, SerializerMixin):
#     __tablename__ = "assignments"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     description = db.Column(db.String)
#     completed = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
    
#     def __repr__(self):
#         return f'<Assignment: "{self.name} | ">'


# class Task(db.Model, SerializerMixin):
#     __tablename__ = "tasks"

#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String)
#     status = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
    
#     def __repr__(self):
#         return f'<Task: "{self.description} | ">'


# class ToDo(db.Model, SerializerMixin):
#     __tablename__ = "toDos"

#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String)
#     status = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
    
#     def __repr__(self):
#         return f'<ToDo: "{self.description} | ">'
    

# class DiscussionQuestion(db.Model, SerializerMixin):
#     __tablename__ = "discussion_questions"

#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String)
#     rating = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
    
#     def __repr__(self):
#         return f'<DiscussionQuestion: "{self.description} | ">'

# class DiscussionResponse(db.Model, SerializerMixin):
#     __tablename__ = "discussion_responses"

#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
    
#     def __repr__(self):
#         return f'<DiscussionResponse: "{self.description} | ">'




