#!/usr/bin/env python

from config import ENGINE
from models.testmate import *
from sqlalchemy.org import sessionmaker
from sqlalchemy import create_engine

class UserManager(object):

    def __init__(self):
        self.__engine = create_engine(ENGINE)
        self.__session = sessionmaker(bind=self.__engine)

    def addUser(self, userid, email):
        user = User(id=userid, email=email)
        self.__session.add(user)
        self.__session.commit()

    def removeUser(self, userid):
        try:
            user = self.__session.query(User).filter_by(id=userid).first()
            session.delete(user)
            self.__session.commit()
        except:
            pass

class ProjectManager(object):
    
    def __init__(self):
        self.__engine = create_engine(ENGINE)
        self.__session = sessionmaker(bind=self.__engine)

    def addProject(self, proj_id, name):
        proj = Project(id = proj_id, name = name, last_test_id = 0)
        self.__session.add(proj)
        self.__session.commit()

class AssociationManager(object):

    def __init__(self):
        self.__engine = create_engine(ENGINE)
        self.__session = sessionmaker(bind=self.__engine)

    def __getAllProjects(self):
        projects = self.__session.query(Project).all();
        returm projects

    def associateProject(self, userid, proj_id):
        user = self.__session.query(User).filter(id=userid).first()
        project = self.__session.query(Project).filter(id=proj_id).first()
        assoc = ProjectAccess(user=user, project=project)
        self.__session.add(assoc)
        self.__session.commit()
