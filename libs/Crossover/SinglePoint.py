# ________©FaroukAshraf________

# ________Libraries____________
import ttkbootstrap as ttk
from tkinter import PhotoImage

def SinglePoint():
    window1 = ttk.Window()
    window1.title("Single-Point Crossover")
    window1.geometry("920x520")
    window1.configure(bg = "#AAD7FF")
    window1.position_center()


    canvas = ttk.Canvas(
        window1,
        height = 480,
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

    Photo = PhotoImage(master = window1, file = r"libs\assets\image1.png")
    label = ttk.Label(master= window1, image= Photo)
    label.place(x=180 , y=245)

    canvas.create_text(
        61,
        254,
        anchor="nw",
        text="Parent 1",
        fill="#000000",
        font=("K2D Medium", 18 * -1)
    )

    canvas.create_text(
        61,
        312,
        anchor="nw",
        text="Parent 2",
        fill="#000000",
        font=("K2D Medium", 18 * -1)
    )

    canvas.create_text(
        10,
        65,
        anchor="nw",
        text="""
    Single Point Crossover: A crossover point on the parent organism string is selected. All data
    beyond that point in the organism string is swapped between the two parent organisms.
    Strings are characterized by Positional Bias.
        """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        23,
        40,
        anchor="nw",
        text="How does single-point crossover work?",
        fill="#000000",
        font=("K2D Medium", 24 * -1)
    )

    window1.mainloop()

if __name__ == "__main__":
    SinglePoint()