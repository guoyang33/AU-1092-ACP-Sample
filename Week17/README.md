# Week17 GUI

## Index

* [Introduction](#introduction)
* [Exercise: Login Form + Hash Guess](#login-form--hash-guess)
* [Exercise: Login Form + TicTacToe](#login-form--tictactoe)

## Introduction

Exercises of design GUI with python, especially tkinter module.

## Login Form + Hash Guess

### Intro

To create a login form, login with assign id/pw (csie/h3041723), after login, show the hash guess window, user input a hash code, check whiches plaintext and hash rule are using.

better using hash to encrypt the compair id and pw in program

just only compair with these 4 plaintext (1234, password, abcdef, qwerty) and 3 hash rule (sha1, sha256, md5)

### Screenshot

### File

* [login-hash_guess.py](src/login-hash_guess.py)

### Execute

~~~~bash
python login-hash_guess.py
~~~~

### Source Code

~~~~py
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

def hashGuess():
    pwDict = {
        '1234': {
            'sha1': '7110eda4d09e062aa5e4a390b0a572ac0d2c0220',
            'sha256': '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',
            'md5': '81dc9bdb52d04dc20036dbd8313ed055'
        },
        'password': {
            'sha1': '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8',
            'sha256': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
            'md5': '5f4dcc3b5aa765d61d8327deb882cf99'
        },
        'abcdef': {
            'sha1': '1f8ac10f23c5b5bc1167bda84b833e5c057a77d2',
            'sha256': 'bef57ec7f53a6d40beb640a780a639c83bc29ac8a9816f1fc6c5c6dcd93c4721',
            'md5': 'e80b5017098950fc58aad83c8c14978e'
        },
        'qwerty': {
            'sha1': 'b1b3773a05c0ed0176787a4f1574ff0075f7521e',
            'sha256': '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5',
            'md5': 'd8578edf8458ce06fbc5bb76a58c5ca4'
        }
    }
    guessData = guessEntry.get()
    for pw in pwDict:
        for type in pwDict[pw]:
            if guessData == pwDict[pw][type]:
                resultLabel['text'] = 'Password: {0}\nHash Type: {1}'.format(pw, type)
                return True
    resultLabel['text'] = 'Not Found'
        


# root
root = Tk()
root.geometry('400x400+200+100')
root.title('Demo')

# hash guess
Label(root, text='Hash Code:', font=('Arial', 18)).pack()
Label(root, text='').pack()

guessEntry = Entry(root, width=340)
guessEntry.pack()
Label(root, text='').pack()

Button(root, text='Submit', command=hashGuess).pack()
Label(root, text='').pack()

Label(root, text='Result:', font=('Arial', 14)).pack()
resultLabel = Label(root, text='', font=('Arial', 12))
resultLabel.pack()

Label(root, text='').pack()
Button(root, text='Exit', command=exit).pack()

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
~~~~

### Program Logic

1. --

## Login Form + TicTacToe

### Intro

To create a login form, login with assign id/pw (csie/h3041723), after login, show the TicTacToe game.

better using hash to encrypt the compair id and pw in program

### Screenshot

### File

* [login-tictactoe.py](src/login-tictactoe.py)

### Execute

~~~~bash
python login-tictactoe.py
~~~~

### Source Code

~~~~py
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
~~~~

### Program Logic

1. --

--

Authored by CYouLiao <guoyang33@gmail.com>