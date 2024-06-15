# _____Copyright © 2024 FaroukAshraf_____

# _________Libraries__________
import ttkbootstrap as ttk
from tkinter import PhotoImage


def Random():
    # ________Main_Window________

    window1 = ttk.Window()
    window1.title("Random Selection")
    window1.geometry("920x400")
    window1.configure(bg = "#AAD7FF")
    window1.position_center()


    # ________Canvas________
    canvas = ttk.Canvas(
        window1,
        height = 360,
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
    
    # ________Text________
    canvas.create_text(
        23,
        30,
        anchor="nw",
        text="How does Random Selection work?",
        fill="#000000",
        font=("K2D Medium", 24 * -1)
    )

    canvas.create_text(
        10,
        55,
        anchor="nw",
        text="""
    Random Selection:

        This technique randomly selects a parent from the population. In terms of 
        disruption of genetic codes, random selection is a little more disruptive,
        on average, than roulette wheel selection solutions, and therefore this 
        strategy is usually avoided
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    window1.mainloop()

if __name__ == "__main__":
    Random()