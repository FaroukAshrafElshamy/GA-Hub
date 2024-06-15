# ________©FaroukAshraf________
# ________Libraries____________
from Utility import *


# ________Main_Window________
window = ttk.Window()
x = window.winfo_screenwidth()
y = window.winfo_screenheight()
window.geometry(f"{int(x*0.75)}x{int(y*0.75)}")
window.title("Farouk Ashraf")
window.position_center()

# ________Canvas________
canvas = ttk.Canvas(
    window,
    bg = "#030F32",
    height = 810,
    width = 1440,
)

canvas.place(x = 0, y = 0)
WindowImage = PhotoImage(
    master=window,
    file=r"assets\image_1.png")

WinImage1 = canvas.create_image(
    720,
    408,
    image=WindowImage
)

# _______Examples_______
FaroukButton = PhotoImage(
    master=window,
    file=r"assets\button_2.png")
Fbutton = Button(
    master=window,
    image=FaroukButton,
    command=Farouk,
    cursor="hand2"
)
Fbutton.place(
    x=521,
    y=236,
    width=145,
    height=96
)


NadaButton = PhotoImage(
    master=window,
    file=r"assets\button_1.png")
Nbutton = Button(
    master=window,
    image=NadaButton,
    command=Nada,
    cursor="hand2"
)
Nbutton.place(
    x=690,
    y=236,
    width=145,
    height=96
)


AhlamButton = PhotoImage(
    master=window,
    file=r"assets\Abutton.png")
Abutton = Button(
    master=window,
    image=AhlamButton,
    command=Ahlam,
    cursor="hand2"
)
Abutton.place(
    x=860,
    y=236,
    width=145,
    height=96
)


AhmedButton = PhotoImage(
    master=window,
    file=r"assets\Abutton2.png")
Abutton2 = Button(
    master=window,
    image=AhmedButton,
    command=Ahmed,
    cursor="hand2"
)
Abutton2.place(
    x=1032,
    y=236,
    width=145,
    height=96
)


RahmaButton = PhotoImage(
    master=window,
    file=r"assets\Rbutton.png")
Rbutton = Button(
    master=window,
    image=RahmaButton,
    command=Rahma,
    cursor="hand2"
)
Rbutton.place(
    x=1203,
    y=236,
    width=145,
    height=96
)


AmaalButton = PhotoImage(
    master=window,
    file=r"assets\Abutton3.png")
Abutton3 = Button(
    master=window,
    image=AmaalButton,
    command=Amaal,
    cursor="hand2"
)
Abutton3.place(
    x=521,
    y=350,
    width=145,
    height=96
)

# _______Buttons_______

ButtonImage1 = PhotoImage(
    master=window,
    file=r"assets\button3.png")
Button1 = Button(
    master=window,
    image=ButtonImage1,
    command= Replacement,
    cursor="hand2"
)
Button1.place(
    x=104,
    y=674,
    width=282,
    height=43
)


ButtonImage2 = PhotoImage(
    master=window,
    file=r"assets\button_3.png")
Button2 = Button(
    master=window,
    image=ButtonImage2,
    command=Mutation,
    cursor="hand2"
)
Button2.place(
    x=104,
    y=584,
    width=282,
    height=43
)


ButtonImage3 = PhotoImage(
    master=window,
    file=r"assets\button_4.png")
Button3 = Button(
    master=window,
    image=ButtonImage3,
    command=Crossover,
    cursor="hand2"
)
Button3.place(
    x=104,
    y=497,
    width=282,
    height=43
)


ButtonImage4 = PhotoImage(
    master=window,
    file=r"assets\button_5.png")
Button4 = Button(
    master=window,
    image=ButtonImage4,  
    command=Select,
    cursor="hand2"
)
Button4.place(
    x=104,
    y=408,
    width=282,
    height=43
)


ButtonImage5 = PhotoImage(
    master=window,
    file=r"assets\button_6.png")
Button5 = Button(
    master=window,
    image=ButtonImage5,
    command=Fitness,
    cursor="hand2"
)
Button5.place(
    x=105,
    y=323,
    width=282,
    height=43
)


ButtonImage6 = PhotoImage(
    master=window,
    file=r"assets\button_7.png")
Button6 = Button(
    master=window,
    image=ButtonImage6,
    command=Init,
    cursor="hand2"
)
Button6.place(
    x=104,
    y=232,
    width=285,
    height=47
)

# _______Arrows_______

Image2 = PhotoImage(
    master=window,
    file=r"assets\image_2.png")
Image_2 = canvas.create_image(
    245,
    562,
    image=Image2
)


Image3 = PhotoImage(
    master=window,
    file=r"assets\image_3.png")
Image_3 = canvas.create_image(
    245,
    650,
    image=Image3
)


Image4 = PhotoImage(
    master=window,
    file=r"assets\image_4.png")
Image_4 = canvas.create_image(
    245,
    386,
    image=Image4
)


Image5 = PhotoImage(
    master=window,
    file=r"assets\image_5.png")
Image_5 = canvas.create_image(
    245,
    300,
    image=Image5
)


Image6 = PhotoImage(
    master=window,
    file=r"assets\image_6.png")
Image_6 = canvas.create_image(
    245,
    475,
    image=Image6
)


canvas.create_rectangle(
    477,
    140,
    478,
    768,
    fill="#93B1FF",
    outline=''
)


window.resizable(False, False)
window.mainloop()