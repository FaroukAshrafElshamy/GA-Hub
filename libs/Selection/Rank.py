# _____Copyright © 2024 FaroukAshraf_____

# _________Libraries__________
import ttkbootstrap as ttk
from tkinter import PhotoImage


def Rank():
    # ________Main_Window________

    window1 = ttk.Window()
    window1.title("Rank Selection")
    window1.geometry("1100x780")
    window1.configure(bg = "#AAD7FF")
    window1.position_center()


    # ________Canvas________
    canvas = ttk.Canvas(
        window1,
        height = 740,
        width = 1060
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
    Photo = PhotoImage(master = window1, file = r"libs\assets\rank.png")
    label = ttk.Label(master= window1, image= Photo)
    label.place(x=30 , y=450)

    Photo1 = PhotoImage(master = window1, file = r"libs\assets\rank2.png")
    label1 = ttk.Label(master= window1, image= Photo1)
    label1.place(x=550 , y=500)

    # ________Text________
    canvas.create_text(
        23,
        30,
        anchor="nw",
        text="How does Rank Selection work?",
        fill="#000000",
        font=("K2D Medium", 24 * -1)
    )

    canvas.create_text(
        10,
        55,
        anchor="nw",
        text="""
    Rank selection: is a different approach in GA for selecting individuals to become parents in the nextgeneration. 
    Instead of directly using fitness values, it focuses on the relative ranking of solutions based on their fitness.
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        10,
        135,
        anchor="nw",
        text="""
    Rank Technique:

        • Ranking: First, the entire population is sorted according to their fitness score, with the fittest individual 
        having rank 1 and the least fit having the lowest rank (equal size ranks for ties are possible).
        
        • Selection Probability: Then, a selection probability is assigned to each individual based on their rank, 
        not their actual fitness value. Higher ranks get a higher probability of being selected.

        • Selection Process: There are different ways to assign these probabilities, but generally, fitter individuals 
        (higher ranks) have a better chance of being chosen for reproduction.
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )
    window1.mainloop()

if __name__ == "__main__":
    Rank()