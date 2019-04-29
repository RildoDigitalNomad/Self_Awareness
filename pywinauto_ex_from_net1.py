from pywinauto.application import Application
import time
import pymongo
from pymongo import MongoClient
import wmi
import threading
import time
import datetime
from flask import Flask


def index():
    return "Hello, World!"

def init_Flask():
	print('Flask initing!!!')
	app = Flask(__name__)
	@app.route('/')
	@app.route('/index')


	
def control_time():
	print(datetime.datetime.now())
	appCmd = Application().connect(path=r"C:\windows\system32\cmd.exe")
	dialogRildo = appCmd.top_window()
	dialogRildo.maximize()
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
	temp_id = mainTrack.insert_one(temp).inserted_id
	print('sera que inseriu??      >>   ' , temp_id)

#c = wmi.WMI ()

#for process in c.Win32_Process ():
 # print (process.ProcessId, process.Name)
  
#app10 = Application()
#testeProcess = app10.findwindows()
#print(app10)


#app = Application(backend="uia").start('notepad.exe')

# describe the window inside Notepad.exe process
#dlg_spec = app.UntitledNotepad
# wait till the window is really open
#actionable_dlg = dlg_spec.wait('visible')
#print('Vendo uma coisinha')
#time.sleep(3)
#dlg_spec.minimize()
#print('opa, ta indo, espera ai')
#time.sleep(5)
#print(dialogRildo)
#print('indo minimizar cmd')
#time.sleep(2)
#dialogRildo.minimize()
#print('agora vou maximizar')
#time.sleep(2)
#print('maximizou???')
#time.sleep(3)
#dialogs = app2.Dialog
#dialogs.minimize()


# -------- MONGO DB
#client = MongoClient('localhost', 27017)
#db = client.test_database
#collection = db.test_collection
#rildo = { "autor": "Rildo"
#}
#post_id = collection.insert_one(rildo).inserted_id
#print('sera que inseriu??')
#print(post_id)

def self_awareness():
	threading.Timer(600, self_awareness).start()
	control_time()

self_awareness()
init_Flask()
	


	
	
	
	
	
	
	