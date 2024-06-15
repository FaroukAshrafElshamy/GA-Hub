# _____Copyright © 2024 FaroukAshraf_____

# _________Libraries__________
import ttkbootstrap as ttk
from tkinter import PhotoImage


def RolletWheel():
    # ________Main_Window________

    window1 = ttk.Window()
    window1.title("Roulette wheel selection ")
    window1.geometry("920x820")
    window1.configure(bg = "#AAD7FF")
    window1.position_center()


    # ________Canvas________
    canvas = ttk.Canvas(
        window1,
        height = 780,
        width = 880
    )
    canvas.place(x = 20, y = 20)
    
    canvas.create_rectangle(
        14,
        19,
        886,
        481,
        fill="#FFFFFF",
        outline="")
    
    # ________Images________
    Photo = PhotoImage(master = window1, file = r"libs\assets\R11.png")
    label = ttk.Label(master= window1, image= Photo)
    label.place(x=80 , y=440)

    Photo1 = PhotoImage(master = window1, file = r"libs\assets\R12.png")
    label1 = ttk.Label(master= window1, image= Photo1)
    label1.place(x=450 , y=480)

    # ________Text________
    canvas.create_text(
        23,
        30,
        anchor="nw",
        text="How does Roulette wheel selection work?",
        fill="#000000",
        font=("K2D Medium", 24 * -1)
    )

    canvas.create_text(
        10,
        55,
        anchor="nw",
        text="""
    Roulette wheel: is a common method in genetic algorithms to choose parents for the next 
    generation. It favors individuals with higher fitness scores but allows some chance for
    less fit ones to be selected as well.
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        10,
        155,
        anchor="nw",
        text="""
    Roulette Technique:

        1- Each individual is assigned to a part of the wheel based on its fitness.

        2- Spin the wheel k times to select the best individuals.

        3- Fitness individual has the largest share of the roulette wheel and
           weakest individual has the smallest share of the roulette wheel.
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    window1.mainloop()

if __name__ == "__main__":
    RolletWheel()