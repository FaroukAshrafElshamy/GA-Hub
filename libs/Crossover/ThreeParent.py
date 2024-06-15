# ________©FaroukAshraf________

# ________Libraries____________
import ttkbootstrap as ttk
from tkinter import PhotoImage


def ThreeParent():
    # ________Main_Window________

    window1 = ttk.Window()
    window1.title("Three-Parent Crossover")
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
    Photo = PhotoImage(master = window1, file = r"libs\assets\Three_P.png")
    label = ttk.Label(master= window1, image= Photo)
    label.place(x=140 , y=200)

    Photo1 = PhotoImage(master = window1, file = r"libs\assets\Three_P1.png")
    label1 = ttk.Label(master= window1, image= Photo1)
    label1.place(x=580 , y=290)

    # ________Text________
    canvas.create_text(
        30,
        210,
        anchor="nw",
        text="Parent 1",
        fill="#000000",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        30,
        285,
        anchor="nw",
        text="Parent 2",
        fill="#000000",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        490,
        285,
        anchor="nw",
        text="Child",
        fill="#000000",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        30,
        360,
        anchor="nw",
        text="Parent 3",
        fill="#000000",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        10,
        65,
        anchor="nw",
        text="""
    Three-Parent Crossover : This technique has three parents , If first and second parent have
    the same gene then the child will take this gene other wise the gene will be taken from
    the third parent.  
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        23,
        40,
        anchor="nw",
        text="How does Three-Parent crossover work?",
        fill="#000000",
        font=("K2D Medium", 24 * -1)
    )

    window1.mainloop()

if __name__ == "__main__":
    ThreeParent()