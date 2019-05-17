from pywinauto.application import Application
import time
import pymongo
from pymongo import MongoClient
import wmi
import threading
import time
import datetime
from app import app
import getch



def control_time():
	#char = getch.getch()
	#print(char)
	#---------- Initialize current date
	todayDate = datetime.datetime.now()
	print('O dia de hoje é: ' , todayDate.strftime("%d.%m.%Y - %H:%M")[0:2])
	
	# -------- MONGO DB
	client = MongoClient('localhost', 27017)
	db = client.self_awareness_database
	mainTrack_Collection2 = db.mainTrack3
	#-----------------------------------------------------------------------------------
	print(datetime.datetime.now().strftime("%d.%m.%Y - %H:%M"))
	#-----------------------------------------------------------------------------------
	appCmd = Application().connect(path=r"C:\windows\system32\cmd.exe")
	dialogRildo = appCmd.top_window()
	dialogRildo.set_focus()
	#-----------------------------------------------------------------------------------
	
	
	pergunta1 = input('O que esteve fzendo durante este tempo? ')
	# ------------
	us = ''
	recurrentQuestion = ''
	for obj in mainTrack_Collection2.find().sort([("date", -1)]).limit(1):
		if obj["date"].strftime("%d.%m.%Y - %H:%M")[0:2] == todayDate.strftime("%d.%m.%Y - %H:%M")[0:2]:
			if  obj["Related_US"] != '' and obj["Related_US"] != 'N/A':
				while True:
					recurrentQuestion = input('Ainda está trabalhando na ultima tarefa? (%s) - S/N  ' %obj["Related_US"])
					try:
						if recurrentQuestion != "s" and recurrentQuestion != "n":
							raise ValueError("A resposta deve ser S (sim) ou N (nao)")
						else:
							break
					except ValueError as ve:
						print (ve)
				if recurrentQuestion == 's':
					us = obj["Related_US"]
	if us == '':
		us = input('US?? ')
					
	#-------------------

	temp = { "autor": "Nathan",
			"date":datetime.datetime.now(), #.strftime("%d.%m.%Y - %H:%M"), #verificar se tirando esse strftime ele salva como data
			"mainQuestion":pergunta1,
			"Related_US" : us}
	#------------- PEGAR A ULTIMA COISA INSERIDA
	
	
	#------------------------
	temp_id = mainTrack_Collection2.insert_one(temp).inserted_id
	print('Record Salvo!! Id      >>   ' , temp_id)
	dialogRildo.minimize()
	
def self_awareness():
	threading.Timer(50, self_awareness).start()
	control_time()

self_awareness()