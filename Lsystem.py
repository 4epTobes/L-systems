import turtle as t
from random import randint

height = 2000
width = 1000
screen = t.Screen()
screen.screensize(width, height)

t.hideturtle()
t.tracer(0)
t.penup()
t.setposition(0,-400)
t.pendown()
t.title("L-system")

angle = 25

axiom = "X"
axmTemp = ""
itr = 6
step = 5
stack = []

translate = {"+":"+",
			 "-":"-",
			 "[":"[",
			 "]":"]",
			 "X":"F-[[X]+X]+F[+FX]-X",
			 "F":"FF"}

for k in range(itr):
	for ch in axiom:
		axmTemp += translate[ch]
	axiom = axmTemp
	axmTemp = ""

t.left(90)
t.pensize(2)
percenage = 0
for ch in axiom:
	t.title("L-system " + str(round(percenage/len(axiom)*100)) + "%")
	if ch == "-":
		t.left(angle)
	elif ch == "+":
		t.right(angle)
	elif ch == "F" or ch == "X":
		t.forward(step)
	elif ch == "[":
		angle_, pos_ = t.heading(), t.pos()
		stack.append((angle_, pos_))
	elif ch == "]":
		angle_, pos_ = stack.pop()
		t.setheading(angle_)
		t.penup()
		t.goto(pos_)
		t.pendown()
	else:
		pass
	percenage += 1

with open("axiom.txt", "a") as f:
	f.write(axiom)

t.update()
t.mainloop()