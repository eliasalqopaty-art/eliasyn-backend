from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database

app = FastAPI(title="Eliasyn System")

# كود فحص بسيط للتأكد أن السيرفر يعمل
@app.get("/")
def home():
    return {"message": "نظام إلياسين يعمل بنجاح، أهلاً بك يا إلياس"}

# نقطة استقبال بيانات المسح (Scan)
@app.get("/check/{batch_num}")
def check_medicine(batch_num: str, db: Session = Depends(database.get_db)):
    batch = db.query(models.Batch).filter(models.Batch.batch_num == batch_num).first()
    if not batch:
        return {"status": "error", "message": "الدواء غير مسجل في النظام"}
    return {
        "medicine": batch.medicine_name,
        "expiry": batch.expiry_date,
        "is_safe": not batch.is_recalled
    }
