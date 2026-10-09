import sys
import os

# Add the parent directory to sys.path so we can import 'app'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database.connection import SessionLocal, engine, Base
from app.models.models import Project, Skill

# Make sure tables exist
Base.metadata.create_all(bind=engine)

db = SessionLocal()

def seed_data():
    # Add Skills
    skills = [
        {"name": "Python", "category": "Programming"},
        {"name": "SQL", "category": "Programming"},
        {"name": "JavaScript", "category": "Programming"},
        
        {"name": "Scikit-learn", "category": "Machine Learning"},
        {"name": "Pandas", "category": "Machine Learning"},
        {"name": "NumPy", "category": "Machine Learning"},
        {"name": "Matplotlib", "category": "Machine Learning"},
        {"name": "Feature Engineering", "category": "Machine Learning"},
        {"name": "Model Evaluation", "category": "Machine Learning"},
        {"name": "Hyperparameter Tuning", "category": "Machine Learning"},
        
        {"name": "TensorFlow", "category": "Deep Learning"},
        {"name": "Keras", "category": "Deep Learning"},
        {"name": "ANN", "category": "Deep Learning"},
        {"name": "CNN", "category": "Deep Learning"},
        {"name": "Transfer Learning", "category": "Deep Learning"},
        {"name": "Backpropagation", "category": "Deep Learning"},
        {"name": "Regularization", "category": "Deep Learning"},
        
        {"name": "OpenCV", "category": "Computer Vision"},
        {"name": "Image Classification", "category": "Computer Vision"},
        {"name": "Image Preprocessing", "category": "Computer Vision"},
        {"name": "Object Detection Basics", "category": "Computer Vision"},
        
        {"name": "LLMs", "category": "Generative AI"},
        {"name": "Prompt Engineering", "category": "Generative AI"},
        {"name": "RAG Architecture", "category": "Generative AI"},
        {"name": "LangChain", "category": "Generative AI"},
        {"name": "Vector DBs (Chroma/FAISS)", "category": "Generative AI"},
        
        {"name": "Git", "category": "Tools & Environments"},
        {"name": "GitHub", "category": "Tools & Environments"},
        {"name": "Google Colab", "category": "Tools & Environments"},
        {"name": "VS Code", "category": "Tools & Environments"},
        {"name": "Jupyter Notebook", "category": "Tools & Environments"},
        {"name": "Linux Environment", "category": "Tools & Environments"},
    ]

    for skill in skills:
        db_skill = Skill(name=skill["name"], category=skill["category"])
        db.add(db_skill)

    # Add Projects
    projects = [
        {
            "title": "Phishing URL Detection",
            "description": "Machine learning system to classify malicious and phishing URLs.",
            "category": "Machine Learning",
            "technologies": ["Python", "Scikit-learn", "Random Forest"],
            "github_url": "https://github.com",
            "live_url": None,
            "featured": True
        },
        {
            "title": "Computer Vision Image Classification",
            "description": "Deep learning image classification system using transfer learning with a pretrained CNN architecture. Employs aggressive data augmentation pipelines, fine-tuned dense layers, and dropout regularization to achieve high generalization accuracy on compact datasets.",
            "category": "Deep Learning",
            "technologies": ["TensorFlow", "Keras", "MobileNetV2", "Transfer Learning", "CNN", "Data Augmentation"],
            "github_url": "https://github.com",
            "live_url": None,
            "featured": True
        },
        {
            "title": "Home Loan Default Prediction",
            "description": "Machine learning project focused on analyzing customer profiles and historical credit characteristics to predict loan default risk. Features deep demographic stratification, missing data imputation, outlier elimination, and gradient-boosted decision trees.",
            "category": "Machine Learning",
            "technologies": ["Exploratory Data Analysis", "Data Cleaning", "Feature Engineering", "Classification", "Model Evaluation", "Customer Segmentation"],
            "github_url": "https://github.com",
            "live_url": None,
            "featured": True
        }
    ]

    for project in projects:
        db_project = Project(**project)
        db.add(db_project)

    db.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    # Check if DB is already seeded
    if db.query(Skill).count() == 0:
        seed_data()
    else:
        print("Database already seeded.")
