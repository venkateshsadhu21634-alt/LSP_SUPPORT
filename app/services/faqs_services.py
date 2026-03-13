from sqlalchemy.orm import Session
from app.repositories.faq_repository import FAQRepository


class FAQService:

    def __init__(self):
        self.repo = FAQRepository()

    def get_all_faqs(self, db: Session):
        return self.repo.get_all(db)

    def get_faq_by_category(self, db: Session, category: str):
        return self.repo.get_by_category(db, category)