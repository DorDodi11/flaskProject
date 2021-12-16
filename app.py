from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)

@ app.route('/')
def home_func():  # put application's code here
        return render_template('cv.html')

@app.route('/assignment8')
def assignment8_func():  # put application's code here
    return render_template('assignment8.html',
                           profile={'name' : 'Dor','last_name' : 'Dodi'},
                           city=('mevasseret zion'),
                           hobbies=['footbal','music','flask'],
                           degrees=('Bsc','Msc'))


#@app.route('/')
#def hello_world():  # put application's code here
 #   return 'Hello World!'


@app.route('/about')
def about_func():  # put application's code here
    return 'this is about page'


@app.route('/contact')
def contact_func():  # put application's code here
    return redirect(url_for('catalog_func'))

@app.route('/catalog')
def catalog_func():  # put application's code here
    return 'this is catalog page'


if __name__ == '__main__':
    app.run(Debug=True)
