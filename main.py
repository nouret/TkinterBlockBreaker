import tkinter
from math import *
from random import choice

size = 600
XCircle = 300
YCircle = 300
XRectangle = 300
r = 25
d = 30
DXCircle = 8
DYCircle = 10

colors = ["red", "green", "blue", "yellow"]

class Block():
	def __init__(self, X0, Y0, X1, Y1, COLOR):
		self.x0, self.y0, self.x1, self.y1, self.color = X0, Y0, X1, Y1, COLOR
		self.me = canvas.create_rectangle(X0, Y0, X1, Y1, fill=COLOR)

	def remove(self):
		canvas.delete(self.me)

	def intersection(self, x, y):
		x0, y0, x1, y1 = self.x0, self.y0, self.x1, self.y1
		if x0 < x < x1:
			dx = 0
		else:
			dx = min(abs(x0 - x), abs(x1 - x))
		if y0 < y < y1:
			dy = 0
		else:
			dy = min(abs(y0 - y), abs(y1 - y))
		return dx * dx + dy * dy < r * r

def key(event):
	print("pressed", event	)

def callback(event):
	print("clicked at", event.x, event.y)

def function(x, y):
	for i in range(x):
		print(y)

def UpHit(x = float("nan")):
	global DYCircle
	DYCircle = -abs(DYCircle)

def DownHit(x = float("nan")):
	global DYCircle
	DYCircle = abs(DYCircle)

def LeftHit(x = float("nan")):
	global DXCircle
	DXCircle = abs(DXCircle)

def RightHit(x = float("nan")):
	global DXCircle
	DXCircle = -abs(DXCircle)

def rectanglemove(event):
	global XRectangle
	XRectangle = event.x
	if XRectangle < 3 * r:
		XRectangle = 3 * r
	if XRectangle > size - 3 * r:
		XRectangle = size - 3 * r
	canvas.coords(rectangle, XRectangle - 3 * r, size, XRectangle + 3 * r, size - d)
	canvas.update()

def move():
	global XCircle, YCircle, XRectangle, DXCircle, DYCircle, blocks
	XCircle += DXCircle
	YCircle += DYCircle
	canvas.coords(circle, XCircle - r, YCircle - r, XCircle + r, YCircle + r)
	if YCircle <= r:
		DownHit()
	if size - r <= YCircle and not(XRectangle - 3 * r <= XCircle <= XRectangle + 3 * r and size - r - d <= YCircle):
		UpHit()
	if (XRectangle - 3 * r <= XCircle <= XRectangle + 3 * r and size - r - d <= YCircle):
		alpha = (XCircle - XRectangle + 3 * r) * pi / (6 * r)
		DXCircle, DYCircle = -cos(alpha) * sqrt(DXCircle ** 2 + DYCircle ** 2), -sin(alpha) * sqrt(DXCircle ** 2 + DYCircle ** 2)
	if XCircle <= r:
		LeftHit()
	if size - r <= XCircle:
		RightHit()
	delete = set()
	for block in blocks:
		if block.intersection(XCircle, YCircle):
			delete |= {block}
			block.remove()
			DownHit()
	for block in delete:
		blocks.remove(block)
	canvas.update()
	canvas.after(50, move)

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=size, height=size)
canvas.bind("<Motion>", rectanglemove)

canvas.pack()
circle = canvas.create_oval(XCircle-r, YCircle-r, XCircle+r, YCircle+r, fill='red')
rectangle = canvas.create_rectangle(XRectangle - 3 * r, size, XRectangle + 3 * r, size - d, fill = "green")
helpcircle = canvas.create_oval(10, 20, 20, 30, fill='green')

blocks = []
for x in range(0, size, 60):
	for y in (0, 30, 60):
		blocks += [(Block(x + 1, y + 1, x + 59, y + 29, choice(colors)))]

root.after(50, move)


def f(x):
	global DXCircle, DYCircle, XCircle, YCircle
	v = sqrt(DXCircle ** 2 + DYCircle ** 2)
	print(v)
	n = sqrt((XRectangle - XCircle) ** 2 + (size - d - YCircle) ** 2)
	print(XCircle, XRectangle, YCircle, d)
	DXCircle, DYCircle = (-XCircle + XRectangle) / n * v, (size - d - YCircle) / n * v

root.bind("<space>", f)

#print(help(canvas.bind))
root.mainloop()
