from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False) # كلمة السر المشفرة
    # الربط بالشركة (كل مستخدم ينتمي لشركة واحدة فقط)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"))
