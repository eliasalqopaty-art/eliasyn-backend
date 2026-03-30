from flask import Flask, request, jsonify
from database import SessionLocal, engine
import models
import auth  # استدعاء ملف الأمان

# إنشاء الجداول آلياً في قاعدة بيانات Render عند أول تشغيل
models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)

@app.route('/')
def home():
    return "Eliasyn System is Live and Secure!"

@app.route('/register_company', methods=['POST'])
def register():
    db = SessionLocal()
    try:
        data = request.json
        # إنشاء شركة جديدة مع ID فريد و API Key تلقائي
        new_company = models.Company(name=data['name'])
        db.add(new_company)
        db.commit()
        db.refresh(new_company)
        
        return jsonify({
            "message": "تم تسجيل الشركة بنجاح في الفندق الرقمي",
            "company_id": str(new_company.id),
            "api_key": new_company.api_key
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
