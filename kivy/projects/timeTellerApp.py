import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from random import randint, sample

kivy.require('1.11.1')

class TimeTellApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical')

        # Create the input box and submit button
        input_box = TextInput(hint_text='Enter the event you want to predict', multiline=False)
        submit_button = Button(text='Submit', size_hint=(None, None), size=(100, 50))
        submit_button.bind(on_press=self.predict_event)

        # Add the input box and submit button to the layout
        layout.add_widget(input_box)
        layout.add_widget(submit_button)

        # Create the labels for the dials
        dial_labels = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Percent', 'Percent', 'Percent', 'Other']

        # Create the dials using spinners
        dials = []
        for label in dial_labels:
            dial = Spinner(text=label, values=[''] + [str(i) for i in range(80)], size_hint=(None, None), size=(100, 50))
            dial.background_color = (1, 1, 1, 1)
            dials.append(dial)

        # Add the dials to the layout
        dial_layout = BoxLayout(orientation='horizontal')
        for dial in dials:
            dial_layout.add_widget(dial)
        layout.add_widget(dial_layout)

        # Create the label for the predicted time
        self.predicted_time_label = Label(text='')

        # Add the predicted time label to the layout
        layout.add_widget(self.predicted_time_label)

        # Create the label for the possible outcomes
        self.possible_outcomes_label = Label(text='')

        # Add the possible outcomes label to the layout
        layout.add_widget(self.possible_outcomes_label)

        return layout
    
TimeTellApp().run()