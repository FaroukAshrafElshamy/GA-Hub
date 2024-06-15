# ________Copyright © 2024 FaroukAshraf________

# ________Libraries____________
from Utility import *

# _______Parameters_______
ButtonWidth = 19

# Main window
window = ttk.Window()
window.title("Genetic Algorithms")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{3*screen_width//4}x{3*screen_height//4}")
window.position_center()


# Text
Text = ttk.Label(
    master= window,
    text="How Does Genetic Algorithms Work?",
    font="Calibri 25 bold",
)
Text.pack()

# Frame1
my_frame = ttk.Frame(window, bootstyle="default")
label = ttk.Label(my_frame,
    text="Explanation of the main methods",
    font="Calibri 25 bold"
    )

label.pack(anchor='w',pady=20,padx=10)


# Button
button = ttk.Button(
    my_frame,
    text="Initial Population",
    width=ButtonWidth+5,
    command= Init
    )
button.pack(side="left", padx=20)

button = ttk.Button(
    my_frame,
    text="Fitness Evaluation",
    width=ButtonWidth+5,
    command= Fitness
    )
button.pack(side="left", padx=20)


# Dropdown menu
dropdown = ttk.Menu(my_frame)
dropdown.add_command(label="Roulette Wheel", command= RolletWheel)
dropdown.add_command(label="Tournament", command= Tournament)
dropdown.add_command(label="Rank method", command= Rank)
dropdown.add_command(label="Random", command= Random)

dropdown_menu = ttk.Menubutton(
    my_frame,
    text= "Selection",
    menu=dropdown,
    width=ButtonWidth
    )
dropdown_menu.pack(side="left", padx=20)

# Dropdown menu 1
dropdown = ttk.Menu(my_frame)

dropdown.add_command(label="Single-point Crossover", command=SinglePoint)
dropdown.add_command(label="Two-point Crossover", command=TwoPoint)
dropdown.add_command(label="Uniform Crossover", command=Uniform)
dropdown.add_command(label="Three-parent Crossover", command = ThreeParent)

dropdown_menu = ttk.Menubutton(
    my_frame,
    text= "Crossover",
    menu=dropdown,
    width=ButtonWidth
    )
dropdown_menu.pack(side="left", padx=20)

# Dropdown menu2
dropdown = ttk.Menu(my_frame)

dropdown.add_command(label="Bit-Flib", command= BitFlib)
dropdown.add_command(label="Interchangeing", command= Interchanging)
dropdown.add_command(label="Reversing", command= Reversing)

dropdown_menu = ttk.Menubutton(
    my_frame,
    text= "Mutaion",
    menu=dropdown,
    width=ButtonWidth
    )
dropdown_menu.pack(side="left", padx=20)


button = ttk.Button(
    my_frame,
    text="Replacement",
    width=ButtonWidth+5,
    command= Replacement
    )
button.pack(side="left", padx=20)


my_frame.pack(side="top", fill= "both",anchor='w' ,pady=20, padx= 10)




# Frame2
my_frame2 = ttk.LabelFrame(window, bootstyle="info",text="Examples")

label = ttk.Label(
    my_frame2,
    text="Some Examples on GA",
    font="Calibri 22 bold"
    )
label.pack(pady=20,padx=20)


button = ttk.Button(
    my_frame2,
    text="N-Queen",
    width=ButtonWidth+5
    )
button.pack(side='left',padx=20, pady=50)

my_frame2.pack(side="bottom", fill= "both", pady=20, padx= 20)

window.mainloop()
