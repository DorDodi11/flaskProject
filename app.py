from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/about')
def about_func():  # put application's code here
    return redirect('/catalog')


@app.route('/contact')
def contact_func():  # put application's code here
    return redirect(url_for('catalog_func'))

@app.route('/catalog')
def catalog_func():  # put application's code here
    return 'this is catalog page'


if __name__ == '__main__':
    app.run()
