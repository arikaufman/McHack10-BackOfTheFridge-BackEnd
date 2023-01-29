import os
from Controller import chatgptadaptercontroller
from Controller import testController
from Controller import imageDetectionController
from flask import Flask, jsonify, render_template
from flask_cors import CORS


# create and configure the app
app = Flask(__name__)
CORS(app)

app.register_blueprint(chatgptadaptercontroller.bp)
app.register_blueprint(testController.bp)
app.register_blueprint(imageDetectionController.bp)
# unrouted page
@app.route('/')
def api():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)