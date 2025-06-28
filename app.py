from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Updated from fake pipeline v2!!!, for new!"

if __name__ == "__main__":
    print("🚀 Flask v2 loaded!")
    app.run(host="0.0.0.0", port=80)
    
