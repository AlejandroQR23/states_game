
import turtle
import pandas

def get_mouse_coordinates(x, y):
    print( x, y )

screen = turtle.Screen()
screen.title( "U.S. States Game" )

us_image =  "blank_states_img.gif"

# * Add US image to the GUI
turtle.addshape( us_image )
turtle.shape( us_image )

# * Get each state coordinates
# turtle.onscreenclick( get_mouse_coordinates )

# * Read the csv file
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    guessed = len(guessed_states)
    
    # * Get the user answer
    input_state = screen.textinput( title=f"{guessed}/50 Guess the state", prompt="What's another state's name?" ).title()

    # * Check the user answer
    if input_state in states:
        guessed_states.append( input_state )

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[ data.state == input_state ]
        t.goto( int(state_data.x), int(state_data.y) )
        t.write( input_state )

turtle.mainloop()