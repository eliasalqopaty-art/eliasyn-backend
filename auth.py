from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

# 1. إعداد أداة التشفير (تخيلها كآلة خلط الأدوية)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 2. مفتاح سري خاص بك (غيره بكلمات عشوائية لزيادة الأمان)
SECRET_KEY = "Eliasyn_Secret_Safe_Key_2026"
ALGORITHM = "HS256"

# وظيفة لتشفير كلمة السر قبل حفظها في قاعدة البيانات
def get_password_hash(password):
    return pwd_context.hash(password)

# وظيفة للتأكد من صحة كلمة السر عند تسجيل الدخول
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# وظيفة لإنشاء "بطاقة دخول مؤقتة" (Token) للموظف
def create_access_token(data: dict):
    to_encode = data.copy()
    # تنتهي صلاحية البطاقة بعد 24 ساعة لزيادة الأمان
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
