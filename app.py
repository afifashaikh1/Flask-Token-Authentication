from flask import Flask
import jwt

app = Flask(__name__)

# secret key
SECRET_KEY = 'mysecretkey'

# 🔹 Your token (already added)
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJleHAiOjE3NzYwNTQxMzB9.DFPgtBB0cl2uGuwFJIZ9JHra4FSZBzgI-0qu2gAQpZk"

# Home
@app.route('/')
def home():
    return "Flask Token Auth Running 🚀"

# 🔒 Protected route (no need to pass token now)
@app.route('/protected')
def protected():
    try:
        jwt.decode(TOKEN, SECRET_KEY, algorithms=["HS256"])
        return "✅ Access Granted (Token Verified)"
    except:
        return "❌ Invalid Token"

if __name__ == '__main__':
    app.run(debug=True)