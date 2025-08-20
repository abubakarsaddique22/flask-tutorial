from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return f'<h1>welcome to homepage</h1>'

@app.route('/welcome/<name>')
def welcome(name):
    return f'Hi {name},your welcome to webpage'



if __name__=='__main__':
    app.run(debug=True)