from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'


if __name__=='__main__':
    app.run(host='*', port=5000)
