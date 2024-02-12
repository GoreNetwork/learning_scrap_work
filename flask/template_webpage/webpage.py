from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    to_kick = ['puppy', 'kitten', 'baby', 'toddler', 'teenager', 'adult', 'elderly']
    return render_template('kick.html', to_kick=to_kick)

@app.route('/puppies/<name>')
def puppies(name):
    """Kick the puppy whose name is name
    http://127.0.0.1:5000/puppies/chewy and the "name" in the list is chewy"""
    to_kick = [name, 'puppy', 'kitten', 'baby', 'toddler', 'teenager', 'adult', 'elderly']
    return render_template('kick.html', to_kick=to_kick)


if __name__ == '__main__':
    app.run(debug=True) 