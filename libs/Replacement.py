# _____Copyright © 2024 FaroukAshraf_____

# _________Libraries__________
import ttkbootstrap as ttk
from tkinter import PhotoImage


def Replacement():
    # ________Main_Window________

    window1 = ttk.Window()
    window1.title("Replacement")
    window1.geometry("1100x760")
    window1.configure(bg = "#AAD7FF")
    window1.position_center()


    # ________Canvas________
    canvas = ttk.Canvas(
        window1,
        height = 720,
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

    # ________Text________
    canvas.create_text(
        23,
        30,
        anchor="nw",
        text="How does Replacement work?",
        fill="#000000",
        font=("K2D Medium", 24 * -1)
    )

    canvas.create_text(
        10,
        55,
        anchor="nw",
        text="""
    Replacement: It is the process of introducing new individuals (offspring) into the population and potentially
    removing some of the existing ones (parents) to make space. It's a crucial step that guides the overall 
    evolution towards better solutions.
            """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )

    canvas.create_text(
        10,
        135,
        anchor="nw",
        text="""

    1- Generational Replacement:

        • In this method, the entire parent population is replaced by the newly generated offspring.
        
        • This approach is simpler to implement but can lead to a faster loss of diversity, especially if the offspring
          population is much smaller than the parent population.
        
    2- Steady-State Replacement:

        • This strategy involves replacing a smaller portion of the parent population (typically one or a few individuals)
          with the best offspring at each iteration.
        
        • It allows for a more gradual evolution and helps maintain diversity in the population for a longer period.
        
        • Random Replacement: The children replace two randomly chosen individuals in the population.
        
        • Weak Parent Replacement: a weaker parent is replaced by a strong child.

        • Both Parents: The child replaces the parent.
    
    Terminition: After Replacement, if we got the fittest chromosome the the program will terminate but if the max 
    limit reached then return the best chromosoe.
        """,
        fill="#0063BC",
        font=("K2D Medium", 20 * -1)
    )
    window1.mainloop()

if __name__ == "__main__":
    Replacement()