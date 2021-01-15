# Imports
from tkinter import *
from PIL import Image, ImageTk
import qrcode
import time

# QR code generator
def get_qr(url):
    # Generate code
    qr = qrcode.make(url)
    # Get file name
    name = nameBox.get()
    # Save code
    qr.save(f"{name}.png", "png")

    # Create a top level
    qr_window = Toplevel(root)
    qr_window.title(f"{name}")
    qr_window.resizable(False, False)
    time.sleep(1)

    # Access and display QR code
    qr_img = Image.open(f"{name}.png")
    qr_img = ImageTk.PhotoImage(qr_img)
    panel = Label(qr_window, image=qr_img)
    panel.image = qr_img
    panel.pack()


# Color values
bg = "#FBEAEB"
fg = "#1D1B1B"
btnbg = "#a6a6a6"
btnfg = "#1D1B1B"

# Initiate GUI
root = Tk()
root.title("QR Code genrator | THE_ARYA")
root.geometry("500x300+200+200")
root.resizable(False, False)

# GUI Title
title = Label(root, text="QR Code generator", font=('lucida', 22), bg=bg, fg=fg)
title.pack(side='top', fill=X, pady=(25, 0))

# URL Box
url = Entry(root, relief="solid", font=('lucida', 15))
url.insert(0, "Enter URL or Text")
url.bind("<FocusIn>", lambda event: url.delete(0, END))
url.pack(fill=X, pady=(25, 0), padx=15)

# Name Box
nameBox = Entry(root, relief="solid", font=('lucida', 15))
nameBox.insert(0, "Enter Name to save code as")
nameBox.bind("<FocusIn>", lambda event: nameBox.delete(0, END))
nameBox.pack(fill=X, pady=(10, 0), padx=15)

# Generator button
btn = Button(root, text="Generate QR code", bg=btnbg, fg=btnfg, activebackground=btnbg, relief='solid', cursor="hand2", command=lambda: get_qr(url.get()))
btn.pack(fill=X, pady=(25, 0), padx=20)

# Close button
quit = Button(root, text="Close", bg=btnbg, fg=btnfg, activebackground=btnbg, relief='solid', cursor="hand2", command=root.quit)
quit.pack(fill=X, pady=(5, 0), padx=20)

# Mainloop
root.mainloop()
