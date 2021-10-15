from flask import Flask

app = Flask(__name__)


def a(x):
    print(x)


def b(y):
    print(2 * y)


def c(z):
    print(3 * z)


def d(x) -> None:
    """

    :param x: int. parameter to be multiplied by 4
    """
    print(4 * x)


def e(z):
    print(5 * z)


def f(z):
    print(6 * z)


def g(z):
    print(7 * z)


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
