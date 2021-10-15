from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """
    Index page
    :return: None
    """
    return "Hello World!"


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    """
    Add two numbers and display the sum
    """
    return f"{a}+{b}={a+b}"


@app.route("/mult/<int:a>/<int:b>")
def mult(a, b):
    return f"{a}*{b}={a*b}"


@app.route("/subst/<int:a>/<int:b>")
def subst(a, b):
    return f"{a}-{b}={a-b}"


if __name__ == "__main__":
    app.run(debug=True)
