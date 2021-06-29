import os
from posixpath import realpath
import sys
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

images = []

window = Tk()
start = '/Users/brock/Desktop/icons'
# size = (350, 400)
size = (800, 800)

window.title("Watermark")
window.config(padx=20, pady=10, bg="grey",
              cursor="hand2")

labels = []

mod_image = ""


def show_labels():
    for x in range(0, len(labels)):
        labels[x].grid(column=1, row=x+1)


def add_text_to_image():
    watermark = text_input.get()
    draw = ImageDraw.Draw(mod_image)
    font = ImageFont.load_default()
    draw.text((0, 0), watermark, (255, 255, 255), font=font)
    mod_image.show()
    mod_image.thumbnail(size, Image.ANTIALIAS)
    test = ImageTk.PhotoImage(mod_image)
    label1 = Label(image=test)
    label1.image = test
    canvas.destroy()
    label1.grid(column=1, row=1, columnspan=2)
    labels.append(label1)


def create_text_label():
    text_input_label.grid(column=1, row=2, padx=10, pady=5)
    text_input.insert(0, '')
    text_input.grid(column=2, row=2, columnspan=2, padx=10, pady=5)
    text_button.grid(column=2, row=3, padx=10, pady=5)


def add_image():
    global mod_image
    for widget in labels:
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir=start, title="Select Images",
                                          filetypes=(("images", ".png"), ("images", ".jpg"), ("images", ".jpeg")))
    relpath = os.path.relpath(filename)
    image1 = Image.open(relpath)
    mod_image = image1
    images.append(
        {"PIL_image": image1, "file_name": relpath.split("/")[-1].split(".")[0]})
    image1.thumbnail(size, Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    canvas.destroy()
    label1.grid(column=1, row=1, columnspan=2)
    labels.append(label1)
    create_text_label()


text_input_label = Label(text='Text: ')

text_button = Button(text='Add Text', highlightbackground='lightblue',
                     fg='black', width=20, command=add_text_to_image)

text_input = Entry(width=35, bg='white', fg='black')

canvas = Canvas(width=size[0], height=size[1],
                highlightbackground="black", highlightthickness=2)
canvas.grid(column=1, row=1, columnspan=2)


add_button = Button(text='Add Image', highlightbackground='lightblue',
                    fg='black', width=20, command=add_image)


add_button.grid(column=1, row=0, columnspan=2, padx=10, pady=5)


window.mainloop()
