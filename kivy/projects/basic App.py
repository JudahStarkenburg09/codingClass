from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class gridLayout(GridLayout):

    def __init__(self, **kwargs):

        super(gridLayout, self).__init__(**kwargs)

        self.cols = 1 #set the amount of columns

        self.textLabel1 = Label(text = "This is a text label, And below is a text input", font_size = 20) #create a text label
        self.add_widget(self.textLabel1) #self.add the text label

        self.inputBox1 = TextInput(multiline = False, font_size = 20) #create a input box
        # self.inputBox1.foreground_color((100, 0, 0))
        self.add_widget(self.inputBox1) #add the input box
        
        self.button1 = Button(text="This is a button!", font_size = 20) #create a button
        self.button1.bind(on_press = self.button1Pressed) #bind the button to on press
        self.add_widget(self.button1) #add the button
    
    def button1Pressed(self, instance):
        print("Button was pressed!")
        inputBoxHad = self.inputBox1.text
        print("Inside the text input box, was: " + inputBoxHad)

class window(App):
    
    def build(self):
        return gridLayout()

window().run()