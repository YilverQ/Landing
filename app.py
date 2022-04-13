from flask import Flask, render_template

app = Flask("__main__")
#app.secret_key = "FlaskAplication"

@app.route("/")
def index():
	return render_template("index.html")

	
if __name__ == "__main__":
	app.run()