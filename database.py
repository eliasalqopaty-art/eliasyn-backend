from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# رابط الربط مع Supabase (تأكد من وضع كلمة السر الخاصة بك)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:YOUR-PASSWORD@db.igchzbsrhuoxyzlpokwc.supabase.co:5432/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"sslmode": "require"}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
