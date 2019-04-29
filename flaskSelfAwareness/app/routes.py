import pymongo
from pymongo import MongoClient
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
	
@app.route('/selfawareness')
def selfAwareness():
	#return "Rildo testando, brincando"
	client = MongoClient('localhost', 27017)
	db = client.self_awareness_database
	mainTrack_Collection = db.mainTrack
	tudo = mainTrack_Collection.find()
	print(tudo)
	return render_template('selfAwareness.html', title='Home', mainTracks = tudo)