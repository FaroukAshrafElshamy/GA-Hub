from tkinter import Button, PhotoImage
import ttkbootstrap as ttk
from .Rolletwheel import RolletWheel
from .Tournament import Tournament
from .Rank import Rank
from .Random import Random

def Select():
    window2 = ttk.Window()
    window2.geometry("449x600")
    window2.position_center()

    canvas = ttk.Canvas(
        master=window2,
        bg = "#041A49",
        height = 600,
        width = 449
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        master=window2,
        file=r"libs\assets\image_1.png")
    image_1 = canvas.create_image(
        224,
        300,
        image=image_image_1
    )

    ButtonImage1 = PhotoImage(
        master=window2,
        file=r"libs\assets\button_4.png")
    Button1 = Button(
        master=window2,
        image=ButtonImage1,
        command=RolletWheel,
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
        file=r"libs\assets\button_3.png")
    Button2 = Button(
        master=window2,
        image=ButtonImage2,
        command=Tournament,
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
        file=r"libs\assets\button_2.png")
    Button3 = Button(
        master=window2,
        image=ButtonImage3,
        command=Rank,
        cursor="hand2"
    )
    Button3.place(
        x=66,
        y=366,
        width=319,
        height=69
    )

    ButtonImage4 = PhotoImage(
        master=window2,
        file=r"libs\assets\button_1.png")
    Button4 = Button(
        master=window2,
        image=ButtonImage4,
        command=Random,
        cursor="hand2"
    )
    Button4.place(
        x=66,
        y=459,
        width=319,
        height=69
    )
    window2.resizable(False, False)
    window2.mainloop()

if __name__ == "__main__":
    Select()