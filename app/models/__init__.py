# models package
# Import submodules so SQLAlchemy model classes get registered with Base
from . import user,  faq, complaint, chat, grievance

__all__ = [
	"user",
	"faq",
	"complaint",
	"chat",
	"grievance",
]
