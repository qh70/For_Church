from flask import *

app=Flask(__name__)

# Pages
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/beginning_universe")
def beginning_universe():
	return render_template("beginning_universe.html")

@app.route("/biological_genetics")
def biological_genetics():
	return render_template("biological_genetics.html")

@app.route("/people_monkey")
def people_monkey():
	return render_template("people_monkey.html")

@app.route("/fossil")
def fossil():
	return render_template("fossil.html")

@app.route("/evolution_theory")
def evolution_theory():
	return render_template("evolution_theory.html")

@app.route("/ape")
def ape():
	return render_template("ape.html")

app.run(host="0.0.0.0",port=4000)