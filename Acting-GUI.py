import PySimpleGUI as sg
import threading
import time

# Function to handle countdown in a separate thread
def start_countdown(timer_label, button_key, countdown_time):
    window[button_key].update(disabled=True)
    for i in range(countdown_time, 0, -1):
        window[timer_label].update(f"Countdown: {i} seconds")
        time.sleep(1)  # Sleep for 1 second
    window[timer_label].update("")
    window[button_key].update(disabled=False)

# Set up the layout with two buttons and two text elements for each countdown
layout1 = [
    [sg.Button("Start Timer 1", key="Start1"), sg.Text("", key="Countdown1")],
    [sg.Button("Start Timer 2", key="Start2"), sg.Text("", key="Countdown2")],
    ]

layout2 = [
    [sg.Button("Seccond Timer 1", key="2Start1" ), sg.Text("", key="2Countdown1")],
  
]
layout = [[sg.Column(layout1, visible = True, key= '-COL1-'), sg.Column(layout2, visible = False, key= '-COL2-')],
[sg.Button("Layout 1")],[sg.Button("Layout 2")]
]


window = sg.Window("Independent Countdown Timers", layout)
current_layout = 1
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # Start Timer 1 countdown in a new thread
    if event == "Start1":
        threading.Thread(target=start_countdown, args=("Countdown1", "Start1", 5), daemon=True).start()
    
    if event == "Layout 1":
        if current_layout != 1:
            window[f'-COL{current_layout}-'].update(visible=False)
            current_layout = 1
            window[f'-COL{current_layout}-'].update(visible=True)

    if event == "Layout 2":
        if current_layout != 2:
            window[f'-COL{current_layout}-'].update(visible=False)
            current_layout = 2
            window[f'-COL{current_layout}-'].update(visible=True)
    # Start Timer 2 countdown in a new thread
    if event == "Start2":
        threading.Thread(target=start_countdown, args=("Countdown2", "Start2", 5), daemon=True).start()

    if event == "2Start1":
        threading.Thread(target=start_countdown, args= ("2Countdown1", "2Start1", 3), daemon=True).start()
window.close()
