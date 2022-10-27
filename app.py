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


@app.route('/dessert/<users_dessert>')
def fave_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'


@app.route('/madlibs/<adjective>/<noun>')
def mad_lib(adjective, noun):
    return f'They jumped {adjective} into the {noun} with a quickness.'


# Tells Python how to run the server. Goes at the bottom of file.
if __name__ == '__main__':
    app.run(debug=True)
