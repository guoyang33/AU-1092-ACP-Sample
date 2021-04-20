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