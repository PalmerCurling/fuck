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
	return str(len(names))


app.debug = True
if __name__ == "__main__":
	app.run()