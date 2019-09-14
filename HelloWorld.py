# My first PySimpleGUI application 
# Created by morrettidon 9/13/2019


import PySimpleGUI as sg


class Application:
    '''Says hello and goodbye to user.'''
    def __init__(self):
        self.layout = [
                    [sg.Text('Welcome to my first app!',font=('helvetica', 38), text_color='maroon')],
                    [sg.Text('Please type your name: ',font=('arial', 38), text_color='navy'), 
                    sg.InputText(font=('Arial', 22))],
                    [sg.Button('ENTER',font=('serif',22)), sg.Button('QUIT',font=('serif',22))]
                    ]
        self.window = sg.Window("Hello world!", self.layout)
        self.running()

    def running(self):
        while True:      
            self.event, self.values = self.window.Read()
            if self.event == 'QUIT':  
                sg.Popup("Goodbye ",self.values[0],font=('verdana', 52),text_color='lime',background_color='navy')
                break
            else:
                sg.Popup("Hello ",self.values[0],font=('verdana', 52),text_color='lime',background_color='navy')
        self.window.Close()


def main():
    app = Application()


if __name__ == '__main__':
    main()
