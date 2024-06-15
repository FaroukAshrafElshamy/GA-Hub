# ________©FaroukAshraf________

# ________Libraries____________
import ttkbootstrap as ttk
from tkinter import PhotoImage


def Fitness():
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

    # ________Text________
    canvas.create_text(
        23,
        40,
        anchor="nw",
        text="What is Fitness Function?",
        fill="#000000",
        font=("K2D Medium", 24 * -1)
    )

    canvas.create_text(
        5,
        80,
        anchor="nw",
        text="""
    Fitness Function: It acts like a compass, guiding the algorithm towards optimal solutions.
    It essentially evaluates the quality of each candidate solution (individual) in the population.
    
    Here are some additional points to consider:

        • The design of the fitness function is crucial for the success of the GA.
          It needs to accurately reflect the problem's goals and be efficient to compute.
        
        • In some cases, directly calculating the fitness might be complex.
          In such scenarios, approximations or penalty functions can be used.

        • Higher the fitness score, greater are the chances of an individual getting 
          selected for reproduction.
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    window1.mainloop()

if __name__ == "__main__":
    Fitness()