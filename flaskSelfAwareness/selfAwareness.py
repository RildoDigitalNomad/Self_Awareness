from pywinauto.application import Application
import win32api
import time
import pymongo
from pymongo import MongoClient
import wmi
import threading
import time
import datetime
from app import app
import getch
import win32
from threading import Timer,Thread,Event
from pynput import keyboard




def on_press(key):
	try:
		print('alphanumeric key {0} pressed'.format(key.char))
	except AttributeError:
		print('special key {0} pressed'.format(key))

def on_release(key):
	print('{0} released'.format(key))
	if key == keyboard.Key.esc:
		# Stop listener
		return False



def checkMouseInactive():
	print ('Começando mouse inactive...')
	x, y = win32api.GetCursorPos()
	print ('Teste::: X: %d e Y: %d' , x, y)

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
	
	
	pergunta1 = input('O que esteve fzendo durante este tempo? \n')
	# ------------
	us = ''
	recurrentQuestion = ''
	for obj in mainTrack_Collection2.find().sort([("date", -1)]).limit(1):
		if obj["date"].strftime("%d.%m.%Y - %H:%M")[0:2] == todayDate.strftime("%d.%m.%Y - %H:%M")[0:2]:
			if  obj["Related_US"] != '' and obj["Related_US"] != 'N/A':
				while True:
					recurrentQuestion = input('Ainda está trabalhando na ultima tarefa? (%s) - S/N  \n' %obj["Related_US"])
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
	
	

class checkMouseClass():
	def __init__(self,t,hFunction):
		self.t=t
		self.hFunction = hFunction
		self.thread = Timer(self.t,self.handle_function)

	def handle_function(self):
		self.hFunction()
		self.thread = Timer(self.t,self.handle_function)
		self.thread.start()
		
	def start(self):
		self.thread.start()

	def cancel(self):
		self.thread.cancel()
	
	def is_Alive(self):
		return self.thread.is_alive()
	
class Application():
	def __init__(self):
		self.mousePositionX = 0
		self.mousePositionY = 0
		self.timer = checkMouseClass(20, self.tasks)
		self.timer.start()
		self.timer2 = checkMouseClass(5, self.mouse)
		self.timer2.start()
		#timer3 = checkMouseClass(5, self.printMouseP)
		#timer3.start()
		
	
	def tasks(self):
		print('tasks')
		with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
			listener.join()
		
	def mouse(self):
		self.laps = 0
		try:
			x, y = win32api.GetCursorPos()
			if ( x == self.mousePositionX and y == self.mousePositionY):
				print('mouse parado')
				self.timer.cancel()
			else: 
				print ('mudou')
				#print('Testando::: ' , self.timer.getName())
				if not (self.timer.is_Alive()): 
					self.timer = checkMouseClass(20, self.tasks)
					self.timer.start()
					print('Voltou a iniciar')
			self.mousePositionX = x
			self.mousePositionY = y
		except:
			print ('Computador bloqueado')
			
		
		
	#def printMouseP(self):
		#print ('Teste::: X: %d e Y: %d' %(self.mousePositionX, self.mousePositionY))
	
def main():
	#threading.Timer(20, main).start()
	#threading.Timer(5, checkMouseInactive).start()
	#control_time()
	#checkMouseInactive()
	timer = checkMouseClass(5, checkMouseInactive)
	timer.start()
	timer2 = checkMouseClass(20, control_time)
	timer2.start()
	
Application()