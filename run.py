# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is my Personality Quiz app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))
