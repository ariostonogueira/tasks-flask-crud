from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Olá, seja bem-vindo ao Flask!"


@app.route("/about")
def about():
    return "Sobre o Flask!"


if __name__ == "__main__":
    app.run(debug=True)
