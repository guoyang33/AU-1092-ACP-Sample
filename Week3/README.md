# 3/12 第三週 | Week 3

## 目錄 | Index

---

## 課堂練習 | Exercise

### 說明-課堂練習 --- Week 3

類別練習

* 英雄人物
  * 請同學建立一個電玩角色 (Hero) 的類別
  * 自訂資料成員 (至少五項) 及函式成員
  * 在 Main 程式裡創建至少 3 個物件，並透過物件設定英雄名
  * Hero 類別裡要包含一個 showInfo() 函式，以顯示英雄人物的所有資訊

* 象棋的棋子
  * 請同學建立一個 Chess 的類別
  * 自訂資料成員 (至少五項) 及函式成員
  * 在 Main 程式裡創建至少 3 個物件，並透過物件設定象棋顏色或字
  * Chess  類別裡要包含一個 showInfo() 函式，以顯示象棋的所有資訊

### 程式碼-課堂練習 --- Week 3

#### Hero.py

~~~~python
# 英雄類別
class Hero:
    def attack(self, target):
        damage = self.PptAtk - target.PptDef
        damage = 0 if damage < 0 else damage
        target.HpCur = 0 if target.HpCur <= damage else target.HpCur-damage
        print("\"{}\" attacked \"{}\", dealt {} damages.".format(self.name, target.name, damage))
        print("\"{}\" left {} HP.".format(target.name, target.HpCur))
        print("---------Attack end.---------\n")

    def showInfo(self):
        print("Here's the properties of hero \"{}\"".format(self.name))
        print("HP :\t{} / {}\nAttack :\t{}\nDefense :\t{}".format(self.HpCur, self.HpMax, self.PptAtk, self.PptDef))
        print("---------Show Info end.----------\n")

    def __init__(self, name, PHp, PAtk, PDef):
        self.name = name
        self.HpMax = PHp
        self.HpCur = PHp
        self.PptAtk = PAtk
        self.PptDef = PDef

# creating heroes
Hero1 = Hero("Ming", 100, 3, 7)
Hero2 = Hero("Uzi", 85, 9, 4)
Hero3 = Hero("Xiaohu", 95, 8, 6)

# showInfo and run object method
Hero1.showInfo()
Hero2.attack(Hero1)
Hero1.showInfo()
~~~~

#### Chess.py

~~~~python
class Chess:
    # 顯示位置
    def showPosition(self):
        print("Showing position of Chess \"{}\", is at \"{}\"\n".format(self.name, self.position))
        for i in range(10, -2, -1):
            for j in range(-2, 11):
                if i==10 or i==-1:
                    if j>0 and j<9:
                        print(" {}  ".format(chr(96+j)), end="")
                    else:
                        print(" ", end="")
                elif i==9 or i==0:
                    if j==0:
                        print("+", end="")
                    elif j>0 and j<9:
                        print("---+", end="")
                    else:
                        print(" ", end="")

                elif i<9 and i>0:
                    if j==-2:
                        print("{} |".format(i), end="")
                    elif j==9:
                        print(" {}".format(i), end="")
                    elif int(self.position[1]) == i and ord(self.position[0])-96== j:
                        print(" @ |", end="")
                    elif j>0 and j<9:
                        print("   |", end="")
            if i<9 and i>1:
                print("\n  +---+---+---+---+---+---+---+---+ ")
            else:
                print()
        print("\nThe Chess \"{}\" is right here. ↑\n".format(self.name))
    
    def showInfo(self):
        print("Shows the properties of Chess \"{}\"".format(self.name))
        print("Name :\t{}\nClass :\t{}\nPosition :\t{}\n".format(self.name, self.chessClass, self.position))

    # constructor
    def __init__(self, name, chessClass, position):
        self.name = name
        self.chessClass = chessClass
        self.position = position

P1 = Chess("P1", "Pawn", "a2")
King = Chess("K", "King", "e1")
Queen = Chess("Q", "Queen", "d1")
Queen.showInfo()
King.showPosition()
~~~~

### 檔案-課堂練習 --- Week 3

* [Hero.py](Hero.py)
* [Chess.py](Chess.py)

---

## 作業

### 說明-作業 --- Week 3

類別練習

* Student 的類別
  * 自訂資料成員 (至少五項) 及函式成員
  * 在 Main 程式裡創建至少 3 個物件，並透過物件設定學生姓名或學號
  * Student 類別裡要包含一個 showInfo() 函式，以顯示學生的所有資訊

* Book 的類別
  * 自訂資料成員 (至少五項) 及函式成員
  * 在 Main 程式裡創建至少 3 個物件，並透過物件設定書名
  * Book 類別裡要包含一個 showInfo() 函式，以顯示書籍的所有資訊

### 程式碼-作業 --- Week 3

#### Student.py

~~~~python
class Student:
    # 上學
    def schooling(self, subject):
        sanLost = 60 if subject.lower()=="math" else 20
        if self.sanCur < sanLost:
            print("\"{}\" don't have enough of sanity.\nYour sanity : {} / {}\n".format(self.name, self.sanCur, self.sanMax))
        else:
            self.sanCur -= sanLost
            if subject.lower()=="math":
                self.scoreMath += 10
            elif subject.lower=="english":
                self.scoreEnglish += 10
            print("\"{}\" learned some {} stuff, he/she has lost {} sanities.".format(self.name, subject, sanLost))
            print("\"{}\" left {} sanities.\n".format(self.name, self.sanCur))

    def showInfo(self):
        print("Shows the properties of student \"{}\"".format(self.name))
        print("Name :\t{}\nSanity :\t{} / {}\nScore :\n\tMath :\t\t{}\n\tEnglish :\t{}\n".format(self.name, self.sanCur, self.sanMax, self.scoreMath, self.scoreEnglish))
    
    # constructor
    def __init__(self, name):
        self.name = name
        self.sanMax = 100
        self.sanCur = 100
        self.scoreMath = 0
        self.scoreEnglish = 0

# creating students
Student1 = Student("ZhanSan")
Student2 = Student("LiSi")
Student3 = Student("XiaoMing")

# showInfo and run object method
Student1.showInfo()
Student1.schooling("Math")
Student1.showInfo()
~~~~

#### Book.py

~~~~python
class Book:
    # 借出
    def borrow(self, renter):
        self.status = "Out"
        self.renter = renter
        print("\"{}\" has rent the book \"{}\" out.\n".format(renter, self.name))
    
    # 還書
    def back(self):
        self.status = "In"
        self.renter = ""
        print("Book \"{}\" is returned.\n".format(self.name))
    
    def showInfo(self):
        print("Shows the properties of book \"{}\"".format(self.name))
        print("Book Name :\t{}\nAuthor :\t{}\nPublication Year :\t{}\nStatus :\t{}\nRenter :\t{}\n".format(self.name, self.author, self.year, self.status, self.renter))

    # constructor
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.status = "In"
        self.renter = ""

# Creating books        
Book1 = Book("Le Petit Prince (R&H)", "Antoine de Saint-Exupéry", 1943)
Book2 = Book("Frankenstein", "Mary Wollstonecraft Shelley", 1818)
Book3 = Book("Adventures of Huckleberry Finn", "Mark Twain", 1884)

# showinfo and run class book method
Book1.showInfo()
Book1.borrow(Student1.name)
Book1.showInfo()
Book1.back()
Book1.showInfo()
~~~~

### 檔案-作業 --- Week 3

---
Author: 109021331 CYouLiao
