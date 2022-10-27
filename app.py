from flask import Flask
import random
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
app = Flask(__name__)


@app.route('/')
def homepage():
    # My name is Paul, actually.
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/animal/<users_animal>')
def fave_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'


@app.route('/dessert/<users_dessert>')
def fave_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'


@app.route('/madlibs/<adjective>/<noun>')
def mad_lib(adjective, noun):
    return f'They jumped {adjective} into the {noun} with a quickness.'


@app.route('/multiply/<number1>/<number2>')
def multiply_two_nums(number1, number2):
    if number1.isdigit() & number2.isdigit():
        return f'{number1} times {number2} is {int(number1)*int(number2)}'
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers!'


@app.route('/sayntimes/<word>/<number>')
def say_n_times(word, number):
    if number.isdigit() is False:
        return 'Invalid input. Please try again by entering a word and a number!'
    else:
        repeat_str = ''
        for i in range(int(number)):
            repeat_str += word + ' '
        return repeat_str


@app.route('/dicegame')
def dicegame():
    random_number = random.randint(1, 6)
    if random_number == 6:
        return 'You rolled a 6. You won!'
    else:
        return f'You rolled a {random_number}. You lost!'


# Tells Python how to run the server. Goes at the bottom of file.
if __name__ == '__main__':
    app.run(debug=True)
