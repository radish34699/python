#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 22:24:18 2018

@author: r
"""

"""
Part B : Movement of a Particle
"""


# Importing relevant library functions.
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib.animation as animation


"""
Question 1 : Plot the trajectory of the particle in the xy-plane over the time interval t=0 to t=2πs.
             On the graph, show the particle’s locations at t=0, π/2and 2π using a marker and a label.
"""

# Defining a function returns x-coordinate for the time t.
def r_x_func(t, T1=1):
    return np.exp(-1*t/T1)

# Defining a function returns y-coordinate for the time t.
def r_y_func(t, T2=1/3):
    return 2*np.cos(t/T2)

# t_range is for plotting when 0 ≤ t < 2π.
t_range = np.arange(0, 2*np.pi, 0.01)

# Plotting the trajectory of the particle.
plt.plot(r_x_func(t_range), r_y_func(t_range))

# Setting the title of the figrue.
plt.title("Trajectory of the Particle")

# The function below shows a marker and a label for the time t.
def mark_location(t):
    plt.plot(r_x_func(t), r_y_func(t), "or")
    plt.text(r_x_func(t), r_y_func(t), t)

# Showing the particle’s locations at t=0, π/2 and 2π.
mark_location(0)
mark_location(np.pi/2)
mark_location(2*np.pi)

# Showing the chart.
plt.show()


"""
#Question 2 (a) : Express the particles acceleration (ax, ay) symbolically, i.e. show the equation. 
"""

# t is a symbol for Sympy.
t = sp.Symbol("t")

# Defining a function returns x-coordinate for the time t.
r_x = sp.exp(-t)

# Defining a function returns y-coordinate for the time t.
r_y = 2*sp.cos(t*3)

# Differentiating the position.
v_x = sp.diff(r_x, t)
v_y = sp.diff(r_y, t)

# Differentiating the velocity.
a_x = sp.diff(r_x, t, 2)
a_y = sp.diff(r_y, t, 2)

# Printing the acceleration.
print("acceleration = (", a_x, "," ,a_y, ")")


"""
Question 2 (b) : Plot the magnitude of the acceleration of the particle against time over the time interval t=0 to t=2πs. 
"""

# a is the magnitude of the acceleration.
a = sp.sqrt(a_x**2 + a_y**2)

# Plotting the magnitude of the acceleratio when 0 ≤ t < 2π.
sp.plot(a, (t, 0, 2*sp.pi), title = "Magnitude of the Acceleration of the Particle")


"""
Question 3 (a) : Find the magnitude velocity of the particle at time t=1s.
"""

# v is the magnitude of the velocity.
v = sp.sqrt(v_x**2 + v_y**2)

# Substituting t = 1 .
print("magnitude velocity at t = 1s :", v.subs([(t, 1)]))


"""
Question 3 (b) : Estimate the time/times when ry=0.
"""

# Solving the equation r_y = 0 .
solutions = sp.solve(r_y)

# Printing the result.
print("time/times when r_y = 0 :", solutions)


"""
Question 4 : Animate the trajectory of the particle and save your work as a .mp4 file. 
"""

# Preparing for plotting.
figure = plt.figure()

# The number of frame will be len(t_range)/frame_inv.
frame_inv = 10
t_range_frame = t_range[::frame_inv]

# The function below is for animation.
def update_fig(i):
    
    # Clearing the plotting.
    plt.cla()
    
    # Adding axis to the figure.
    ax = figure.add_subplot(1, 1, 1)
    
    # Setting the range of axis. (-2.15 ≤ x ≤ 2.15, -0.05 ≤ y ≤ 1.05)
    ax.set_ylim(-2.15, 2.15)
    ax.set_xlim(-0.05, 1.05)
    
    # Setting axis labels.
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    
    # Setting grid.
    ax.grid()
    
    # Setting the title for the chart.
    plt.title("t = %s" % round(t_range_frame[i], 5))
    
    # Plotting the trajectory of the particle.
    plt.plot(r_x_func(t_range[0:i*frame_inv]), r_y_func(t_range[0:i*frame_inv]))
    
    # Plotting the position of the particle.
    plt.plot(r_x_func(t_range_frame[i]), r_y_func(t_range_frame[i]), "or")

# Animating the trajectory.
print("Animating...")
anim = animation.FuncAnimation(figure, update_fig, interval = 50, frames = len(t_range_frame))

# Saving the animation.

# In my computer, I couldn't find ffmpeg with the code below.
#print(animation.writers.list())

# These codes below will probably work, although they didn't work on my computer.
writer = animation.writers["ffmpeg"](fps=15, bitrate=1800)
anim.save("animation.mp3", writer=writer)

# Saving the trajectory as a .html file worked on my computer.
#ani.save("animation.html")