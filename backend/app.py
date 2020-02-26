from flask import Flask
app = Flask(__name__)

# base directory of the app
@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

# api request for image processing
# retuns json of boxes of cats
@app.route('/api/upload', methods=['POST'])
def upload_image():
    file = request.files['file']

if __name__ == '__main__':
    app.run(debug=True)
