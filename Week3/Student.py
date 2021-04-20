"""
這是物件導向程式的作業
"""

# Student 類別
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

print("-----------------Break Line-----------------\n")

#Book 類別
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
