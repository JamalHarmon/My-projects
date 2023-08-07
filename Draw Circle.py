#Turtle Graphics Project 7.1

from turtle import Turtle

def drawCircle(t, x, y, rad):
    # draw the specified circle.
    # set the center point for the circle
    # Turn 3 degrees and moving a given distance 120 times
    #range is set to 120
    # Distance moved is 2.0 * PI * rad / 120.0

    t.up()
    t.goto(x,y)
    t.goto(x,y+rad)
    for count in range(120):
        t.down()
        t.pencolor("red")
        #t.down()
        #t.goto(x,y+rad)
        t.forward(rad)
        t.left(3)
        distance = ((2.0 * 3.14 *rad/120.0))

    return(distance)


def main():
    t = Turtle()
    drawCircle(t,0,0,5)

if __name__ == "__main__":
    main()
