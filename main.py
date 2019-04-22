import win32gui
import threading
import time


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def rildoBrincando():
	if __name__ == "__main__":
		results = []
		top_windows = []
		win32gui.EnumWindows(windowEnumerationHandler, top_windows)
		for i in top_windows:
			#print ('Teste do rildo::: ' , i)
			if "skype" in i[1].lower():
				print ('Teste do rildo::: ' , i)
				win32gui.ShowWindow(i[0],5)
				win32gui.SetForegroundWindow(i[0])
				#break
			
def printit():
		threading.Timer(5.0, printit).start()
		print "Hello, World!"		

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            print('Doing something imporant in the background')

            time.sleep(self.interval)
			
	

printit()

#example = ThreadingExample()
#time.sleep(3)
#print('Checkpoint')
#time.sleep(2)
#print('Bye')