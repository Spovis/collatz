# visualize the collatz sequence (aka 3x + 1 problem)

import turtle
import random

def generate_sequence(length, max_value):
    # will be the list of lists, each list starts with the next integer
    # and ends with either 1 or the start of another sequence
    print("calculating sequence...")
    sequences = []
    for iter in range(length):
        number = random.randint(1,max_value)
        unique_steps = [] # the unique numbers that this starter number hits
        unique = True
        while unique:
            unique_steps.append(number)
            if number % 2 == 0:
                number = number // 2
            elif number == 1:
                pass
            else:
                number = 3 * number + 1
            if number in unique_steps:
                unique = False
        sequences.append(unique_steps)

    # create a master dict of all numbers which will eventually aslo have their xy coordinates
    # this means that we wont have to repeatedly redraw huge sections of the graph, ergo gooder performance
    # keys are the numbers, values are the xy coordinates and the heading
    # eg {1 : [0,0, 90]}
    master_dict = {}
    for sequence in sequences:
        for number in sequence:
            if number not in master_dict.keys():
                master_dict[number] = [] # we'll get to the xy values and headings once we start graphing
    print("finished the math, will now graph")

    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor("black")
    wn.title("Collatz Sequence")
    wn.setup(width=3840, height=2160) # 4k resolution
    turt = turtle.Turtle()
    turt.hideturtle()
    turt.speed("fastest")
    turt.color(80,80,80)
    turt.width(1)

    progress = 0
    for sequence in sequences:
        print("progress: " + str(progress) + "/" + str(len(sequences)), end="\r")
        progress += 1
        turt.penup()
        turt.goto((-1000,-400))
        turt.setheading(0)
        turt.backward(550)
        turt.pendown()
        sequence = sequence[::-1]
        should_remove_up_to = 0
        for i in range(len(sequence)-1):
            if master_dict[sequence[i]] != []:
                if master_dict[sequence[i+1]] != []:
                    should_remove_up_to = i
        del sequence[:should_remove_up_to]
        if master_dict[sequence[0]]:
            turt.penup()
            turt.goto(master_dict[sequence[0]][0], master_dict[sequence[0]][1])
            turt.setheading(master_dict[sequence[0]][2])
            turt.pendown()
        for number in sequence:
            if master_dict[number] == []:
                master_dict[number] = [turt.xcor(), turt.ycor(), turt.heading()]
            turt.forward(8)
            if number % 2 == 0:
                turt.left(10)
            else:
                turt.right(19)
    print("finished graphing")

    # infinite loop so I can take a screenshot before I close it
    while True:
        pass
generate_sequence(length=300, max_value=68719476737)
