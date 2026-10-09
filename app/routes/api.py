from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any

from app.database.connection import get_db
from app.models.models import Contact, Project, Skill
from app.schemas.schemas import ContactCreate, ContactResponse, ProjectResponse, SkillResponse

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.post("/contact", response_model=ContactResponse)
def submit_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    if len(contact.message) > 5000:
        raise HTTPException(status_code=400, detail="Message too long")
    db_contact = Contact(name=contact.name, email=contact.email, message=contact.message)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return {"success": True, "message": "Message sent successfully"}

@router.get("/projects", response_model=List[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return projects

@router.get("/projects/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.get("/skills")
def get_skills(db: Session = Depends(get_db)):
    skills = db.query(Skill).all()
    # Group by category
    skills_by_category: Dict[str, List[SkillResponse]] = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append({
            "id": skill.id,
            "name": skill.name,
            "category": skill.category
        })
    return skills_by_category

@router.get("/resume")
def get_resume():
    # Since we don't have a real resume file right now, we can just return a simple text file or 
    # mock response. In a real app we would use FileResponse
    from fastapi.responses import FileResponse
    import os
    resume_path = os.path.join(os.path.dirname(__file__), "..", "..", "resume.pdf")
    if os.path.exists(resume_path):
        return FileResponse(resume_path, filename="Kenil_Bhadani_Resume.pdf")
    
    # Fallback if resume is missing
    return {"error": "Resume file not found on server"}
