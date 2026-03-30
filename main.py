from flask import Flask, request, jsonify
from database import SessionLocal, engine
import models

# إنشاء الجداول في قاعدة البيانات لأول مرة
models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)

@app.route('/register_company', methods=['POST'])
def register():
    data = request.json
    db = SessionLocal()
    
    # إنشاء شركة جديدة
    new_company = models.Company(name=data['name'])
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    
    return jsonify({
        "message": "تم تسجيل الشركة بنجاح",
        "company_id": str(new_company.id),
        "api_key": new_company.api_key # هذا هو مفتاح شقتهم!
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
