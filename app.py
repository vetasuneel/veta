from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
# from pyngrok import ngrok
# port_no = 5000

  
  
app = Flask(__name__)
# ngrok.set_auth_token("2FfawXouJ0x3SjV6kv7B7bn4hjW_2unGskpEiAhXwk6JhS5gD")
# public_url = ngrok.connect(port_no)
  
  
app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'product'
  
mysql = MySQL(app)
# coin = 0

  



@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM product WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            # session['tokenn'] = user['tokenn']

            mesage = 'Logged in successfully !'
            return render_template('index_dashboard.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)
  
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))
  
@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM product WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO product VALUES (NULL, % s, % s, % s)', (userName, email, password))
            mysql.connection.commit()
            
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('sign-up.html', mesage = mesage)

@app.route('/c', methods=['POST', 'GET'])
def c():
    return render_template("index1.html")
@app.route('/pro' , methods=['POST', 'GET'])
def pro():
    output = request.form.to_dict()

    name = output["name"]
    # temp = output["temp"]
    # token = output["token"]



    
    # length_sent = len(name)
    # word_count = len(name.split())
    # space_count = name.count(' ')
    # namecount = word_count + space_count

    # model = "mamoon rasheed"
    
    # length_sent = len(model)
    # word_count = len(model.split())
    # space_count = model.count(' ')
    # modelcount = word_count + space_count + namecount
    # coin_minus = coin - modelcount


    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # sql = "UPDATE user SET tokenn = %s WHERE name = %s "
    # data = (coin_minus,userName)
    # cursor.execute(sql,data)
    # mysql.connection.commit()

    
    
    return render_template("index1.html",name = name)
    
if __name__ == "__main__":
    #  print(public_url)
# app.run(port=port_no)
   app.run(debug=True,port=8080)




