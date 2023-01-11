import PySimpleGUI as sg
import os

# FONTS
titlef = "Helvetica 50"

stat = ""

layout = [
    [sg.Text("TICKET REGRISTRATION", font=titlef)],
    [sg.Text(' '*30)],
    [sg.Text('Name', size=(15, 1)), sg.InputText(k='-name-', enable_events = True)],
    [sg.Text('Tier', size=(15, 1)), sg.Radio('Base', 'options', default=True), sg.Radio('VIP', 'options')],
    [sg.Submit(), sg.Text(' '*60), sg.Text('', k='-stat-')],
    [sg.Text('\n'*3)],
    [sg.Exit()]

    ]

# Create the window
window = sg.Window("Ticket Registration Software", layout, size=('800','365'), font="Helvetica 20")

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Exit" or event == sg.WIN_CLOSED:
      break
    if event == '-name-':
      window['-stat-'].update('')


    if event == "Submit" and values['-name-'] != "":
      with open('ticketlist.txt', 'r+') as f:
        tickets = f.read()
        f.close()
      name = values['-name-']

      if values[0] == True:
        opt = "Standard"
      if values[0] == False:
        opt = "VIP"

      content = tickets + f'\n{name}: Tier-> {opt} | VALID'
      with open('ticketlist.txt', 'w+') as f:
        tickets = f.write(content)
        f.close()
      window['-name-'].update('')
      window['-stat-'].update('Saved!')


window.close()
