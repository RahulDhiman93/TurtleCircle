import turtle

def square():
	window=turtle.Screen()
	window.bgcolor("red")
	rahul = turtle.Turtle()
	rahul.color("yellow")
	rahul.shape("turtle")
	rahul.speed(15)
	i=0
	while i!=40:
		rahul.forward(100)
		rahul.right(90)
		rahul.forward(100)
		rahul.right(90)
		rahul.forward(100)
		rahul.right(90)
		rahul.forward(100)
		rahul.right(90)
		circle(rahul)
		i+=1


	'''anku=turtle.Turtle()
	anku.color("blue")
	anku.shape("arrow")
	anku.circle(100)

	rk=turtle.Turtle()
	rk.color("green")
	anku.shape("arrow")
	anku.forward(100)
	anku.forward(100)
	anku.right(120)
	anku.forward(100)
	anku.right(120)
	anku.forward(100)
	anku.right(120)'''
	
def circle(tur_tle):
	tur_tle.right(10)


square()
    