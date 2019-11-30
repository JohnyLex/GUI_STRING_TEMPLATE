import string
import PySimpleGUI as sg
lay = [[sg.Text('Name    '),sg.Input(size=(20,1))],
       [sg.Text('Forname'),sg.Input(size=(20,1))],
       [sg.Text('Age       '),sg.Input(size=(20,1))],
       [sg.Button(button_text='Registration'),sg.Button(button_text='Cancel')]

]
windows =sg.Window('Registration Form ').layout(lay)
buttons , values =windows.read()
if buttons in (None,'Registration'):
    age = int(values[2])
    name = values[0]
    fname = values[1]
if buttons in (None,'Cancel'):
    print('Good By')
    exit()

values ={'Forname':fname,'name':name,'age':age}
t = string.Template("""
Name    : $name
Vorname : $Forname
Age     : $age
""")
print('Client information:',t.substitute(values))
