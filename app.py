from flask import Flask, render_template, request
app = Flask(__name__)

names=[]

def add_to_names(name):
	if len(names) < 3:
		names.append(name)
	else:
		if name == names[0] and names[0] == names[1] and names[0] == names[2]:
			return False 
		else:
			names.append(name)
	return True

#route to view all the people who have given a fuck
@app.route("/", methods=['GET', 'POST'])
def index():
	most_recent_names = names[0:10]
	return render_template('index.html', most_recent_names=most_recent_names)

#gives fuck
@app.route("/new_fucks", methods=['POST'])
def new_fuck():
	new_name = request.form["name"]
	if add_to_names(new_name):
		return str(len(names))+" fucks given"
	else:
		return "You have fucked too many times. Please let other fuckers fuck a bit before continuing your fucking"

#returns number of fucks given
@app.route("/number_fucks", methods=['GET'])
def number_fucks():
	return str(len(names))

app.debug = True
if __name__ == "__main__":
	app.run()
