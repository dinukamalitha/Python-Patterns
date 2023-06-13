import turtle as t
import colorsys as clr
import matplotlib.pyplot as plt
import numpy as np

# Set up the turtle graphics window
fig = plt.figure(figsize=(6, 6), facecolor='black')
ax = fig.add_subplot(111, facecolor='black')
ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)
ax.axis('off')

# Set the speed of drawing to maximum
t.speed(0)

# Reduce the number of screen updates for faster rendering
t.tracer(2)  

# Set the width of the turtle's pen
t.width(2)

# Set the background color of the window to black
t.bgcolor("black") 

# Move the turtle to a starting position
t.goto(10,0)

# Draw a series of circles, changing the color based on the hue (i/60), 
# saturation (0.77), and value (0.89) of the HSV color space.
for i in range(36):
    color = clr.hsv_to_rgb(i/60, 0.77, 0.89)
    t.color(color)
    t.circle(180)
    t.right(12)

    # Draw the current turtle position onto the Matplotlib figure
    x, y = t.position()
    ax.scatter(x, y, color=color, s=15)

# Move the turtle to a new starting position
t.goto(80,-152)

# Draw a more complex pattern using nested loops and circles

# Loop 25 times, changing the hue each time
for j in range (25):  
    
    # Within each loop, loop 15 times, changing the saturation each time
    for i in range(15):  
        
        # Set the color based on the hue and saturation
        color = clr.hsv_to_rgb(i/15,j/25,1)
        t.color(color)
        
        # Turn the turtle to the right by 120 degrees
        t.right(120)  
        
        # Draw a circle with a decreasing radius, moving the turtle forward by 100 units
        t.circle(200-j*4,100)
        
        # Turn the turtle to the left by 120 degrees
        t.left(120)
        
        # Draw a circle with a decreasing radius, moving the turtle forward by 100 units
        t.circle(200-j*5,100)
        
        # Turn the turtle to the right by 360 degrees (a full circle)
        t.right(360)
        
        # Draw a circle with a fixed radius and angle, moving the turtle forward by 48 units
        t.circle(90,48)  
        
        # Draw the current turtle position onto the Matplotlib figure
        x, y = t.position()
        ax.scatter(x, y, color=color, s=15)

# Hide the turtle and display the Matplotlib figure
t.hideturtle()
plt.show()
