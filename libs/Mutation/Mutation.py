from tkinter import PhotoImage,Button
import ttkbootstrap as ttk
from .BitFlib import BitFlib
from .Interchanging import Interchanging
from .Reversing import Reversing


def Mutation():
    window2 = ttk.Window()
    window2.geometry("450x500")
    window2.position_center()

    canvas = ttk.Canvas(
        master=window2,
        bg = "#041A49",
        height = 500,
        width = 450
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        master=window2,
        file=r"libs\assets\Mutation\image_1.png")
    image_1 = canvas.create_image(
        225,
        300,
        image=image_image_1
    )

    ButtonImage1 = PhotoImage(
        master=window2,
        file=r"libs\assets\Mutation\button_3.png")
    Button1 = Button(
        master=window2,
        image=ButtonImage1,
        command=BitFlib,
        cursor="hand2"
    )
    Button1.place(
        x=66,
        y=180,
        width=319,
        height=69
    )

    ButtonImage2 = PhotoImage(
        master=window2,
        file=r"libs\assets\Mutation\button_2.png")
    Button2 = Button(
        master=window2,
        image=ButtonImage2,
        command=Interchanging,
        cursor="hand2"
    )
    Button2.place(
        x=66,
        y=277,
        width=319,
        height=69
    )

    ButtonImage3 = PhotoImage(
        master=window2,
        file=r"libs\assets\Mutation\button_1.png")
    Button3 = Button(
        master=window2,
        image=ButtonImage3,
        command=Reversing,
        cursor="hand2"
    )
    Button3.place(
        x=66,
        y=366,
        width=319,
        height=69
    )

    window2.resizable(False, False)
    window2.mainloop()

if __name__ == "__main__":
    Mutation()