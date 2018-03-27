"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.form['person']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Show user the madlibs form!"""

    wants_game = request.args.get("wants_game")
    colors = ['blue', 'purple', 'fuchsia']
    pets = ['dog', 'cat', 'rabbit', 'pony', 'cockroach']
    if wants_game == "True":
        return render_template("game.html",
                               colors=colors,
                               pets=pets)
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Shows the completed madlib form!!"""

    person = request.args.get("person")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    color = request.args.get("color")
    pets = request.args.getlist("pets")

    # files = ["madlib.html", "madlibs1.html"]
    # madlib_choice = choice(files)

    return render_template("madlib.html",
                           person=person,
                           color=color,
                           noun=noun,
                           adjective=adjective,
                           pets=pets)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
