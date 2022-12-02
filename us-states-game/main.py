import turtle
import pandas
import writing


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")


while
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)


# If answer_state is one of the states in all the states of the 50_states.csv
    #If they got it right:
        #Create a turtle to write the name of the state at the state's x and y coordinate
titled_answer_state = answer_state.title()
all_states = data.state.to_list()
if titled_answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.pu()
    state_data = data[data.state == titled_answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state.item())
    # name = writing.Writing(state.state, state.x, state.y)



# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
turtle.mainloop()

# screen.exitonclick()