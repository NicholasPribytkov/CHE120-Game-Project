# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:16:03 2024

@author: liamg
"""

from time import sleep
import threading
import PySimpleGUI as sg


def test():
    count = 10
    while count >= 0:
        window.write_event_value('Update', f'{count:0>2d}')
        sleep(1)
        count -= 1
    window.write_event_value('End', None)

layout = [[sg.Button('Start'), sg.Text('  ', size=(2, 1), key='Timing')]]
window = sg.Window('Assistant updater', layout)
start = window['Start']
timing = window['Timing']

while True:

    event, values = window.read(timeout=10)
    if event == 'Cancel'  or event is None:
        break
    elif event == 'Start':
        start.update(disabled=True)
        threading.Thread(target=test, daemon=True).start()
    elif event == 'End':
        start.update(disabled=False)
        timing.update(value='  ')
    elif event == 'Update':
        timing.update(value=values['Update'])

window.close()