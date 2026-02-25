from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.faq import FAQ

router = APIRouter(prefix="/api/v1/faqs", tags=["FAQ"])


@router.get("/")
def get_faqs(db: Session = Depends(get_db)):
    return db.query(FAQ).all()


