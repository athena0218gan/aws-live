from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

#code for connection
app.config['MYSQL_HOST'] = 'localhost'#hostname
app.config['MYSQL_USER'] = '3306'#username
app.config['MYSQL_PASSWORD'] = 'Bait3273'#password
#in my case password is null so i am keeping empty
app.config['MYSQL_DB'] = 'assignment'#database name

mysql = MySQL(app)
@app.route('/')

@app.route('/projectreg',methods=['GET','POST'])
def projectreg():
    msg=''
    #applying empty validation
    if request.method == 'POST' and 'name' in request.form and 'tech' in request.form and 'desc' in request.form and 'gname' in request.form:
        #passing HTML form data into python variable
        n = request.form['name']
        t = request.form['tech']
        d = request.form['desc']
        g = request.form['gname']
        #creating variable for connection
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #query to check given data is present in database or no
        cursor.execute('SELECT * FROM pro_reg WHERE PRO_NAME = % s', (n,))
        #fetching data from MySQL
        result = cursor.fetchone()
        if result:
            msg = 'Project already exists !'
        else:
            #executing query to insert new data into MySQL
            cursor.execute('INSERT INTO PRO_REG VALUES (NULL, % s, % s, % s,% s,% s)', (n, t, d, g,'Pending',))
            mysql.connection.commit()
            #displaying message
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('projectreg.html', msg=msg)
if __name__ == '__main__':
    app.run(port=5000,debug=True)