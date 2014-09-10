#!/usr/bin/python

import pytest
from testmate.models.testmate import *
from testmate.usermanagement import *


class TestUserManager:
    def test_addUser(self):
        user_mgr = UserManager()
        user = user_mgr.addUser('user1', 'user1@domain.dom')
        assert (user.id == 'user1' and user.email == 'user1@domain.dom')

    def test_addUser_session(self):
        user_mgr = UserManager()
        assert user_mgr._getSession().query(User).count() == 1

    def test_removeUser(self):
        user_mgr = UserManager()
        user_mgr.removeUser('user1')
        assert user_mgr._getSession().query(User).count() == 0

class TestProjectManager:
    def test_addProject(self):
        proj_mgr = ProjectManager()
        proj = proj_mgr.addProject('MEG', 'McAfee Email Gateway')
        assert (proj.id == 'MEG' and proj.name ==  'McAfee Email Gateway')

    def test_addProject_session(self):
        proj_mgr = ProjectManager()
        assert proj_mgr._getSession().query(Project).count() == 1

    def test_removeProject(self):
        proj_mgr = ProjectManager()
        proj_mgr.removeProject('MEG')
        assert proj_mgr._getSession().query(Project).count() == 0
