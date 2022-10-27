from flask import Flask
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Paul!'


if __name__ == '__main__':
    app.run(debug=True)
