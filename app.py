import os
import openai
from Controller import chatgptadaptercontroller
from flask import Flask, jsonify, render_template
from flask_cors import CORS


# create and configure the app
app = Flask(__name__)
CORS(app)

os.environ['OPENAI_API_KEY'] = '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'
app.register_blueprint(chatgptadaptercontroller.bp)

# unrouted page
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)