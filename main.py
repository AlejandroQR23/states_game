
import turtle

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

# * Get the user answer
input_state = screen.textinput( title="Guess the state", prompt="What's another state's name?" )

turtle.mainloop()