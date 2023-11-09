#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import *

fake = Faker()


langs = ["Ruby", "Python", "Java", "JavaScript", "SQL", "Docker",
         "Kubernetes", "Stripe", "Google", "Server", "Dashboard"]
items = ["data structures", "models", "database", "views",
         "routes", "calls", "network", "api", "repo", "migration"]
goal = ["complete", "review", "update", "audit",
        "approve", "remediate", "overhaul", "implement"]


def create_users():
    # u1 = User(email="breellejordyn@gmail.com", name="BreElle Wells")
    # u2 = User(email="hirokikato1@gmail.com", name="Hiro Kato")

    # users = [u1, u2]
    users = []

    name_list = []
    for _ in range(50):
        name = fake.name()
        while name in name_list:
            name = fake.name()
        name_list.append(name)
        u = User(
            name=name,
            email=fake.email(),
            password_hash="millythecat1",
        )
        users.append(u)
    return users


def create_groups():
    groups = []
    for n in range(25):
        g = Group(
            name=f"Group: {n+1}",
        )
        groups.append(g)

    return groups


def create_meetings():
    meetings = []
    for n in range(25):
        m = Meeting(
            topic=f"Meeting: {n+1}"
        )
        meetings.append(m)

    return meetings


def create_standup_questions():
    questions = []
    for _ in range(25):
        sq = Question(
            description=f"Standup: talk about {rc(langs)} {rc(items)} and {rc(goal)}"
        )
        questions.append(sq)
    return questions


def create_standup_responses():
    responses = []
    for _ in range(25):
        res_text = fake.texts(nb_texts=1, max_nb_chars=500)[0]
        res = Response(
            content=res_text
        )
        responses.append(res)

    return responses


def create_todos():
    td = []
    status = [True, False]
    for _ in range(75):
        t = ToDo(
            description=fake.text(),
            completed=rc(status),
        )
        td.append(t)

    return td


def create_todo_lists():
    tdl = []

    for n in range(30):
        t = ToDoList(
            description=f"{rc(langs)} {rc(goal)} tickets"
        )
        tdl.append(t)

    return tdl


def create_discussion_topics():
    dq_topics = []

    for n in range(20):
        dq = DiscussionTopic(
            content=f"What do you think of {rc(langs)} {rc(items)}?",
            rating=randint(1, 5)
        )
        dq_topics.append(dq)
    return dq_topics


def create_discussion_responses():
    dq_responses = []
    for n in range(20):
        dqr = DiscussionResponse(
            content=f"What do you think of {rc(langs)} {rc(items)}?"

        )
        dq_responses.append(dqr)
    return dq_responses


if __name__ == "__main__":
    fake = Faker()
    with app.app_context():
        print("Clearing db...")
        db.drop_all()

        print("Creating tables...")
        db.create_all()

        print("Starting seed...")
        print("-----------------")

        print("Seeding users...")
        users = create_users()
        db.session.add_all(users)
        db.session.commit()
        print("-----------------")

        print("Seeding groups...")
        groups = create_groups()
        db.session.add_all(groups)
        db.session.commit()
        print("-----------------")

        print("Adding users to groups...")
        users = User.query.all()
        groups = Group.query.all()
        for n in range(0, 15):
            users[n].groups.append(groups[n])
            print(f"added user:{n} to group:{n}")
        db.session.commit()
        print("-----------------")

        print("Seeding meetings...")
        meetings = create_meetings()
        db.session.add_all(meetings)
        db.session.commit()
        print("-----------------")

        print("Adding meetings to groups...")
        meetings = Meeting.query.all()
        for n in range(0, 25):
            meetings[n].group = groups[n]
            print(f"added meeting:{n} to group:{n}")
        db.session.commit()
        print("-----------------")

        print("Seeding standup_questions...")
        questions = create_standup_questions()
        db.session.add_all(questions)
        db.session.commit()
        print("-----------------")

        print("Adding standup questions to meeting agendas...")
        standup_questions = Question.query.all()
        for n in range(0, 25):
            meetings[n].questions.append(standup_questions[n])
            print(f"added meeting:{n} to meeting:{n}")
        db.session.commit()
        print("-----------------")

        print("Seeding standup_responses...")
        responses = create_standup_responses()
        db.session.add_all(responses)
        db.session.commit()
        print("-----------------")

        print("Adding standup responses to standup questions...")
        for su_response in responses:
            su_response.user_id = rc([user.id for user in users])
            su_response.question_id = rc(
                [question.id for question in questions])
        db.session.commit()
        print("-----------------")

        print("Seeding user todos...")
        td = create_todos()
        db.session.add_all(td)
        db.session.commit()
        print("-----------------")

        print("Seeding user todo lists...")
        pres = ToDoList(description="Presentation Outline")
        testu = User.query.first()
        pres.users.append(testu)
        db.session.add(pres)
        db.session.commit()
        tdl = create_todo_lists()
        db.session.add_all(tdl)
        db.session.commit()
        print("-----------------")

        print("Adding todo items to their respective lists...")
        tdlists = ToDoList.query.all()
        for t in ToDo.query.all():
            t.list_id = rc([tdl.id for tdl in tdlists])
            t.list_id = rc([tdl.id for tdl in tdlists])
        db.session.commit()
        print("-----------------")

        print("Adding todo lists to users...")

        for tdl in tdlists:
            tdl.users.append(rc([user for user in users]))
        for tdl in tdlists:
            tdl.users.append(rc([user for user in users]))
        db.session.commit()
        print("-----------------")

        print("Seeding discussion topics...")
        topics = create_discussion_topics()
        db.session.add_all(topics)
        db.session.commit()
        print("-----------------")

        print("Seeding discussion responses...")
        dq_res = create_discussion_responses()
        db.session.add_all(dq_res)
        db.session.commit()
        print("-----------------")

        print("Adding discussion responses to discussion topics...")
        dq_responses = DiscussionResponse.query.all()
        dq_topics = DiscussionTopic.query.all()

        for dqr in dq_responses:
            dqr.user_id = rc([user.id for user in users])
            dqr.discussion_topic_id = rc([topic.id for topic in dq_topics])
        db.session.commit()
        print("-----------------")

        print("Done seeding!")
