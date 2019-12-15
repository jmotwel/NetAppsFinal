from flask import Flask, jsonify
from flask import request, render_template
from flask import make_response



app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')



if __name__=='__main__':

    app.run(debug=True, port=8000, host='0.0.0.0')
