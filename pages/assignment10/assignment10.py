from flask import Flask, url_for, redirect, render_template, request, session, Blueprint
import mysql.connector

assignment10 = Blueprint('assignment10',
                         __name__,
                         static_folder='static',
                         static_url_path='/pages/assignment10',
                         template_folder='templates')

@assignment10.route('/assignment10')
def index():
    return redirect('/users')

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/users')
def users():
    #query = "select * from users"
    #query_result = interact_db(query=query, query_type='fetch')
    #return render_template('Assignment10.html', users=query_result)
    return render_template('Assignment10.html')
'''
@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        nickname = request.form['nickname']
        query = "insert into users(name,lastname,nickname) values ('%s','%s','%s')" % (name, lastname, nickname)
        interact_db(query=query, query_type='commit')
        return redirect('/users')
    return redirect('/users')


@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        name1 = request.form['name']
        query = "delete from users where name ='%s';" % name1
        interact_db(query, query_type='commit')
        return redirect('/users')
    return redirect('/users')'''


