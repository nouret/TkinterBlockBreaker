import tkinter

size = 600
XCircle = 300
YCircle = 300
XRectangle = 300
r = 25
DXCircle = 2
DYCircle = 3

def key(event):
	print("pressed", event	)

def callback(event):
	print("clicked at", event.x, event.y)

def function(x, y):
	for i in range(x):
		print(y)

def VertHit(x = float("nan")):
	global DYCircle
	DYCircle *= -1

def HorHit(x = float("nan")):
	global DXCircle
	DXCircle *= -1

def rectanglemove(event):
	global XRectangle
	XRectangle = event.x
	if XRectangle < 3 * r:
		XRectangle = 3 * r
	if XRectangle > size - 3 * r:
		XRectangle = size - 3 * r
	canvas.coords(rectangle, XRectangle - 3 * r, size, XRectangle + 3 * r, size - 10)
	canvas.update()

def move():
	global XCircle, YCircle
	XCircle += DXCircle
	YCircle += DYCircle
	canvas.coords(circle, XCircle - r, YCircle - r, XCircle + r, YCircle + r)
	if XCircle <= r or size - r <= XCircle:
		HorHit()
	if YCircle <= r or size - r <= YCircle:
		VertHit()
	canvas.update()
	canvas.after(50, move)

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=size, height=size)
canvas.bind("<Motion>", rectanglemove)
canvas.pack()
circle = canvas.create_oval(XCircle-r, YCircle-r, XCircle+r, YCircle+r, fill='red')
rectangle = canvas.create_rectangle(XRectangle - 3 * r, size, XRectangle + 3 * r, size - 10, fill = "green")
helpcircle = canvas.create_oval(10, 20, 20, 30, fill='green')
root.after(50, move)
root.mainloop()