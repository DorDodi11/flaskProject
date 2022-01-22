import random
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request, jsonify
from flask import session
import requests
from flask import blueprints
from interact_with_DB import interact_db


app = Flask(__name__)
app.secret_key = '12345'


####pages
##homepage
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)



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


'''@app.route('/assignment11/users', methods=['GET'])
def returnusersjsonify():
    if request.method == 'GET':
        query = "select * from users"
        query_result = interact_db(query=query, query_type='fetch')
        data = list(map(lambda row: row._asdict(), query_result))
        data = jsonify(data)
    return data'''


def get_user(num):
    res = requests.get(f' https://reqres.in/api/users/{num}')
    # res = requests.get('https://pokeapi.co/api/v2/pokemon/%s' % random_n)
    res = res.json()
    return res


@app.route('/assignment11/outer_source', methods=['GET'])
def outersource():
    num=3
    if "number" in request.args:
        num = int(request.args['number'])
        print(num)
        user1 = get_user(num)
        return render_template('assignment11.html', user=user1)
    return render_template('assignment11.html')


@app.route('/assignment12/restapi_users',defaults = {'USER_ID':1})
@app.route('/assignment12/restapi_users/<int:USER_ID>')
def selectuser_func(USER_ID):
    if USER_ID == 1:
        query = "SELECT * FROM users WHERE id=1;"
        query_result = interact_db(query=query, query_type='fetch')
        response = query_result[0]
        response = jsonify(response)
        return response
    else:
        query = "SELECT * FROM users WHERE id='%s';" %USER_ID
        query_result = interact_db(query=query,query_type='fetch')
        response = {}
        if len(query_result) != 0:
            response = query_result[0]
        else :
            return "This user doesn't exist "
        response = jsonify(response)
    return response


if __name__ == '__main__':
    app.run(Debug=True, port=3307)
