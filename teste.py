from tkinter import *
from tkinter import Canvas
from datetime import date


import pyautogui
import keyboard
import pathlib
import json
import os

# 14 - 78: Processamento de arquivos do programa

file_dir = pathlib.Path(__file__).parent.resolve()


parent_dir = os.path.expanduser('~/Documents')
pasta = 'My Screenshots'
path = os.path.join(parent_dir, pasta)
isFile = os.path.isdir(path)

thumb = path + '/' + 'thumbnails'
isFileThumb = os.path.isdir(thumb)

fullimg = path + '/' + 'fullimages'
isFileFull = os.path.isdir(fullimg)


if isFile == False:
    os.mkdir(path)
    print(f'Diretório {path} criado')
else:
    print(f'O diretório {path} já existe')

lista = os.listdir(path)
number_files = len(lista)
capture_number = 0

if isFileThumb == True:
    print("A pasta thumbnails existe")
else:
    print("A pasta thumbnails não existe")
    os.mkdir(thumb)

if isFileFull == True:
    print("A pasta fullimages já existe")
else:
    os.mkdir(fullimg)

try:
    with open('options.json') as option:
        my_options = json.load(option)

except:
    print("[ERRO]: options.json não encontrado")
    
    optionDefault = {
        "saveFull": False
    }

    os.path.join(file_dir, "options.json")

    with open("options.json", "w") as option:
        json.dump(optionDefault, option)

finally:
    with open("options.json") as option:
        my_options = json.load(option)

print(f"Screenshots inteiras? ", my_options['saveFull'])

#82 - 189: Funções do programa

def close(self):
    win.destroy()
        
def coords(event):
    global x1
    global y1
    global my_rectangle
    my_rectangle = None
    x1, y1 = event.x, event.y
    my_rectangle = canvas.create_rectangle(x1, y1, x1, y1, fill="black", tags=f"{my_rectangle}")
    rectInfo()
      
def finalcoords(event):
    global x2
    global y2
    x2, y2 = event.x, event.y 
    resize()



def showFinalCoords(self):
    abs(x1 - x2)
    abs(y1 - y2)
    


def rectInfo():
    if my_rectangle > 1:
        canvas.delete(f"{my_rectangle - 1}")    

def resize():
    canvas.coords(my_rectangle, x1, y1, x2, y2)

def capture(event):    
    YEAR = date.today().year 
    MONTH = date.today().month 
    DAY = date.today().day
    
    width = abs(x1 - x2)
    height = abs(y1 - y2)
   
    if event.char == 'c':
        screenshotlist = os.listdir(path)
        thumblist = os.listdir(thumb)

        number_files_screenshots = len(screenshotlist)
        number_files_screenshots += 1

        number_files_thumbnails = len(thumblist)
        number_files_thumbnails += 1

        if x2 - x1 < 0:
            canvas.delete(my_rectangle)
            print("Screenshot adicionada!")
            win.destroy()
            if y1 - y2 < 0:
                pyautogui.screenshot(path + "/" + f"IMG_{YEAR}-{MONTH}-{DAY}_{number_files_screenshots - 2}.png", region=(x2, y1, width, height))
            elif y1 - y2 > 0:
                pyautogui.screenshot(path + "/" + f"IMG_{YEAR}-{MONTH}-{DAY}_{number_files_screenshots - 2}.png", region=(x2, y2, width, height))
            pyautogui.screenshot(thumb + "/" + f"thumb_{YEAR}-{MONTH}-{DAY}_{number_files_thumbnails - 1}.png")
            print(f"Altura: {abs(y1 - y2)}")
            print(f"Largura: {abs(x1 - x2)}")

        elif x1 - x2 < 0:
            print("Screenshot adicionada!")
            canvas.delete(my_rectangle)
            win.destroy()
            if y1 - y2 < 0:
                pyautogui.screenshot(path + "/" + f"IMG_{YEAR}-{MONTH}-{DAY}_{number_files_screenshots - 2}.png", region=(x1, y1, width, height))
            elif y1 - y2 > 0:
                pyautogui.screenshot(path + "/" + f"IMG_{YEAR}-{MONTH}-{DAY}_{number_files_screenshots - 2}.png", region=(x1, y2, width, height))   
            pyautogui.screenshot(thumb + "/" + f"thumb_{YEAR}-{MONTH}-{DAY}_{number_files_thumbnails - 1}.png")
            print(f"Altura: {abs(y1 - y2)}")
            print(f"Largura: {abs(x1 - x2)}")


    
def captureFull():
    YEAR = date.today().year 
    MONTH = date.today().month 
    DAY = date.today().day

    fullimagelist = os.listdir(fullimg)
    number_files_fullimages = len(fullimagelist)

    number_files_fullimages += 1

    pyautogui.screenshot(fullimg + '/' f"fullimage_{YEAR}-{MONTH}-{DAY}_{number_files_fullimages - 1}.png")
    print("Screenshot capturada!")

while True:
    if keyboard.read_key() == 'print screen' and my_options['saveFull'] == False:
    
        win = Tk()

        win.geometry("650x250")

        win.attributes('-fullscreen', True)
        win.attributes("-alpha", 0.1)
        win.config(cursor="cross")

        win.bind("<Escape>", close)

        win.bind("<Button-1>", coords)

        win.bind("<B1-Motion>", finalcoords)

        win.bind("<ButtonRelease-1>", showFinalCoords)

        win.bind("<Key>", capture)

        canvas = Canvas(win, bg='white')
        canvas.pack(fill=BOTH, expand=True)

        win.focus_force()
        win.mainloop()

    elif keyboard.read_key() == 'print screen' and my_options['saveFull'] == True:
    
        captureFull()

    elif keyboard.is_pressed('ctrl + /'):
        with open("options.json", "w") as option:
            my_options['saveFull'] = not my_options['saveFull']
            json.dump(my_options, option)
            print(f"Configuração saveFull alterada para: ", my_options['saveFull'])