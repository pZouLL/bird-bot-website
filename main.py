from flask import Flask , redirect , url_for , render_template , request , session , flash , send_file
from datetime import timedelta
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/commands')
def commands():
    return render_template('commands.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/FAQ')
def FAQ():
    return render_template('FAQ.html')

if __name__ == '__main__':
    app.run()
