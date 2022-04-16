from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

data = [
    {
      "id":"0"
    }
]

@app.route('/')
def homepage():
    global data
    return render_template('homepage.html', data=data)

if __name__ == '__main__':
   app.run(debug = True)

