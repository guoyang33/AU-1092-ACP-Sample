"""
這是物件導向程式的練習
"""

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
