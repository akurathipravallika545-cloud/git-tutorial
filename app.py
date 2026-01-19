from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>Docker App</title>
        <style>
          body {
            background-color: black;
            color: lime;
            font-family: Arial;
            text-align: center;
            margin-top: 100px;
          }
          h1 {
            color: cyan;
          }
          p {
            color: orange;
            font-size: 20px;
          }
        </style>
      </head>
      <body>
        <h1>🚀 Docker App Running on EC2</h1>
        <p>Colored Output from Flask + Docker</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

