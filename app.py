
import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "DevOps Demo")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/", methods=["GET"])
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Demo Application</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #101827;
                color: white;
                text-align: center;
                padding: 80px 20px;
            }}
            .card {{
                max-width: 550px;
                margin: auto;
                padding: 35px;
                background: #1e293b;
                border-radius: 15px;
            }}
            .status {{
                color: #4ade80;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>DevOps Demo Application</h1>
            <p>Welcome! Your application is running.</p>
            <p class="status">● Application Status: Running</p>
            <p>Version: {APP_VERSION}</p>
            <p>Managed using Python, Flask and DevOps tools.</p>
        </div>
    </body>
    </html>
    """


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "application": APP_NAME,
        "version": APP_VERSION
    }), 200


@app.route("/version", methods=["GET"])
def version():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION
    }), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
