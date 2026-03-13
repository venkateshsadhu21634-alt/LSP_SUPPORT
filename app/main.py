from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import faq, chat, complaint, contact, grievance


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="LSP Support Module API",
    description="Support APIs for Loan Service Provider Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "LSP Support Module API is running"}



app.include_router(faq.router, prefix="/api/v1/support", tags=["FAQ"])
app.include_router(chat.router, prefix="/api/v1/support/chat", tags=["Chat"])
app.include_router(complaint.router, prefix="/api/v1/support", tags=["Complaint"])
app.include_router(contact.router, prefix="/api/v1/support", tags=["Contact"])
app.include_router(grievance.router, prefix="/api/v1/support", tags=["Grievance"])