from sqlalchemy.orm import Session
from app.models.grievance import Grievance
from app.schemas.grievance_schema import GrievanceCreate
from app.repositories.grievance_repository import GrievanceRepository


class GrievanceService:

    def __init__(self):
        self.repo = GrievanceRepository()

    def create_grievance(self, db: Session, data: GrievanceCreate):

        grievance = Grievance(
            name=data.name,
            email=data.email,
            message=data.message
        )

        return self.repo.create(db, grievance)

    def get_all_grievances(self, db: Session):
        return self.repo.get_all(db)