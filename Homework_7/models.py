from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='students')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teacher', back_populates='subjects')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.now)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject = relationship('Subject', back_populates='grades')
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', back_populates='grades')

Group.students = relationship('Student', back_populates='group')
Teacher.subjects = relationship('Subject', back_populates='teacher')
Subject.grades = relationship('Grade', back_populates='subject')
Student.grades = relationship('Grade', back_populates='student')

