from tkinter import *
from PIL import Image, ImageTk
import qrcode
import time

def get_qr(url):
    qr = qrcode.make(url)
    qr.save("qrcode.png", "png")

    qr_window = Toplevel(root)
    qr_window.title("QR CODE")
    qr_window.resizable(False, False)
    time.sleep(1)

    qr_img = Image.open("qrcode.png")
    qr_img = ImageTk.PhotoImage(qr_img)
    panel = Label(qr_window, image=qr_img)
    panel.image = qr_img
    panel.pack()


bg = "#FBEAEB"
fg = "#1D1B1B"
btnbg = "#a6a6a6"
btnfg = "#1D1B1B"

root = Tk()
root.title("QR Code genrator | THE_ARYA")
root.geometry("500x300+200+200")
root.resizable(False, False)

title = Label(root, text="QR Code generator", font=('lucida', 22), bg=bg, fg=fg)
title.pack(side='top', fill=X, pady=(25, 0))

url = Entry(root, relief="solid", font=('lucida', 15))
url.insert(0, "Enter URL or Text")
url.bind("<FocusIn>", lambda event: url.delete(0, END))
url.pack(fill=X, pady=(25, 0), padx=15)

btn = Button(root, text="Generate QR code", bg=btnbg, fg=btnfg, activebackground=btnbg, relief='solid', cursor="hand2", command=lambda: get_qr(url.get()))
btn.pack(fill=X, pady=(25, 0), padx=20)
quit = Button(root, text="Close", bg=btnbg, fg=btnfg, activebackground=btnbg, relief='solid', cursor="hand2", command=root.quit)
quit.pack(fill=X, pady=(5, 0), padx=20)

root.mainloop()
