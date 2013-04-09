from flask import Flask, render_template, request
import os
import psycopg2
import time
app = Flask(__name__)

conn = psycopg2.connect("dbname=fuck user=postgres password=thrashers") #check_same_thread=False)
cursor = conn.cursor()

#cursor.execute("""CREATE TABLE fuckers (name text, created_at text)""")


def current_time():
	fuck_time = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
	return fuck_time

def count_fuckers():
	cursor.execute('SELECT * FROM fuckers')
	return len(cursor.fetchall())


def add_to_names(name):
	if count_fuckers() < 3:
		cursor.executemany('INSERT INTO fuckers VALUES (%s,%s)', [(name, current_time())])
		conn.commit()
	else:
		cursor.execute('SELECT * FROM fuckers ORDER BY name DESC LIMIT 3')
		rows = cursor.fetchall()

		if name == rows[0][0] and name == rows[1][0] and name == rows[2][0]:
			return False 
		else:
			cursor.execute('INSERT INTO fuckers VALUES (%s,%s)', [(name, fuck_time)])
	return True

#route to view all the people who have given a fuck
@app.route("/", methods=['GET', 'POST'])
def index():
	most_recent_names = cursor.execute('SELECT * FROM fuckers DESC LIMIT 10')
	return render_template('index.html', most_recent_names=most_recent_names)

#gives fuck
@app.route("/new_fucks", methods=['POST'])
def new_fuck():
	new_name = request.form["name"]
	if add_to_names(new_name):
		return str(count_fuckers())+" fucks given"
	else:
		return "You have fucked too many times. Please let other fuckers fuck before continuing"

#returns number of fucks given
@app.route("/number_fucks", methods=['GET'])
def number_fucks():
	return str(count_fuckers())

#app.debug = True
if __name__ == "__main__":
	port = int(os.environ.get("HEROKU_POSTGRESQL_COPPER_URL", 5000))
	app.run(host='0.0.0.0', port=port)
