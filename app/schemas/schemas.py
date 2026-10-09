from pydantic import BaseModel, EmailStr
from typing import List, Optional, Any

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    message: str

class ContactResponse(BaseModel):
    success: bool
    message: str

class ProjectBase(BaseModel):
    title: str
    description: str
    category: str
    technologies: List[str]
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    image: Optional[str] = None
    featured: bool = False
    metrics: Optional[Any] = None

class ProjectResponse(ProjectBase):
    id: int

    class Config:
        orm_mode = True

class SkillBase(BaseModel):
    name: str
    category: str

class SkillResponse(SkillBase):
    id: int

    class Config:
        orm_mode = True
