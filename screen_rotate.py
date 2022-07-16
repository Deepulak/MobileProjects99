from tkinter import *
import rotatescreen

# Creating tkinter object
master = Tk()
master.geometry("140x100")
master.title("Screen Rotation")
master.configure(bg='light grey')

# variable classes in tkinter
result = StringVar()

# Creating buttond to change orientation
Button(master, text="Up", width=5, commnad=lambda:Screen_rotation(
	"up"),bg="white").grid(row=0, column=3)
Button(master, text="Right", width=5, commnad=lambda:Screen_rotation(
	"right"),bg="white").grid(row=1, column=6)
Button(master, text="Left", width=5, commnad=lambda:Screen_rotation(
	"left"),bg="white").grid(row=1, column=2)
Button(master, text="Down", width=5, commnad=lambda:Screen_rotation(
	"down"),bg="white").grid(row=3, column=3)

# Double click on GUI to Undo screen rotation
master.bind("<Double 1>", master_call)
master.mainloop()

# function for rotate screen
def Screen_rotation(temp):
	screen = rotatescreen.get_primary_display()
	if temp == "up":
		screen.set_landscape()
	elif temp == "right":
		screen.set_portrait_flipped()
	elif temp == "down":
		screen.set_landscape_flipped()
	elif temp == "left":
		screen.set_portrait()

def master_call(event):
	screen = rotatescreen.get_primary_display()
	screen.set_landscape()