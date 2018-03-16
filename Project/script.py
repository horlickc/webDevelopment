from flask import Flask, request, render_template, redirect, url_for
import pymysql.cursors
import time

app = Flask(__name__)

#open database connection
db = pymysql.connect(host='localhost', user='root', password='123456789', db='site')


@app.route("/main")
def main():
	return render_template("main.html")

@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/features")
def features():
	return render_template("features.html")

@app.route("/download")
def download():
	return render_template("dl.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")


@app.route("/register", methods = ['POST', 'GET'])
def register():
	error = None
	if request.method == 'POST':
		usn = request.form["username"]
		pwd = request.form["password"]
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		#maxid = cursor.fetchone()
		# Execute the SQL command
		cursor.execute("""INSERT INTO userinfo (un, pw) VALUES (%s, %s)""", (usn, pwd))
		# Commit your changes in the database
		db.commit()
	return render_template("main.html", error = error)
	db.close()


@app.route("/premission", methods=['POST', 'GET'])
def premission():
	error = None
	if request.method == 'POST':
		usn = request.form["username"]
		pwd = request.form["password"]
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		#maxid = cursor.fetchone()
		# Execute the SQL command
		sql = ("SELECT un, pw FROM userinfo WHERE un = '"+usn+"'")
		cursor.execute(sql)
		# Commit your changes in the database
		db.commit()
		results = cursor.fetchall()
		for row in results:
			custName = row[0]
			custPassword = row[1]
			print ("usn = %s, pwd = %s" % (custName, custPassword))
			return redirect(url_for('redirectmain', username = custName))
			time.sleep(5)
			##custPwd = password
	return render_template("redirect_main.html", error = error)
	db.close()


@app.route("/redirectmain")
def redirectmain():
	return render_template("redirect_main.html")


@app.route("/logout", methods = ['POST', 'GET'])
def logout():
	return redirect(url_for("main"))








if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0", port=8000)