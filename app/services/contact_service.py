from sqlalchemy.orm import Session
from app.models.contact import Contact
from app.schemas.contact_schema import ContactCreate
from app.repositories.contact_repository import ContactRepository


class ContactService:

    def __init__(self):
        self.repo = ContactRepository()

    def create_contact(self, db: Session, data: ContactCreate):

        contact = Contact(
            name=data.name,
            email=data.email,
            message=data.message
        )

        return self.repo.create(db, contact)