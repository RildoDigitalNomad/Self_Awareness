import pymongo
from pymongo import MongoClient
from flask import render_template
from app import app
import json
import datetime
from flask import jsonify, request, make_response, send_from_directory

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
	
@app.route('/selfawareness', methods=['GET', 'POST'])
def selfAwareness():
	if request.method == 'POST':
		print('clicou')
		if request.form.get('match-with-pairs'):
			print('tem coisa selecioda')
	client = MongoClient('localhost', 27017)
	db = client.self_awareness_database
	mainTrack_Collection = db.mainTrack3
	tudo = mainTrack_Collection.find()
	dropdown_list2 = []
	for track in mainTrack_Collection.find():
		if track['date'].strftime("%d.%m.%Y - %H:%M")[0:2] not in dropdown_list2:
			dropdown_list2.append(track['date'].strftime("%d.%m.%Y - %H:%M")[0:2])		 
	return render_template('selfAwareness.html', title='Home', mainTracks = tudo, dropdown_list = dropdown_list2, rildo = 'Nathan' )
	
@app.route('/drop')
def drop():
	client = MongoClient('localhost', 27017)
	db = client.self_awareness_database
	db.mainTrack3.drop()
	return "DROPOOU"
	
@app.route('/popular')
def popular():
	date1 = datetime.datetime(2019, 5, 12, 0, 0, 0, 0)
	print(date1)
	print(type(date1))
	date2 = datetime.datetime(2019, 5, 11, 0, 0, 0, 0)
	print(date2)
	client = MongoClient('localhost', 27017)
	db = client.self_awareness_database
	mainTrack_Collection2 = db.mainTrack3
	temp = [{ "autor": "Nathan",
			"date":date1, #.strftime("%d.%m.%Y - %H:%M"), #verificar se tirando esse strftime ele salva como data
			"mainQuestion":'populando apenas',
			"Related_US" : '123445'},
			{ "autor": "Nathan",
			"date":date2, #.strftime("%d.%m.%Y - %H:%M"), #verificar se tirando esse strftime ele salva como data
			"mainQuestion":'populando apenas',
			"Related_US" : '1234'}
			]
	#------------- PEGAR A ULTIMA COISA INSERIDA
	
	
	#------------------------
	temp_id = mainTrack_Collection2.insert_many(temp)
	print('Ids:: ' , temp_id.inserted_ids)
	return "Salvoou"