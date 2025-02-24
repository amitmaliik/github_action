# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, GitHub Actions!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# tests/test_app.py
def test_hello():
    assert True

# requirements.txt
flask==2.0.1
pytest==7.0.1
