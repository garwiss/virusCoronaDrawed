
import turtle
import os

colors = ["lightgrey","grey","yellow", "red", "green", "blue","purple","lightgrey","grey"]

while True:
    a = 0
    b = 0

    turtle.bgcolor("black")
    turtle.speed(0)

    turtle.penup()
    turtle.goto(0, 200)
    turtle.pendown()

    for color in colors:
        a = 0
        b = 0
        turtle.pencolor(color)

        while True:
            turtle.forward(a)
            turtle.right(b)
            a += 3
            b += 1
            if b == 200:
                break


# import turtle
# import os


# # Renk listesi
# colors = ["yellow", "red", "green", "blue", "purple"]  
# while True:
#     a = 0
#     b = 0

#     turtle.bgcolor("black")
#     turtle.speed(0)
# #     turtle.pencolor("green")
#     turtle.penup()
#     turtle.goto(0, 200)
#     turtle.pendown()

#     for color in colors:  # Renk listesini döngüye alıyoruz
#         turtle.pencolor(color)  # Her döngü adımında bir sonraki rengi seçiyoruz
        
#         while True:
#             turtle.forward(a)
#             turtle.right(b)
#             a += 3
#             b += 1
#             if b == 200:
#                 break
#     # os.system("corona.py")
