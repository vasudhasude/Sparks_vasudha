from flask import Flask,render_template,url_for,redirect,session,make_response
import mysql.connector as mysql
from flask import request
import os


app=Flask(__name__)
app.secret_key = os.urandom(24)


conn=mysql.connect(host='localhost',database='sparks',user='root',password='Vasudhir@2')
cursor=conn.cursor()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/customers')
def customers():
    cursor.execute("select account_no,name,email,contact from customers;")
    data = cursor.fetchall()
    return render_template('customers.html',data=data) 


@app.route('/transfer_history')
def transfer_history():
    cursor.execute("select name,account_no,amount,date from history;")
    data1 = cursor.fetchall()
    return render_template('transfer_history.html',data=data1)     
 
@app.route('/transfer_money')
def transfer_money():
    return render_template("transfer_money.html")   


@app.route('/history',methods=['POST'])
def history():
    name=request.form.get('name')
    account_no=request.form.get('account_no')
    amount=request.form.get('amount')
    date=request.form.get('date')
    
    cursor.execute("""INSERT INTO `history`(`name`,`account_no`,`amount`,`date`) VALUES
                   ('{}', '{}', '{}', '{}') """.format(name,account_no,amount,date))

    conn.commit() 

    
    return render_template("transfer_success.html") 

if __name__=="__main__":
  app.run(debug=True)   