from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body style="background-color:orange; text-align:center;">
    <h1 style="color:white;">🚀 Hello from Python </h1>
    <h2 style="color:cyan;">Docker App Running on EC2 🚀</h2>
    </body>
    </html>
        """

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
