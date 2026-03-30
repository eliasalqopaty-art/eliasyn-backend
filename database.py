from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# جلب الرابط السري لقاعدة البيانات من إعدادات Render
DATABASE_URL = os.environ.get("DATABASE_URL")

# إصلاح بسيط لنوع الرابط إذا كان يبدأ بـ postgres://
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# المحرك الذي يدير الاتصالات
engine = create_engine(DATABASE_URL)

# الجلسة التي نستخدمها لإرسال واستقبال البيانات
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# القاعدة التي تبنى عليها كل الجداول
Base = declarative_base()
