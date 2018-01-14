from flask import Flask, render_template
import json
import urllib2

response = urllib2.urlopen('http://ckpool.org/pool/pool.work')
miners = json.loads(response.read())
print miners


app = Flask(__name__)

@app.route("/")
def index():
	CHR = "6.29P"
	return render_template("index.html", CHR=CHR)


@app.route("/pool_status")
def pool_status():
	return render_template("pool_status.html", miners= miners)

@app.route("/pool_work")
def pool_work():
	return render_template("pool_work.html")

@app.route("/blocks")
def blocks():
	return render_template("blocks.html")

if __name__ == "__main__":
	app.run(debug=True)
