
# CI trigger test

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps Engineering Project  Production EKS Automation by Deepak kumar  is LIVE!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
