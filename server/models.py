from config import db
from sqlalchemy_serializer import SerializerMixin
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
    db.Column("question_id", db.Integer, db.ForeignKey("questions.id")),
)

user_todo_list = db.Table(
    "user_todo_list",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("todo_list_id", db.Integer, db.ForeignKey("todo_lists.id")),
)



class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    groups = db.relationship("Group", secondary=user_group, backref="members")
    todo_lists = db.relationship("ToDoList", secondary=user_todo_list, backref="users")
    
    
    responses = db.relationship("Response", backref="user")

    serialize_rules = ("-groups.members", "-responses.user", "-responses.groups", "-todo_lists.users")
    def __repr__(self):
        return f'<User: "{self.name}">'
    

class Group(db.Model, SerializerMixin):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    meetings = db.relationship("Meeting", backref="group")
    serialize_rules = ("-members.groups", "-meetings.group")

    
    def __repr__(self):
        return f'<Group: "{self.name}">'


class Meeting(db.Model, SerializerMixin):
    __tablename__ = "meetings"

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    questions = db.relationship("Question", secondary=meeting_question, backref="meetings")
    
    serialize_rules = ("-questions.meetings",)
    

    def __repr__(self):
        return f'<Meeting: "{self.topic}">'


class Question(db.Model, SerializerMixin):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    #relationships: meetings | 
    responses = db.relationship("Response", backref="question")
    serialize_rules=("-meetings.questions", "-responses.question")

    def __repr__(self):
        return f'<StandupQuestion: "{self.description}">'


class Response(db.Model, SerializerMixin):
    __tablename__ = "responses"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))
    #relationship: question | user
    serialize_rules = ("-user.responses", "-question.responses", "-user.groups")


    def __repr__(self):
        return f'<StandupResponse: "{self.content} | ">'



class ToDoList(db.Model, SerializerMixin):
    __tablename__ = "todo_lists"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    items = db.relationship("ToDo", backref="todo_list")
   
    serialize_rules=("-items.todo_list", "-users.todo_lists")

    def __repr__(self):
        return f'<ToDo: "{self.description} | ">'


class ToDo(db.Model, SerializerMixin):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    completed = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    list_id = db.Column(db.Integer, db.ForeignKey("todo_lists.id"))
      

    serialize_rules=("-todo_list.items",)

    def __repr__(self):
        return f'<ToDo: "{self.description} | ">'
    


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




# class Task(db.Model, SerializerMixin):
#     __tablename__ = "tasks"

#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String)
#     completed = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
    
#     def __repr__(self):
#         return f'<Task: "{self.description} | ">'





# class Assignment(db.Model, SerializerMixin):
#     __tablename__ = "assignments"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     description = db.Column(db.String)
#     status = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     # relationship: users |
#     users = db.relationship("User", secondary=user_assignment, backref="assignments")
    
#     serialize_rules = ("-users.assignments",)
    
#     def __repr__(self):
#         return f'<Assignment: "{self.name} | ">'


# user_assignment = db.Table(
#     "user_assignment",
#     db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
#     db.Column("assignment_id", db.Integer, db.ForeignKey("assignments.id")),
# )