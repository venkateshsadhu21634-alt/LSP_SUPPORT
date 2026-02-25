from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import faq, chat, complaint, contact, grievance


Base.metadata.create_all(bind=engine)


app = FastAPI(title="LSP Support Module")

# Include all routers
app.include_router(faq.router)
app.include_router(chat.router)
app.include_router(complaint.router)
app.include_router(contact.router)
app.include_router(grievance.router)





