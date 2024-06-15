# ________©FaroukAshraf________
"""
This Python file serves as a container for calling libraries, 
which helps to enhance the readability of the code.
"""

import ttkbootstrap as ttk
from tkinter import PhotoImage, Button
from libs.Init import Init
from libs.fitness import Fitness
from libs.Selection.Select import Select
from libs.Crossover.Crossover import Crossover
from libs.Mutation.Mutation import Mutation
from libs.Replacement import Replacement


# _______Crossover_______
from libs.Crossover.SinglePoint import SinglePoint
from libs.Crossover.TwoPoint import TwoPoint
from libs.Crossover.Uniform import Uniform
from libs.Crossover.ThreeParent import ThreeParent 

# _______Mutation_______
from libs.Mutation.BitFlib import BitFlib
from libs.Mutation.Interchanging import Interchanging 
from libs.Mutation.Reversing import Reversing


# _______Selection_For_Rejmain_______
from libs.Selection.Rolletwheel import RolletWheel
from libs.Selection.Tournament import Tournament
from libs.Selection.Rank import Rank
from libs.Selection.Random import Random


# _______Examples_______
from libs.Examples.Farouk import Farouk
from libs.Examples.Nada import Nada
from libs.Examples.Ahlam import Ahlam
from libs.Examples.Ahmed import Ahmed
from libs.Examples.Rahma import Rahma
from libs.Examples.Amaal import Amaal
