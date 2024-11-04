# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:01:14 2024

@author: liamg
"""

import PySimpleGUI as sg
import Timers
time_left="0"
layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("Start")], [sg.Button("exit")],
           [sg.Text(text="timer")]]

# Create the window
window = sg.Window("Demo", layout)
# Create an event loop
temp = True
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "exit":
        window.close()
    if event == "Start":
        
        window['Start'].update(button_color=('white')) 
        window['Start'].update(disabled=True)
        Timers.countdown(5)
        window['Start'].update(button_color=('black')) 
        window['Start'].update(disabled=False)
        
        
    if event == sg.WIN_CLOSED:
        break
window.close