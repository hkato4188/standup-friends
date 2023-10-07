#!/usr/bin/env python3

from app import app
from models import *


if __name__ == '__main__':
    with app.app_context():
        import ipdb
        
        users = User.query.all()
        groups = Group.query.all()
        
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
            


        ipdb.set_trace()
        pass