import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import tkinter
from PIL import Image, ImageTk, ImageDraw, ImageFont
import math

images = []

window = Tk()
start = '/Users/brock/Desktop/icons'
# window.geometry("800x800")
size = (350, 400)
# size = (800, 800)

window.title("Watermark")
window.config(padx=20, pady=10, bg="grey",
              cursor="hand2")

labels = []

font_options = ['Times', 'Arial', 'Duude']
v = font_options[0]

mod_image = ""

# text_value = ""


def show_labels():
    for x in range(0, len(labels)):
        labels[x].grid(column=1, row=x+1)


POPUP_COLOR = "lightgrey"
text_input = ""
size_slider = ""
font_variable = ""
x_location_slider = ""
y_location_slider = ""
photo_x_max = 500
photo_y_max = 500
# photo_x_max = ""
# photo_y_max = ""
relpath = ""
color_picker = (255, 255, 255)
water_marked_pic = ""

fonts = {
    'Impact': '/System/Library/Fonts/Supplemental/Impact.ttf',
    'Arial': '/System/Library/Fonts/Supplemental/Arial.ttf',
    'Times New Roman': '/System/Library/Fonts/Supplemental/Times New Roman.ttf'
}


def change_color():
    global color_picker
    colors = askcolor(title="Choose Color")
    temp = colors[0]
    color_picker = tuple([math.floor(x) for x in temp])


def print_info(event):
    global water_marked_pic
    image1 = Image.open(relpath)
    watermark = text_input.get()
    style = font_variable.get()

    draw = ImageDraw.Draw(image1)
    font_style = fonts[style]
    font = ImageFont.truetype(font_style, size_slider.get())
    draw.text((x_location_slider.get(), y_location_slider.get()),
              watermark, color_picker, font=font)

    water_marked_pic = image1

    image1.thumbnail(size, Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    canvas.destroy()
    label1.grid(column=1, row=1, columnspan=2)
    labels.append(label1)


def save_pic():
    global water_marked_pic
    water_marked_pic.save(
        f"{start}/" + f"{images[0]['file_name']}_watermark.png", "png")


def add_text_to_image():
    global text_input, size_slider, font_variable, x_location_slider, y_location_slider, photo_y_max, photo_x_max
    # print("Photo x max:", photo_x_max, "Photo y max:", photo_y_max)
    pop_up = Toplevel(window)
    pop_up.title("Add Text")
    pop_up.config(padx=20, pady=10, bg=POPUP_COLOR)
    # Text
    text_label = Label(pop_up, text='Text ', bg=POPUP_COLOR)
    text_label.grid(pady=2, column=1, row=0)
    text_input = tkinter.Entry(pop_up, width=35, fg=POPUP_COLOR)
    # text_input.config(comm)
    text_input.grid(pady=2, column=2, row=0, columnspan=3)
    text_input.insert(0, 'Text')
    # Font
    font_label = Label(pop_up, text='Font ', bg=POPUP_COLOR)
    font_label.grid(pady=2, column=1, row=1)
    font_variable = StringVar()
    font_variable.set('Impact')
    font_input = OptionMenu(pop_up, font_variable, *
                            fonts.keys(), command=print_info)
    font_input.config(width=33, bg=POPUP_COLOR, fg='black')
    font_input.grid(pady=2, column=2, row=1, columnspan=3)
    # Font Size
    size_label = Label(pop_up, text='Size ', bg=POPUP_COLOR)
    size_label.grid(pady=2, column=1, row=2)
    current_value = DoubleVar(pop_up)
    current_value.set(10)
    size_slider = Scale(pop_up, from_=10, to=100,
                        orient='horizontal', variable=current_value, command=print_info)
    size_slider.config(bg=POPUP_COLOR, fg='black')
    size_slider.grid(pady=2, column=2, row=2, columnspan=2)

    # Color
    color_button = Button(pop_up, text='Color', fg='black', highlightbackground='black',
                          width=20, command=change_color)
    color_button.grid(pady=2, column=4, row=2, padx=10)

    # Text Location Horizontal
    x_location_label = Label(pop_up, text='X Location ', bg=POPUP_COLOR)
    x_location_label.grid(pady=2, column=1, row=3)
    x_value = DoubleVar(pop_up)
    x_value.set(0)
    x_location_slider = Scale(pop_up, from_=0, to=photo_x_max,
                              orient='horizontal', variable=x_value, command=print_info)
    x_location_slider.config(bg=POPUP_COLOR, fg='black')
    x_location_slider.grid(pady=2, column=2, row=3)
    # Text Location Vertical
    y_location_label = Label(pop_up, text='Y Location ', bg=POPUP_COLOR)
    y_location_label.grid(pady=2, column=3, row=3)
    y_value = DoubleVar(pop_up)
    y_value.set(0)
    y_location_slider = Scale(pop_up, from_=0, to=photo_y_max,
                              orient='vertical', variable=y_value, command=print_info)
    y_location_slider.config(bg=POPUP_COLOR, fg='black')
    y_location_slider.grid(pady=2, column=4, row=3)
    # Button
    save_pic_button = Button(pop_up, text='Save Image', fg='black', highlightbackground='black',
                             width=20, command=save_pic)
    save_pic_button.grid(pady=2, column=1, row=100, padx=10, columnspan=4)

    # print_info(event=)


def add_image():
    global mod_image, photo_y_max, photo_x_max, relpath
    for widget in labels:
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir=start, title="Select Images",
                                          filetypes=(("Images", ".png"), ("Images", ".jpg"), ("Images", ".jpeg")))
    # filetypes=(("Images", (".png", ".jpg", ".jpeg"))))
    relpath = os.path.relpath(filename)
    image1 = Image.open(relpath)

    # print("IMAGE 1 SIZE:", image1.size)

    photo_x_max = image1.size[0]
    photo_y_max = image1.size[1]

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
    # create_text_label()
    if label1:
        add_text_button.config(highlightbackground='white',
                               command=add_text_to_image)


def need_image():
    messagebox.showinfo(title='Attention',
                        message=f"Image Select Needed")


canvas = Canvas(width=size[0], height=size[1],
                highlightbackground="black", highlightthickness=2)
canvas.grid(column=1, row=1, columnspan=2)


add_image_button = Button(text='Add Image', fg='black', highlightbackground='white',
                          width=20, command=add_image)
add_image_button.grid(column=1, row=0, padx=10, pady=5)


add_text_button = Button(text='Add Text', fg='black', highlightbackground='black',
                         width=20, command=need_image)
add_text_button.grid(column=2, row=0, padx=10, pady=5)
# add_text_to_image()
window.mainloop()
