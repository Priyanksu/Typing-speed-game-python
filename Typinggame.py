from tkinter import *
import random
from tkinter.messagebox import askretrycancel
import time

words = ['apple',"game",'ok',"hello","car",'kite','laptop','computer','python',"youtube",
"monitor","java","artificial","mouse","country","titanium","remote","keyboard","speaker","microphone",
"trackpad","smartphone","charger","orange","blue","red","black","purple","potato","tomato","carrot",
"grapes","colors","fruits","vegetables","bag","box","friday","monday","tuesday","wednesday",
"thursday","saturday","sunday","sun","moon","earth"]

score = 0
gTime = 60
Time = 60
incorrect = 0
correct = 0
accuracy = 0
total = 0

def ch_time():
    global Time,score,accuracy,correct,total,gTime
    if Time>0:
        Time = Time-1
        Time_label.configure(text=f"Time left: {Time}")
        Time_label.after(1000,ch_time)
    else:
        Calculate()
        Result.configure(text=f"Speed= {score} wpm Accuracy= {accuracy}% \n correct={correct} total={total}")
        Message = askretrycancel(title="Message",message="Click retry to try again")
        if Message:
            Time= gTime
            score = 0
            accuracy= 0
            correct = 0
            total =0
            incorrect = 0
            Result.configure(text="Type the word and press enter")
            Time_label.configure(text=f"Time left: {time}")
            WordEntry.delete(0,END)
            Start()
        else:
            root.destroy()

def Start():
    if Time==gTime:
        time.sleep(1)
        ch_time()
        Words_label.configure(text=word)

def NewWords(event):
    global correct,incorrect,total,gTime,word
    if Time==gTime:
        time.sleep(1)
        ch_time()
        Words_label.configure(text=word)
    if WordEntry.get()==Words_label['text']:
        correct += 1
        total += 1
    elif Words_label['text'] == "Press start to begin":
        corrcet = 0
        total = 0
        incorrect = 0
    else:
        incorrect += 1
        total += 1
    random.shuffle(words)
    word = random.choice(words)
    Words_label.configure(text=word)
    WordEntry.delete(0,END)

def Calculate():
    global score,accuracy,correct,total,gTime
    score = int(correct)/(gTime/60)
    accuracy = correct/total * 100
    # formula for accuracy = Total correct words/total words * 100
    accuracy = round(accuracy,2)

root = Tk()
root.geometry("700x500")
root.title("Typing game")
root.wm_resizable(False,False)
root.configure(bg="Light Green")

Game_name = Label(root,text="Welcome to typing game",bg="Light Green",fg="Black",font="Ubuntu 30 bold")
Game_name.pack(anchor='n',pady=(10,0),padx=(0,40))

Time_label = Label(root,text=f"time: {Time}",bg="Light green",fg="Black",font="Ubuntu 20 bold")
Time_label.pack(anchor='ne',pady=(30,0),padx=(0,40))

StartBtn = Button(root,text='Start',bg = "Dark green",fg="Black",font="Ubuntu 20 bold",command=Start)
StartBtn.pack(anchor="ne",side=RIGHT,pady=(70,0))

WordEntry = Entry(root,width=30,bg="White",fg="black",font="Monospace 20 bold")
WordEntry.focus()
WordEntry.pack(pady=(70,0),padx=(50,0))


word = random.choice(words)
Words_label = Label(root,text="Press start to begin",bg="Light Green",fg="Red",font="Monospace 25 bold")
Words_label.pack(pady=(25,0),padx=(50,0))

Result = Label(root,text="Press start or enter to start ",bg="Light Green",fg="Blue",font="Monospace 20 bold")
Result.pack(pady=(60,0),padx=(50,0),fill=X)

WordEntry.bind('<Return>',NewWords)
root.mainloop()