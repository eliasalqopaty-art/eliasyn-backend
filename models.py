from sqlalchemy import Column, String, Boolean, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_name = Column(String, nullable=False)
    api_key = Column(String, unique=True)

class Batch(Base):
    __tablename__ = "batches"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"))
    medicine_name = Column(String, nullable=False)
    batch_num = Column(String, nullable=False)
    expiry_date = Column(Date, nullable=False)
    is_recalled = Column(Boolean, default=False)
