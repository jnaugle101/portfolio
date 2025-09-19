
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Flask</h1>"

if __name__ == "__main__":
    # Use PORT from env (Render sets this), else default to 5001 locally
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)




