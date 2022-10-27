from flask import Flask
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Paul!'


@app.route('/animal/<users_animal>')
def fave_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'


if __name__ == '__main__':
    app.run(debug=True)
