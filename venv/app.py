import os
import openai
from Controller import chatgptadaptercontroller
from Controller import testController
from flask import Flask, jsonify, render_template
from flask_cors import CORS


# create and configure the app
app = Flask(__name__, instance_relative_config=True)
CORS(app)

os.environ['OPENAI_API_KEY'] = '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'
app.register_blueprint(chatgptadaptercontroller.bp)
app.register_blueprint(testController.bp)

# unrouted page
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)