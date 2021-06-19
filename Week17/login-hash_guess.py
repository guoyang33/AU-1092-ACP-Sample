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