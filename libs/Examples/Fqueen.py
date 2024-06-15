import turtle


def Queen(Chrom,n):

    def board(Chrom,n):
        # Chessboard dimensions and square size
        board_size = 8
        square_size = 800 // board_size  # Adjust square size based on board size

        # Setting up the turtle
        window = turtle.Screen()
        window.setup(800,800)
        window.title("N-queen")
        window.register_shape(r"libs\Examples\assets\Farouk_assets\queen.gif")
        window.bgcolor("white")  # Set background color to black
        window.tracer(0)
        Q = turtle.Turtle()
        pen = turtle.Turtle()
        pen.hideturtle()


        # Function to draw a square (used for chessboard)
        def DrawSquare(color):
            pen.fillcolor(color)
            pen.begin_fill()
            for _ in range(4):
                pen.forward(square_size)
                pen.left(90)
            pen.end_fill()

        # Function to draw the chessboard
        def DrawBoard():
            for row in range(board_size):
                for col in range(board_size):
                    color = "black" if (row + col) % 2 == 0 else "gray"
                    pen.penup()
                    pen.goto((col * -square_size)+300, (row * -square_size)+300)
                    pen.pendown()
                    DrawSquare(color)
        DrawBoard()

        def Queen(chrom,n):
            img = r"libs\Examples\assets\Farouk_assets\queen.gif"
            Q.shape(img)
            Q.shapesize(3)
            Q.pu()
            for i in range(n):
                Q.goto((-350)+(100*i), (-450)+(100*chrom[i]))
                Q.stamp()
        Queen(Chrom,n)
        window.mainloop()

    board(Chrom,n)

if __name__ == "__main__":
    Queen([4,2,1,3,1,4,6,7],8)





    # def queen(chrom):
    #     window.update()
    #     a = turtle.Turtle(); b = turtle.Turtle(); c = turtle.Turtle(); d = turtle.Turtle()
    #     e = turtle.Turtle(); f = turtle.Turtle(); g = turtle.Turtle(); h = turtle.Turtle()
    #     a.color("blue")
    #     a.shape('turtle');a.shapesize(3);b.shape('turtle');b.shapesize(3)
    #     c.shape('turtle');c.shapesize(3);d.shape('turtle');d.shapesize(3)
    #     e.shape('turtle');e.shapesize(3);f.shape('turtle');f.shapesize(3)
    #     g.shape('turtle');g.shapesize(3);h.shape('turtle');h.shapesize(3)
    #     a.goto(-360, (-450)+(100*chrom[0]));b.goto(-260, (-450)+(100*chrom[1]))
    #     c.goto(-160, (-450)+(100*chrom[2]));d.goto(-60, (-450)+(100*chrom[3]))
    #     e.goto(40, (-450)+(100*chrom[4]));f.goto(140, (-450)+(100*chrom[5]))
    #     g.goto(240, (-450)+(100*chrom[6]));h.goto(340, (-450)+(100*chrom[7]))


    # queen([1,5,8,7,2,3,3,4])







# from tkinter import *
# import ttkbootstrap as ttk

# # Create the main window
# root = ttk.Window(themename="darkly")
# root.title("Dropdown with Menubutton")

# def command1():
#   print("Command 1 Executed")

# def command2():
#   print("Command 2 Executed")

# def command3():
#   print("Command 3 Executed")

# # Create the menubutton and its menu
# dropdown_menu = ttk.Menu(root)
# dropdown_menu.add_command(label="Option 1", command=command1)
# dropdown_menu.add_command(label="Option 2", command=command2)
# dropdown_menu.add_command(label="Option 3", command=command3)

# dropdown = ttk.Menubutton(root, menu=dropdown_menu, bootstyle="warning")
# dropdown.pack(pady=20)

# root.mainloop()