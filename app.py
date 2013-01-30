from flask import Flask, request, render_template
app = Flask(__name__)

names=[]

#route to view all the people who have given a fuck
@app.route("/")
def index():
	return str(names)

#gives fuck
@app.route("/new_fucks", methods=['POST'])
def new_fuck():
	new_name = request.form["name"]
	names.append(new_name)

#returns number of fucks given
@app.route("/number_fucks", methods=['GET'])
def number_fucks():
	return str(len(names))

#View for recent fucks given (under construction)
@app.route("/fucks_given", methods=['GET'])
def fucks_given():
	return render_template("fucks_given")

app.debug = True
if __name__ == "__main__":
	app.run()
