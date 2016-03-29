import tkinter

size = 600
XCircle = 300
YCircle = 300
XRectangle = 300
r = 25
d = 30
DXCircle = 2
DYCircle = 3

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
	global XCircle, YCircle, XRectangle
	XCircle += DXCircle
	YCircle += DYCircle
	canvas.coords(circle, XCircle - r, YCircle - r, XCircle + r, YCircle + r)
	if YCircle <= r:
		DownHit()
	if size - r <= YCircle or (XRectangle - 3 * r <= XCircle <= XRectangle + 3 * r and size - r - d <= YCircle):
		UpHit()
	if XCircle <= r:
		LeftHit()
	if size - r <= XCircle:
		RightHit()
	canvas.update()
	canvas.after(50, move)

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=size, height=size)
canvas.bind("<Motion>", rectanglemove)
canvas.pack()
circle = canvas.create_oval(XCircle-r, YCircle-r, XCircle+r, YCircle+r, fill='red')
rectangle = canvas.create_rectangle(XRectangle - 3 * r, size, XRectangle + 3 * r, size - d, fill = "green")
helpcircle = canvas.create_oval(10, 20, 20, 30, fill='green')
root.after(50, move)
root.mainloop()