from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random

from app.models.complaint import Complaint
from app.schemas.complaint_schema import ComplaintCreate
from app.repositories.complaint_repository import ComplaintRepository


class ComplaintService:

    def __init__(self):
        self.repo = ComplaintRepository()

    def create_complaint(self, db: Session, data: ComplaintCreate):

        complaint_number = "CMP-" + str(random.randint(10000, 99999))
        sla_deadline = datetime.utcnow() + timedelta(days=30)

        complaint = Complaint(
            complaint_number=complaint_number,
            user_id=data.user_id,
            category=data.category,
            subject=data.subject,
            description=data.description,
            priority=data.priority,
            status="Open",
            sla_deadline=sla_deadline,
            escalated=False
        )

        return self.repo.create(db, complaint)

    def get_all_complaints(self, db: Session):

        complaints = self.repo.get_all(db)

        for c in complaints:
            if c.status not in ["Resolved", "Closed"] and datetime.utcnow() > c.sla_deadline:
                c.escalated = True

        db.commit()

        return complaints

    def get_complaint(self, db: Session, complaint_id: int):

        complaint = self.repo.get_by_id(db, complaint_id)

        if not complaint:
            return None

        if complaint.status not in ["Resolved", "Closed"] and datetime.utcnow() > complaint.sla_deadline:
            complaint.escalated = True
            db.commit()

        return complaint