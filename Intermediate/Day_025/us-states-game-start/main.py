import turtle
import pandas


class State:

    def __init__(self):
        self.name = None
        self.x_coordinate = 0
        self.y_coordinate = 0

    def add_to_map(self):
        showing_a_new_state = turtle.Turtle()
        showing_a_new_state.speed("fastest")
        showing_a_new_state.hideturtle()
        showing_a_new_state.penup()
        showing_a_new_state.color("blue")
        showing_a_new_state.goto(self.x_coordinate, self.y_coordinate)
        showing_a_new_state.write("{}".format(self.name), False, "center", ('Arial', 8, 'normal'))


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_db = pandas.read_csv("50_states.csv")

states_list = []

for state in states_db.state:
    new_state = State()
    get_line = states_db[states_db.state == state]
    new_state.name = str(get_line.state.tolist()[0])
    new_state.x_coordinate = int(get_line.x.tolist()[0])
    new_state.y_coordinate = int(get_line.y.tolist()[0])
    states_list.append(new_state)

game_is_on = True
number_of_states = len(states_list)
correct_guesses = []
while game_is_on and len(correct_guesses) < number_of_states:
    answer = screen.textinput(("{}/{} States Correct".format(len(correct_guesses), number_of_states)),
                              "What's another state's name?").lower()
    if answer == "exit":
        states_to_learn = [state.name for state in states_list if state not in correct_guesses]
        break
    for state in states_list:
        if state.name.lower() == answer:
            if state not in correct_guesses:
                state.add_to_map()
                correct_guesses.append(state)



data = pandas.DataFrame(states_to_learn)
data.to_csv("states_to_learn.csv")