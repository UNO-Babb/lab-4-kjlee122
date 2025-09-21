import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS
def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
def fillCorner(alice, corner):
    drawSquare(alice, 100)
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
       alice.forward(50)
       alice.begin_fill()
       drawSquare(alice, 50)
       alice.end_fill()
    elif corner == 3:
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 4:
        alice.forward(100)
        alice.right(90)
        alice.forward(100)
        alice.right(90)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
def squaresInSquares(void, num):
    void.up()
    void.setposition(-200, 200)
    void.down()
    length = 400
    for n in range(num):
        drawSquare(void, length)
    
        length = (length-40)
        void.right(90)
        void.up()
        void.forward(20)
        void.left(90)
        void.forward(20)
        void.down()


def main():
    myTurtle = turtle.Turtle()
    drawSquare(myTurtle, 100)
    drawPolygon(myTurtle, 5) #draws a pentagon
   drawPolygon(myTurtle, 8) #draws an octogon
    fillCorner(myTurtle, 1)
    fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    
   fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    fillCorner(myTurtle, 4)
    

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
