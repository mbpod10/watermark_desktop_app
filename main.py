import os
import sys
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

images = []

window = Tk()
window.geometry('750x1250')
start = '/Users/brock/Desktop/icons'
size = (359, 296)

window.title("Image Converter")
window.config(padx=50, pady=50, bg="grey",
              cursor="hand2")

labels = []


def show_labels():
    for x in range(0, len(labels)):
        labels[x].grid(column=1, row=x+1)


def add_image():
    filename = filedialog.askopenfilename(initialdir=start, title="Select Images",
                                          filetypes=(("images", ".png"), ("images", ".jpg"), ("images", ".jpeg")))
    relpath = os.path.relpath(filename)
    image1 = Image.open(relpath)
    images.append(
        {"PIL_image": image1, "file_name": relpath.split("/")[-1].split(".")[0]})
    image1.thumbnail(size)
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    labels.append(label1)
    show_labels()


def convert_image_to_png():
    for img in images:
        to_png = img["PIL_image"].convert("RGB")
        to_png.save(f"{start}/" + f"{img['file_name']}.png", "png")


add_button = Button(text='Add Image', highlightbackground='lightblue',
                    fg='black', width=20, command=add_image)
add_button.grid(column=3, row=1, columnspan=2)

convert_button = Button(text='Convert To Png', highlightbackground='lightblue',
                        fg='black', width=20, command=convert_image_to_png)
convert_button.grid(column=3, row=2, columnspan=2)

window.mainloop()
