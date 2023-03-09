import turtle
import pandas

# Intro code
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
t = turtle.Turtle()

while len(guessed_states) != 50:
    state_answer = screen.textinput(title=f"Guess the state {len(guessed_states)}/50",
                                    prompt="What's another state's name?").title()
    if state_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # or
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states_csv = pandas.DataFrame(missing_states)
        missing_states_csv.to_csv("Missing States.csv")
        break
    if state_answer in all_states:
        guessed_states.append(state_answer)
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_answer)
        # Or
        # t.write(state_data.state.item())
