import turtle
from time import sleep

import numpy as np

screen = turtle.Screen()
screen.title("Turtle graph")

plt = turtle.Turtle()
writer = turtle.Turtle()
frame = turtle.Turtle()
screen.setup(1160, 600, )

plt.penup()
frame.penup()
writer.penup()

plt.setposition(-400, -250)
frame.setposition(-400, -250)
writer.setposition(-430, -250)

plt.pendown()
frame.pendown()
frame.pensize(3)
frame.pencolor("red")
frame.speed(10)


def label_y(y_min, y_max):
	number_of_label = 20
	y_g = 500 / number_of_label
	interval = y_min
	interval_coefficient = (y_min - y_max) / (number_of_label - 1)
	shift_in_x = 1 + (len(str(interval_coefficient)) * 6)
	print(interval_coefficient)
	writer.setposition(-400 - shift_in_x, -250)
	
	for wr in range(number_of_label):
		writer.write(float(interval))
		interval = interval - interval_coefficient
		writer.setposition(-400 - shift_in_x, writer.ycor() + y_g)


def label_x(x_min, x_max, x_val):
	number_of_label = 20
	y_g = 800 / number_of_label
	interval = x_val[0]
	interval_coefficient = (x_min - x_max) / (number_of_label)
	shift_in_x = 1 + (len(str(round(interval_coefficient))) * 7)
	writer.setposition(-400 + shift_in_x, -250)
	index = 0
	# writer.clear()
	for wr in range(number_of_label):
		if index <= len(x_val):
			writer.write(round(x_val[index]))
			index = index+round(y_g)
			writer.setposition(writer.xcor() + shift_in_x + y_g, -250)
		else:
			writer.write(round(x_val[-1]))
			index = index + round(y_g)
			writer.setposition(writer.xcor() + shift_in_x + y_g, -250)
			break


def makeframe():
	frame.setposition(400, -250)
	frame.setposition(400, 250)
	frame.setposition(-400, 250)
	frame.setposition(-400, -250)


makeframe()


def ploltGraph(x, y):
	plt.setposition(x, y)


a = np.arange(0, 50, 0.1)
sample = len(a)
x = []
zoom_x = 800 / sample
temp_x = -400
while True:
	x.append(temp_x)
	temp_x = temp_x + zoom_x
	if temp_x >= 400:
		break

y_ax = np.sin(a)
y_min = y_ax.min()
y_max = y_ax.max()
margin = 0
zoom_y = ((500 - margin) / (y_max - y_min))

label_y(y_min, y_max)
label_x(a[0], a[-1], a)

y_gap = (-250 - y_min) / zoom_y
y_min = -250
y_max = y_max + y_gap


# y = [(randint(y_min, round(y_max))) for i in range(len(x))]
y = [i*zoom_y for i in y_ax]

plt.pensize(2)
plt.hideturtle()
theta = 180
while True:
	screen.tracer(len(x) + 1)
	plt.pendown()
	plt.clear()
	for i in range(len(x)):
		ploltGraph(x[i], y[i])
	
	y[:-1] = y[1:]
	y[-1] = np.cos(theta)* zoom_y
	# x[:-1] = x[1:]
	# x[-1] =  1
	# label_x(x[0], x[-1], y_ax)
	plt.penup()
	plt.setx(-400)
	theta += 0.1
	sleep(0.01)
# plt.clear()

