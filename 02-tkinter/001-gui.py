#simple GUI

try:
	# for pyhton 2
	from Tkinter import *
except ImportError:
	# for python 3
	from tkinter import *

#create window
root = Tk()

#modify root window
root.title("Latihan GUI - zar")
root.geometry("600x600")

#get frame from root
app = Frame(root);
#method grid untuk menampilkan element di GUI
app.grid()

label1 = Label(app,text="Tekan tombol")
label1.grid()

button1 = Button(app)
button1.configure(text="Button 1")
button1.grid()

button2 = Button(app)
button2.grid()
button2["text"]="Button 3 hehe"

#kick off the event loop
""" main loop """
root.mainloop()