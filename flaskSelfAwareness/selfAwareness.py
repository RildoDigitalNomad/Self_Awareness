from pywinauto.application import Application
import time
import pymongo
from pymongo import MongoClient
import wmi
import threading
import time
import datetime
from app import app




def control_time():
	print(datetime.datetime.now())
	appCmd = Application().connect(path=r"C:\windows\system32\cmd.exe")
	dialogRildo = appCmd.top_window()
	dialogRildo.maximize()
	if (dialogRildo.is_maximized()):
		dialogRildo.set_focus()
	
	pergunta1 = input('O que esteve fzendo durante este tempo?')
	print('Eu digitei::: ', pergunta1)
	print('Agora seria a hora de salvar!')
	# -------- MONGO DB
	client = MongoClient('localhost', 27017)
	db = client.self_awareness_database
	mainTrack_Collection = db.mainTrack
	temp = { "autor": "Nathan",
			"date":datetime.datetime.now(),
			"mainQuestion":pergunta1}
	temp_id = mainTrack_Collection.insert_one(temp).inserted_id
	print('sera que inseriu??      >>   ' , temp_id)
	#time.sleep(10)
	dialogRildo.minimize()
	
def self_awareness():
	threading.Timer(300, self_awareness).start()
	control_time()

self_awareness()