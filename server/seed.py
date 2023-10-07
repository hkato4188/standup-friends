#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import *

fake = Faker()



def create_users():
    u1 = User(email="breellejordyn@gmail.com", name="BreElle Wells")
    u2 = User(email="hirokikato1@gmail.com", name="Hiro Kato")
    db.session.add_all([u1,u2])
    db.session.commit()

    users = [u1, u2]

    name_list = []
    for _ in range(50):
        name = fake.name()
        while name in name_list:
            name = fake.name()
        name_list.append(name)
        u = User(
            name=name,
            email=fake.email()
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
            topic=f"Meeting: {n+1}",
        )
       meetings.append(m)

    return meetings

def create_standup_questions():
    questions = []
    for n in range(25):
        sq = StandupQuestion(
            description=fake.text(),
        )
        questions.append(sq)
    return questions


# def create_standup_responses():
#     questions = []
#     for n in range(20):
#         sq = StandupQuestion(
#             description=fake.text(),
#             user_id=rc([user.id for user in users]),
#             post_id=rc([post.id for post in posts]),
#         )
#         questions.append(sq)

#     return questions


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
        for n in range(0,15):
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
        groups = Group.query.all()
        for n in range(0,15):
            meetings[n].group_host = groups[n]
            print(f"added meeting:{n} to group:{n}")
        db.session.commit()
        print("-----------------")

        print("Seeding standup_questions...")
        standup_questions = create_standup_questions()
        db.session.add_all(standup_questions)
        db.session.commit()
        print("-----------------")

        print("Adding standup questions to meeting agendas...")
        meetings = Meeting.query.all()
        standup_questions = StandupQuestion.query.all()
        for n in range(0,15):
            meetings[n].standup_questions.append(standup_questions[n])
            print(f"added meeting:{n} to group:{n}")
        db.session.commit()
        print("-----------------")


#         print("Seeding standup_answers...")
#         standup_answers = create_standup_answers()
#         db.session.add_all(standup_answers)
#         db.session.commit()
#         print("-----------------")
        

        print("Done seeding!")
