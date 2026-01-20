from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background-color: #0f172a;
                color: white;
                font-family: Arial;
                text-align: center;
                margin-top: 80px;
            }
            h1 {
                color: #38bdf8;
            }
            p {
                color: #4ade80;
                font-size: 22px;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Docker Flask App</h1>
        <p>Running from GitHub → EC2 → Docker</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

