import os
from Controller import chatgptadaptercontroller
from Controller import testController
from Domain import imageDetectionDomain
from flask import Flask, jsonify, render_template
from flask_cors import CORS


# create and configure the app
app = Flask(__name__)
CORS(app)

os.environ['OPENAI_API_KEY'] = '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'
app.register_blueprint(chatgptadaptercontroller.bp)
app.register_blueprint(testController.bp)
# unrouted page
@app.route('/')
def api():
    imageDetectionDomain.detectGroceries()
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)