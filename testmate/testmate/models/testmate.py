#!/usr/bin/env python

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Text, Sequence, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Represents a TestMate user.
class User(Base):
    __tablename__ = 'users'
    id = Column(String(8), primary_key=True)
    email = Column(String(30))
    access = relationship("ProjectAccess")
    acl = relationship("AccessControl")
    testcase = relationship("TestCase")
    #testrun = relationship("TestRun")

# Represents a project under testmate.
class Project(Base):
    __tablename__ = 'projects'
    id = Column(String(10), primary_key=True)
    name = Column(String(30))
    last_test_id = Column(Integer)
    access = relationship("ProjectAccess")
    testcase = relationship("TestCase")
    testsuite = relationship("TestSuite")
    #testrun = relationship("TestRun")
    build = relationship("Build")
    version = relationship("Version")

# Holds which user has access to which projects.
class ProjectAccess(Base):
    __tablename__ = 'projectaccess'
    id = Column(Integer, Sequence('seq_assoc_id', start=1, increment=1), primary_key=True)
    user = Column(String(8), ForeignKey('users.id'))
    project = Column(String(10), ForeignKey('projects.id'))
    

# Holds which user can do what.
class AccessControl(Base):
    __tablename__ = 'acl'
    id = Column(Integer, primary_key=True)
    user = Column(String(8), ForeignKey('users.id'))
    role = Column(Integer)

# Builds numbers nad projects
class Build(Base):
    __tablename__ = "builds"
    pkey = Column(Integer, primary_key=True)
    id = Column(String(20))
    project = Column(String(10), ForeignKey('projects.id'))

# Versions of projects
class Version(Base):
    __tablename__ = 'versions'
    pkey = Column(Integer, primary_key=True)
    version = Column(String(20))
    project = Column(String(10), ForeignKey('projects.id'))


# Represents a test suite
class TestSuite(Base):
    __tablename__ = 'testsuites'
    id = Column(Integer, primary_key=True)
    proj = Column(String(10), ForeignKey('projects.id'))
    name = Column(String(50))
    parent = Column(Integer, nullable=True)
    testcase = relationship("TestCase")

# Represents a test case
class TestCase(Base):
    __tablename__ = 'testcases'
    id = Column(Integer, primary_key=True)
    summary = Column(String(100))
    creator = Column(String(8), ForeignKey('users.id'))
    creation_time = Column(DateTime, default=func.now())
    project = Column(String(10), ForeignKey('projects.id'))
    version = Column(String(20))
    parent = Column(Integer, ForeignKey('testsuites.id'))
    steps = Column(Text)
