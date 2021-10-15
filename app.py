from math import pi

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
    """
    Method to print 5 times an integer
    :param z: int. Integer to multiply
    """
    print(5 * z)


def f(z):
    print(6 * z)


def g(z):
    print(7 * z)


def h(z):
    print(8 * z)


def i(z):
    return 9 * z


def j(z):
    return 10 * z


def k(z):
    return 11 * z


def l(z):
    return 12 * z


def estIsocele(a, b, c):
    """
    Method to determine if a triangle is isocele or not
    """
    return (a == b )or (b == c) or (a == c)


def estEquilateral(a, b, c):
    return a == b and b == c


def perimetre(r):
    return 2 * pi * r


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
