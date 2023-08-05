import PySimpleGUI as sg
from ocr import ocr

layout = [
    [sg.Text("Choose image: "), sg.In(enable_events=True, key='path'), sg.FilesBrowse()],
    [sg.Button("Extract Text")],
    [sg.Multiline(size=(400, 200), key='result')]
]

window = sg.Window("EDITABLE TEXT", layout, size=(550, 350), element_justification='c')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == "Extract Text":
        print(values["path"])
        window["result"](ocr(values["path"]))

window.close()
