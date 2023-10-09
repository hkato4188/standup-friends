#!/usr/bin/env python3

from app import app
from models import *


if __name__ == '__main__':
    with app.app_context():
        import ipdb
        
        users = User.query.all()
        groups = Group.query.all()
        meetings = Meeting.query.all()
        questions = Question.query.all()
        responses = Response.query.all()
        todos = ToDo.query.all()
        todo_lists = ToDoList.query.all()



        u1 = users[0]
        u2 = users[1]
        u3 = users[2]
        u4 = users[3]
        u5 = users[4]
        g1 = groups[0]
        g2 = groups[1]
        g3 = groups[2]
        g4 = groups[3]
        g5 = groups[4]
        m1 = meetings[0]
        m2 = meetings[1]
        m3 = meetings[2]
        m4 = meetings[3]
        m5 = meetings[4]
        q1 = questions[0]
        q2 = questions[1]
        q3 = questions[2]
        q4 = questions[3]
        q5 = questions[4]
        r1 = responses[0]
        r2 = responses[1]
        r3 = responses[2]
        r4 = responses[3]
        r5 = responses[4]
        t1 = todos[0]
        t2 = todos[1]
        t3 = todos[2]
        t4 = todos[3]
        t5 = todos[4]
        list1 = todo_lists[0]
        list2 = todo_lists[1]
        list3 = todo_lists[2]
        list4 = todo_lists[3]
        list5 = todo_lists[4]


        ipdb.set_trace()
        pass