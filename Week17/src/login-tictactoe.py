from tkinter import *
import hashlib

def login():
    idData = idEntry.get()
    pwData = pwEntry.get()
    if len(idData) > 0 and len(pwData) > 0:
        s256 = hashlib.sha256()
        s256.update(idData.encode('utf-8'))
        idHash = s256.hexdigest()
        s256 = hashlib.sha256()
        s256.update(pwData.encode('utf-8'))
        pwHash = s256.hexdigest()
        if idHash == '207a0fd942624d8c7d26cb85594480f37840acfbf399f6cdc3724774ba9f1931' and pwHash == '5515f0912ec4ca5c9537a9c29ed62372869e0f2332c58eb312bd7ca7de850456':
            root.deiconify()
            loginScreen.destroy()
        else:
            idEntry.delete(0, 'end')
            pwEntry.delete(0, 'end')
    else:
        idEntry.delete(0, 'end')
        pwEntry.delete(0, 'end')

def exitProgram():
    loginScreen.destroy()
    root.destroy()

# root
root = Tk()
root.geometry('400x400+200+100')
root.title('Demo')

# TicTacToe
btns = [[0] * 3 for i in range(3)]
times = 0
flag = False

def setBtnsState(state):
    for i in range(3):
        for j in range(3):
            btns[i][j]['state'] = state

def checkLine(team, i, j):
    global btns
    lineList = [
        [btns[0][0]['text'], btns[1][1]['text'], btns[2][2]['text']],
        [btns[0][2]['text'], btns[1][1]['text'], btns[2][0]['text']],
        [btns[i][0]['text'], btns[i][1]['text'], btns[i][2]['text']],
        [btns[0][j]['text'], btns[1][j]['text'], btns[2][j]['text']]
    ]
    return True if [team]*3 in lineList else False

def btnPress(i, j):
    global flag
    global times
    team = btns[i][j]['text']
    if btns[i][j]['text'] not in ['X', 'O']:
        team = 'O' if flag else 'X'
        btns[i][j]['text'] = team
        flag = False if flag else 'O'
        times = times + 1
        if checkLine(team, i, j):
            setBtnsState(DISABLED)
            gameoverScreen = Toplevel(root)
            Label(gameoverScreen, text='Winner is {0}!!!'.format(team), font=('Times', 28)).pack()
            Button(gameoverScreen, text='OK', command=exit).pack()
            print('winner is team {0}!!!'.format(team))
        else:
            if times == 9:
                setBtnsState(DISABLED)
                gameoverScreen = Toplevel(root)
                Label(gameoverScreen, text='Draw!!!'.format(team), font=('Times', 28)).pack()
                Button(gameoverScreen, text='OK', command=exit).pack()

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

for i in range(3):
    for j in range(3):
        btns[i][j] = Button(root, text='　', font=('Arial', 24), command=lambda i1=i, j1=j: btnPress(i1, j1))
        btns[i][j].grid(row=i, column=j, sticky=NSEW)


# login screen
loginScreen = Toplevel(root)
loginScreen.title('Login')

Label(loginScreen, text='ID: ', anchor=E, justify=RIGHT, font=("Arial", 20)).grid(row=0, column=0, sticky=NSEW)
idEntry = Entry(loginScreen)
idEntry.grid(row=0, column=1, sticky=NSEW)

Label(loginScreen, text='Password: ', anchor=E, justify=RIGHT, font=("Arial", 20)).grid(row=1, column=0, sticky=NSEW)
pwEntry = Entry(loginScreen, show='*')
pwEntry.grid(row=1, column=1, sticky=NSEW)

Button(loginScreen, text='Login', command=login).grid(row=2, column=0, sticky=NSEW)
Button(loginScreen, text='Exit', command=exitProgram).grid(row=2, column=1, sticky=NSEW)


root.withdraw()
root.mainloop()