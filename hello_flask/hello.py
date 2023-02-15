from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media2.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif?cid=ecf05e47cv0vuugp6tyye6jbfuvxvoupk1jl50sxnpnf6kpe&rid=giphy.gif&ct=g" width= 200px>'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return("Bye")


@app.route("/username/<name>/<int:number>")
def greeting():
    return(f"Hi,{name}, you are {number} years old!")


if __name__ == "__main__":
    app.run(debug=True)
