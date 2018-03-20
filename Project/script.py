from flask import Flask, request, render_template, redirect, url_for
import pymysql.cursors

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

@app.route("/special")
def special():
	return render_template("special.html")

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
		ema = request.form["email"]
		cursor = db.cursor()
		cursor.execute("""INSERT INTO userinfo (un, pw, email, amount) VALUES (%s, %s, %s, 1000)""", (usn, pwd, ema))
		db.commit()
	return render_template("main.html", error = error)
	db.close()


@app.route("/premission", methods=['POST', 'GET'])
def premission():
	error = None
	if request.method == 'POST':
		usn = request.form["username"]
		pwd = request.form["password"]
		cursor = db.cursor()
		try:
			sql = ("SELECT * FROM userinfo WHERE un = '"+usn+"'")
			cursor.execute(sql)
			result = cursor.fetchall()
			for info in result:
				if usn == str(info[1]):
					if pwd == str(info[2]):
						return render_template("main.html", usn = usn)
					else:
						return render_template("login.html", msg = "worng pw")
				else:
					return render_template("login.html", msg = "error")
		except:
			return render_template("login.html", msg = "error")
	db.close()

@app.route("/download/purchase")
def purchase():
	return render_template("game.html")

@app.route("/download/game")
def game():
	return render_template("game.html")

@app.route("/comment", methods=['POST', 'GET'])
def comment():
	error = None
	if request.method == 'POST':
		us = request.form["name"]
		em = request.form["email"]
		cm = request.form["comment"]
		cursor = db.cursor()
		cursor.execute("""INSERT INTO comment (user, email, cm) VALUES (%s, %s, %s)""", (us, em, cm))
		db.commit()
	return render_template("contact.html", error = error, done = "We recived you opinion. Thank you!")
	db.close()

@app.route("/dashboard")
def dashboard():
	return render_template("dashboard.html")

@app.route("/logout", methods = ['POST', 'GET'])
def logout():
	return redirect(url_for("main"))








if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0", port=8000)