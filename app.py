from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/v1/hello")
def api_v1_hello():
    return "This is the first response"

if __name__ == "__main__":
    app.run(debug=True,port=80)