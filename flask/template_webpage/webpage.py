from flask import Flask, render_template, request

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

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signedup')
def signedup():
    email = request.args.get('email')
    name = request.args.get('name')
    password = request.args.get('password')
    return render_template('signedup.html', name=name, email=email, password=password)

if __name__ == '__main__':
    app.run() 