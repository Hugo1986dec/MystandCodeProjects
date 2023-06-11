"""
File: bouncing_ball.py
Name: 劉映麟
-------------------------
TODO: Simulate a bouncing ball animation in a graphics window.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3  # Horizontal velocity
DELAY = 10  # Delay between animation frames
GRAVITY = 1  # Acceleration due to gravity
SIZE = 20  # Size of the ball
REDUCE = 0.9  # Coefficient of restitution (bounce factor)
START_X = 30  # Initial x-coordinate of the ball
START_Y = 40  # Initial y-coordinate of the ball

window = GWindow(800, 500, title='bouncing_ball.py')  # Create a graphics window
ball = GOval(SIZE, SIZE)  # Create a ball object
ball.filled = True
ball.fill_color = "black"
window.add(ball, START_X, START_Y)  # Add the ball to the window at the initial position
start_point = (START_X, START_Y)  # Store the initial position of the ball

vy = 0  # Vertical velocity
num_bounces = 0  # Number of times the ball has bounced to the ground
over_side = 0  # Number of times the ball has gone over the right side of the window


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # Register a mouse click event listener that calls start_falling() function
    onmouseclicked(start_falling)

    while True:
        global vy, num_bounces, over_side
        if vy != 0 or num_bounces > 0:
            ball.move(VX, vy)  # Move the ball horizontally with a constant velocity
            vy += GRAVITY  # Update the vertical velocity with gravity
            if ball.y + vy + ball.height >= window.height:
                num_bounces += 1
                vy = -vy * REDUCE  # Reverse the vertical velocity with a bounce factor
                ball.y = window.height - vy - ball.height  # Adjust the ball's y-coordinate to prevent it from going below the ground
            if ball.x + VX + ball.width >= window.width:
                over_side += 1
                num_bounces = 0  # Reset the number of bounces
                ball.x = start_point[0]  # Reset the ball's x-coordinate to the initial position
                ball.y = start_point[1]  # Reset the ball's y-coordinate to the initial position
                vy = 0  # Reset the vertical velocity
                onmouseclicked(start_falling)  # Register the mouse click event listener again
                if over_side == 3:  # If the ball has gone over the right side 3 times
                    break  # Exit the loop to stop the animation
        pause(DELAY)  # Pause the animation for the specified delay


def start_falling(event):
    """
    This function is called when the user clicks the mouse to start the animation.
    It sets the initial vertical velocity to a positive value.
    """
    global vy
    vy = 1


if __name__ == "__main__":
    main()
