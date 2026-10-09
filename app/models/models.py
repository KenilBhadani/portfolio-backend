from sqlalchemy import Column, Integer, String, Boolean, JSON
from app.database.connection import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    message = Column(String)

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    category = Column(String, index=True)
    technologies = Column(JSON)
    github_url = Column(String, nullable=True)
    live_url = Column(String, nullable=True)
    image = Column(String, nullable=True)
    featured = Column(Boolean, default=False)
    metrics = Column(JSON, nullable=True)

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
