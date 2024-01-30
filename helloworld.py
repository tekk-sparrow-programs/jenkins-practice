from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/home/<name>')
def home(name):
    return '<h1>Hello %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')