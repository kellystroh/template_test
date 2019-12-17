from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('01-homepage.html')

@app.route('/post', methods=['GET'])
def post():
    return render_template('02-Single-post.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('03-About-me.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('04-Contact.html')

@app.route('/soon', methods=['GET'])
def soon():
    return render_template('05-Coming-soon.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)