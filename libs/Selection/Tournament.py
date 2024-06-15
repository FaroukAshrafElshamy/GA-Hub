# _____Copyright © 2024 FaroukAshraf_____

# _________Libraries__________
import ttkbootstrap as ttk
from tkinter import PhotoImage


def Tournament():
    # ________Main_Window________

    window1 = ttk.Window()
    window1.title("Tournament Selection")
    window1.geometry("920x850")
    window1.configure(bg = "#AAD7FF")
    window1.position_center()


    # ________Canvas________
    canvas = ttk.Canvas(
        window1,
        height = 810,
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
    Photo = PhotoImage(master = window1, file = r"libs\assets\Tour.png")
    label = ttk.Label(master= window1, image= Photo)
    label.place(x=65 , y=350)

    # ________Text________
    canvas.create_text(
        23,
        30,
        anchor="nw",
        text="How does Tournament Selection work?",
        fill="#000000",
        font=("K2D Medium", 24 * -1)
    )

    canvas.create_text(
        10,
        55,
        anchor="nw",
        text="""
    Tournament Selection: It is a method used to pick individuals for reproduction in the next 
    generation.Unlike roulette selection, it involves a more direct competition between candidate
    solutions.
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        10,
        145,
        anchor="nw",
        text="""
    Tournament Technique:

        In K-Way tournament selection, we select K individuals from the population at random and
        selectthe best out of these to become a parent. The same process is repeated for selecting 
        the next parent.Tournament Selection is also extremely popular in literature as it can even
        work with negative fitness values.
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    window1.mainloop()

if __name__ == "__main__":
    Tournament()