"""
Chapter 3: Algorithms & Complexity — Interactive Study Dashboard
Flask Web Server
"""

import os
from pathlib import Path
from flask import Flask, render_template, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = BASE_DIR / "templates" if (BASE_DIR / "templates").exists() else BASE_DIR

app = Flask(__name__, template_folder=str(TEMPLATE_DIR), static_folder=str(BASE_DIR))

@app.route("/")
def index():
    if (BASE_DIR / "templates" / "index.html").exists():
        return render_template("index.html")
    return send_from_directory(str(BASE_DIR), "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Chapter 3 Algorithms Dashboard on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
