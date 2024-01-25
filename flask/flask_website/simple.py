from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Kick the puppy!!</h1>'

@app.route('/page_2')
def page_2():
    return '<h1>Kick the puppy even more!!</h1>'


if __name__ == '__main__':
    app.run(debug=True)