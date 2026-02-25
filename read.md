# 📌 Module 9 – Support Module
Loan Service Provider Platform

## 📖 Overview

The Support Module handles customer interaction and issue resolution within the platform.  
It provides functionality for complaint management, chat support, contact requests, and FAQ retrieval.

This module is designed with scalable architecture using:

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic v2
- Swagger (/docs) for API testing

---

# 🏗 Architecture Flow

User → API Route → Schema Validation → ORM Model → Database → Response Model → User

All requests follow proper validation and database integration flow.

---

# 🔄 Functional Flow

## 1️⃣ Complaint Creation Flow

User submits complaint  
→ Data validated using Pydantic schema  
→ Complaint number generated  
→ SLA deadline set to 30 days  
→ Record stored in database  
→ Success response returned  

SLA Logic:
- SLA deadline = created_date + 30 days
- If current date > SLA deadline AND status not resolved
  → escalated = True

---

## 2️⃣ Complaint Retrieval Flow

GET /complaints  
→ Fetch all complaints  
→ Check SLA breach  
→ Auto-update escalation flag if needed  
→ Return structured response

GET /complaint/{id}  
→ Fetch specific complaint  
→ Apply escalation logic  
→ Return complaint details

---

## 3️⃣ Chat Support Flow

POST /chat/message  
→ Store user message in database  

GET /chat/history?user_id=1  
→ Retrieve chat history for specific user  

Relationship:
User (1) → (Many) ChatMessages

---

## 4️⃣ Contact Flow

POST /contact  
→ Public contact form  
→ Data validated  
→ Stored in database  

This is independent of user authentication.

---

## 5️⃣ FAQ Flow

GET /faqs  
→ Fetch frequently asked questions  
→ Return static support information  

---

# 🗄 Database Entities

## Users
- id (PK – BigInteger)
- email
- status

## Complaint
- id (PK)
- complaint_number
- user_id (FK → users.id)
- category
- subject
- description
- priority
- status
- sla_deadline
- escalated

## Chat_Message
- id (PK)
- user_id (FK → users.id)
- message
- created_at

## Contact_Message
- id (PK)
- name
- email
- subject
- message

## FAQ
- id (PK)
- question
- answer

---

# 🔗 Relationships

User → Complaint (1 : Many)  
User → ChatMessage (1 : Many)  

Contact and FAQ are independent entities.

---

# 🔐 Integration Details

✔ User Module integrated via user_id foreign key  
✔ Database integrated using SQLAlchemy ORM  
✔ Pydantic v2 compatible schemas  
✔ Swagger documentation enabled  
✔ SLA and Escalation logic implemented  

---

# 🚀 Current Status

- Ticket CRUD implemented  
- SLA tracking implemented (30 days)  
- Escalation logic implemented  
- Chat support implemented  
- Contact form implemented  
- Database relationships established  
- Integration testing completed  

---

# 📈 Future Enhancements (Optional)

- JWT Authentication
- Role-based access (Admin/User)
- Email/SMS notifications
- Pagination & filtering
- Complaint status update API
- Logging & monitoring

---

# 👨‍💻 Developer Notes

The Support module is designed as a loosely coupled system.  
It integrates with the User module and can be extended to integrate with Loan, Payment, and Notification modules in future.

This module follows scalable backend architecture principles and production-ready structure.