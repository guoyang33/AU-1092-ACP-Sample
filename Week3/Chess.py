#1100312 Excerise 2

# Chess 類別
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
