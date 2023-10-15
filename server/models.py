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
    groups = db.relationship("Group", secondary=user_group, backref="members")
    todo_lists = db.relationship("ToDoList", secondary=user_todo_list, backref="users")
    responses = db.relationship("Response", backref="user")
    discussion_responses = db.relationship("DiscussionResponse", backref="submitter")
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    serialize_rules = ("-groups.members", "-responses.user", "-todo_lists.users", "-discussion_responses.submitter")
    
    def __repr__(self):
        return f'<User: "{self.name}">'

    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []
    
    @validates('name')
    def validate_name(self, db_column, name):
        if isinstance(name, str) and name:
            return name
        else:
            self.validation_errors.append('Name must be a string and be at least one character long.')

    @validates("email")
    def validate_email(self, db_column, email):
        all_emails = [user.email for user in User.query.all()]
        email_regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

        if email in all_emails:
            self.validation_errors.append("Email address is already registered.")
        elif not re.fullmatch(email_regex, email):
            self.validation_errors.append("Please enter a valid email.")
        elif re.fullmatch(email_regex, email) and not email in all_emails:
            return email
    

class Group(db.Model, SerializerMixin):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    meetings = db.relationship("Meeting", backref="group")
    #relationship: members
    serialize_rules = ("-members.groups", "-meetings.group")
  
    def __repr__(self):
        return f'<Group: "{self.name}">'

    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []
    
    @validates('name')
    def validate_name(self, db_column, name):
        if isinstance(name, str) and name:
            return name
        else:
            self.validation_errors.append('Name must be a string and be at least one character long.')



class Meeting(db.Model, SerializerMixin):
    __tablename__ = "meetings"

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    questions = db.relationship("Question", secondary=meeting_question, backref="meetings")
    #relationship: group
    serialize_rules = ("-questions.meetings", "-group.meetings")
    

    def __repr__(self):
        return f'<Meeting: "{self.topic}">'

    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []
    
    @validates('topic')
    def validate_topic(self, db_column, topic):
        if isinstance(topic, str) and topic:
            return topic
        else:
            self.validation_errors.append('Please provide the topic for the meeting.')
    
    @validates("group_id")
    def validate_group(self, db_column, group_id):
        group = Group.query.filter(Group.id == group_id).first()
        if group:
            return group_id
        else:
            self.validation_errors.append("Group not found.")


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

    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []
    
    @validates('description')
    def validate_description(self, db_column, description):
        if isinstance(description, str) and len(description)>=15:
            return description
        else:
            self.validation_errors.append('Please provide a more detailed question description.')
    

class Response(db.Model, SerializerMixin):
    __tablename__ = "responses"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))
    #relationship: question | user
    serialize_rules = ("-user.responses", "-question.responses")

    def __repr__(self):
        return f'<StandupResponse: "{self.content} | ">'

    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []
    
    @validates('content')
    def validate_content(self, db_column, content):
        if isinstance(content, str) and len(content)>=300:
            return content
        else:
            self.validation_errors.append('Responses must be at least 300 characters long. Please provide more detail and substance to your response.')
    
    @validates("user_id")
    def validate_user(self, db_column, user_id):
        user = User.query.filter(User.id == user_id).first()
        if user:
            return user_id
        else:
            self.validation_errors.append("User not found.")

    @validates("question_id")
    def validate_question(self, db_column, question_id):
        question = Question.query.filter(Question.id == question_id).first()
        if question:
            return question_id
        else:
            self.validation_errors.append("Question not found.")


class ToDoList(db.Model, SerializerMixin):
    __tablename__ = "todo_lists"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    items = db.relationship("ToDo", backref="todo_list", cascade="all, delete")
   
    serialize_rules=("-items.todo_list", "-users.todo_lists")

    def __repr__(self):
        return f'<ToDo: "{self.description} | ">'

    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []
    
    @validates('description')
    def validate_description(self, db_column, description):
        if isinstance(description, str) and description:
            return description
        else:
            self.validation_errors.append('Please describe your todo list with a short sentence.')
    

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
    
    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []
    
    @validates('description')
    def validate_description(self, db_column, description):
        if isinstance(description, str) and description:
            return description
        else:
            self.validation_errors.append('Please briefly describe your todo item with a short sentence.')

    @validates('completed')
    def validate_completed(self, db_column, completed):
        status = ["true", "false"]
        if isinstance(completed, str) and completed.lower() in status:
            return completed
        else:
            self.validation_errors.append('Please enter True or False for the status of your todo item.')

    @validates("list_id")
    def validate_list(self, db_column, list_id):
        list = ToDoList.query.filter(ToDoList.id == list_id).first()
        if list:
            return list_id
        else:
            self.validation_errors.append("ToDo list not found.")

class DiscussionTopic(db.Model, SerializerMixin):
    __tablename__ = "discussion_topics"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    rating = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    discussion_responses = db.relationship("DiscussionResponse", backref="discussion_topic")
    
    serialize_rules=("-discussion_responses.discussion_topic",)
    
    def __repr__(self):
        return f'<DiscussionTopic: "{self.content} | ">'

    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []
    
    @validates('content')
    def validate_content(self, db_column, content):
        if isinstance(content, str) and content:
            return content
        else:
            self.validation_errors.append('Please briefly describe your discussion topic.')

    @validates('rating')
    def validate_rating(self, db_column, rating):
        
        if isinstance(rating, int) and rating in range(1,6):
            return rating
        else:
            self.validation_errors.append('Please select a rating value between 1 - 5.')

class DiscussionResponse(db.Model, SerializerMixin):
    __tablename__ = "discussion_responses"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id")) 
    discussion_topic_id = db.Column(db.Integer, db.ForeignKey("discussion_topics.id")) 
    serialize_rules = ("-submitter.discussion_responses", "-discussion_topic.discussion_responses")
#    relationship: submitter
    def __repr__(self):
        return f'<DiscussionResponse: "{self.content} | ">'

    validation_errors = []

    @classmethod
    def clear_validation_errors(cls):
        cls.validation_errors = []
    
    @validates('content')
    def validate_content(self, db_column, content):
        if isinstance(content, str) and content:
            return content
        else:
            self.validation_errors.append('Please briefly describe your discussion topic.')


    @validates("user_id")
    def validate_user(self, db_column, user_id):
        user = User.query.filter(User.id == user_id).first()
        if user:
            return user_id
        else:
            self.validation_errors.append("User not found.")

    @validates("discussion_topic_id")
    def validate_discussion_topic(self, db_column, discussion_topic_id):
        discussion_topic = DiscussionTopic.query.filter(DiscussionTopic.id == discussion_topic_id).first()
        if discussion_topic:
            return discussion_topic_id
        else:
            self.validation_errors.append("Discussion topic not found.")