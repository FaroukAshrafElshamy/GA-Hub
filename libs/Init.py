# ________©FaroukAshraf________

# ________Libraries____________
import ttkbootstrap as ttk
from tkinter import PhotoImage


def Init():
    # ________Main_Window________

    window1 = ttk.Window()
    window1.title("Initial Population")
    window1.geometry("920x520")
    window1.configure(bg = "#AAD7FF")
    window1.position_center()


    # ________Canvas________
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
    
    # ________Images________
    Photo = PhotoImage(master = window1, file = r"libs\assets\Init.png")
    label = ttk.Label(master= window1, image= Photo)
    label.place(x=170 , y=135)

    # ________Text________
    canvas.create_text(
        23,
        20,
        anchor="nw",
        text="What is Initial Population?",
        fill="#000000",
        font=("K2D Medium", 24 * -1)
    )

    canvas.create_text(
        5,
        30,
        anchor="nw",
        text="""
    Initial Population: It refers to the first generation of candidate solutions and it is randomly 
    generated, it consists of a set of Chromosomes (Solutions), each one has a set of Genes.
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        550,
        155,
        anchor="nw",
        text="Gene",
        fill="Red",
        font=("K2D Medium", 28 * -1)
    )

    canvas.create_text(
        550,
        235,
        anchor="nw",
        text="Chromosome",
        fill="#00C100",
        font=("K2D Medium", 28 * -1)
    )

    canvas.create_text(
        550,
        389,
        anchor="nw",
        text="Population",
        fill="#FF00FF",
        font=("K2D Medium", 28 * -1)
    )

    window1.mainloop()

if __name__ == "__main__":
    Init()