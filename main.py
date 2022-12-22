import PIL.Image
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk


root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")


def BMI():
    h = float(Height.get())
    w = float(Weight.get())

    # convert
    m = h/100
    bmi = round(float(w/m**2), 1)
    # print(bmi)
    label1.config(text=bmi)

    # you can Change

    if bmi <= 18.5:
        label2.config(text="Under Weight!!")
        label3.config(text="It indicates that you are healthy!")

    elif bmi > 18.5 and bmi <= 25:
        label2.config(text="Normal")
        label3.config(text="You have lower weight then normal body!")

    elif bmi > 25 and bmi <= 30:
        label2.config(text="Under Weight!!")
        label3.config(
            text="It indicates that a person is \n slightly overweight! \n A doctor may advise to lose some \n Weight!")

    else:
        label2.config(text="Obes!!")
        label3.config(
            text="Health may be at risk, if they do not \n lose weight🙀😥")


# icon
image_icon = PhotoImage(file="D:\\practise\\BMI\\icon.png")
root.iconphoto(False, image_icon)

# Top
top = PhotoImage(file="D:\\practise\\BMI\\top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)

# bottom box
Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)


# two boxes
box = PhotoImage(file="D:\\practise\\BMI\\box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)


# scale
scale = PhotoImage(file="D:\\practise\\BMI\\scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=310)


#######################Slider1#################
current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = PIL.Image.open("D:\\practise\\BMI\\man.png")
    # img.show()
    resized_image = img.resize((50, 10+size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550-size)
    secondimage.image = photo2


# Command to change background color for scale
style = ttk.Style()
style.configure("TScale", background="white")


slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale",
                   command=slider_changed, variable=current_value)
slider.place(x=80, y=250)


######################### Slider2@###################
current_value2 = tk.DoubleVar()


def get_current_value2():
    return '{: .2f}'.format(current_value2.get())


def slider_changed2(event):
    Weight.set(get_current_value2())


# Command to change background color for scale
style2 = ttk.Style()
style2.configure("TScale", background="white")


slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale",
                    command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)


# Entry box

Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5,
               font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())


weight = Entry(root, textvariable=Weight, width=5,
               font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())


# man image
secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y=530)


Button(root, text="view Report", width=15, height=2,
       font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=280, y=340)


label1 = Label(root, font="arial 60 bold", bg="lightblue", fg="#fff")
label1.place(x=125, y=305)

label2 = Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=280, y=430)

label3 = Label(root, font="arial 10 bold", bg="lightblue")
label3.place(x=200, y=500)


root.mainloop()
