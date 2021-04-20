# 3/12 第三週 | Week 3

## 目錄 | Index

---

## 課堂練習 | Exercise

### 說明-課堂練習 --- Week 3

物件導向

請同學將課堂練習的過程記錄在Github的 Repository 中的 Readme 檔案。

完成後請將 Github Repository 連結上傳至系統

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

---

## 作業

### 說明-作業 --- Week 3

### 程式碼-作業 --- Week 3

### 檔案-作業 --- Week 3

---
Author: 109021331 CYouLiao
