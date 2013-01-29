from flask import Flask, request
app = Flask(__name__)

names=[]

@app.route("/")
def index():
	return str(names)

@app.route("/new_fuck", methods=['POST'])
def new_fuck():
	new_name = request.form["name"]
	names.append(new_name)
	return "Great Success\n"

@app.route("/number_fucks", methods=['GET'])
def number_fucks():
	return str(len(names))

app.debug = True
if __name__ == "__main__":
	app.run()
