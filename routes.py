from flask import Flask, render_template
import json
import urllib2


pool_stats_cats = ['runtime','lastupdate','Users','Workers','Idle','Disconnected','hashrate1m','hashrate5m',
'hashrate15m','hashrate1hr','hashrate6hr','hashrate1d','hashrate7d','SPS1m','SPS5m','SPS15m','SPS1h',
'diff','accepted','rejected','lns','herp','reward']

#test git again


url = urllib2.urlopen('http://ckpool.org/pool/pool.status')
for obj in url.readlines():
	data = json.loads(obj.decode())
	if 'runtime' in data:
		runtime = data['runtime']
	if 'lastupdate' in data:
		lastupdate = data['lastupdate']
	if 'Users' in data:
		Users = data['Users']		
	if 'Workers' in data:
		Workers = data['Workers']
	if 'Idle' in data:
		Idle = data['Idle']
	if 'Disconnected' in data:
		Disconnected = data['Disconnected']
	if 'hashrate1m' in data:
		hashrate1m = data['hashrate1m']
	if 'hashrate5m' in data:
		hashrate5m = data['hashrate5m']
	if 'hashrate15m' in data:
		hashrate15m = data['hashrate15m']
	if 'hashrate1hr' in data:
		hashrate1hr = data['hashrate1hr']
	if 'hashrate6hr' in data:
		hashrate6hr = data['hashrate6hr']
	if 'hashrate1d' in data:
		hashrate1d = data['hashrate1d']
	if 'hashrate7d' in data:
		hashrate7d = data['hashrate7d']
	if 'SPS1m' in data:
		SPS1m = data['SPS1m']
	if 'SPS5m' in data:
		SPS5m = data['SPS5m']									
	if 'SPS15m' in data:
		SPS15m = data['SPS15m']
	if 'SPS1h' in data:
		SPS1h = data['SPS1h']
	if 'diff' in data:
		diff = data['diff']
	if 'accepted' in data:
		accepted = data['accepted']
	if 'rejected' in data:
		rejected = data['rejected']
	if 'lns' in data:
		lns = data['lns']
	if 'herp' in data:
		herp = data['herp']
	if 'reward' in data:
		reward = data['reward']

app = Flask(__name__)

@app.route("/")
def index():
	CHR = "6.29P"
	return render_template("index.html", hashrate1m=hashrate1m, Workers=Workers)


@app.route("/pool_status")
def pool_status():
	return render_template("pool_status.html", runtime=runtime, lastupdate=lastupdate,Users=Users,Workers=Workers,Idle=Idle,Disconnected=Disconnected,
		hashrate1m=hashrate1m,hashrate5m=hashrate5m,hashrate15m=hashrate15m,hashrate1hr=hashrate1hr,hashrate6hr=hashrate6hr,
		hashrate1d=hashrate1d,hashrate7d=hashrate7d,SPS1m=SPS1m,SPS5m=SPS5m,SPS15m=SPS15m,SPS1h=SPS1h,diff=diff,accepted=accepted,
		rejected=rejected,lns=lns,herp=herp,reward=reward)

@app.route("/pool_work")
def pool_work():
	return render_template("pool_work.html")

@app.route("/blocks")
def blocks():
	return render_template("blocks.html")

if __name__ == "__main__":
	app.run(debug=True)
