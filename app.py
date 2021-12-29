from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session
app = Flask(__name__)
app.secret_key='123'

@ app.route('/')
def home_func():  # put application's code here
        return render_template('cv.html')

@app.route('/assignment8')
def assignment8_func():  # put application's code here
    return render_template('assignment8.html',
                           profile={'user1':{ 'name' : 'Dor ','last_name' : 'Dodi', 'email':'dordodi@gmail.com'}},
                           city=('mevasseret zion'),
                           hobbies=['footbal','music','flask'],
                           degrees=('Bsc','Msc'))

@app.route('/assignment9', methods=['GET','POST'])
def assignment9_func():
    if request.method == 'GET':
        if 'first name' in request.args:
            name1 = request.args['first name']
            name2 = request.args['last name']
            users = [{'name': 'dor', 'lastname': 'dodi', 'nickname': 'shamen'},
                     {'name': 'moti', 'lastname': 'dodi', 'nickname': 'aba'},
                     {'name': 'anat', 'lastname': 'dodi', 'nickname': 'ima'},
                     {'name': 'lior', 'lastname': 'dodi', 'nickname': 'joint'},
                     {'name': 'ariel', 'lastname': 'dodi', 'nickname': 'kabab'}]
            if name1 == "" and name2 == "":
                return render_template('assignment9.html',fullist=users )
            else:
                flag = False
                for user in users:
                    if user['name'] == name1 and user['lastname'] == name2:
                        flag = True
                        return render_template('assignment9.html', searchfound=user)
                if not flag:
                    return render_template('assignment9.html', itemnotfound="Item not found!")

        return render_template('assignment9.html')
    if request.method == 'POST':
        name3 = request.form['first name']
        name4 = request.form['last name']
        users = [{'name': 'dor', 'lastname': 'dodi', 'nickname': 'shamen'},
                 {'name': 'moti', 'lastname': 'dodi', 'nickname': 'aba'},
                 {'name': 'anat', 'lastname': 'dodi', 'nickname': 'ima'},
                 {'name': 'lior', 'lastname': 'dodi', 'nickname': 'joint'},
                 {'name': 'ariel', 'lastname': 'dodi', 'nickname': 'kabab'}]
        for user in users:
            if user['name'] == name3 and user['lastname'] == name4:
                nickname1 = user['nickname']
                session['nickname1']=nickname1
                return render_template('assignment9.html', nickname=nickname1)
            else:
                return render_template('assignment9.html', notregistered="you are not registered!")

    return render_template('assignment9.html')






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
