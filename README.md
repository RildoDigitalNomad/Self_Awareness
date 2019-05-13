# Self_Awareness



PYTHON


import win32gui
 
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
		#print ('Teste do rildo::: ' , i)
        if "word" in i[1].lower():
            print ('Teste do rildo::: ' , i)
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            break


Trabalhar com Pandas Series para gerenciar o time stamp
https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.Series.html


Solucionando problema na instalação do win32gui

https://stackoverflow.com/questions/20113456/installing-win32gui-python-module

Documentação Win32GUI
http://docs.activestate.com/activepython/3.1/pywin32/win32gui.html

Primeiro exemplo funcional
https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/


https://pywinauto.readthedocs.io/en/latest/getting_started.html

docker exec -it e5c4c9d3880b /bin/bash

docker ps

https://insomniacgeek.com/2018/03/25/run-mongodb-in-a-docker-container-on-docker-for-windows/

set FLASK_APP=hello
flask run


GIT -> https://rogerdudler.github.io/git-guide/index.pt_BR.html