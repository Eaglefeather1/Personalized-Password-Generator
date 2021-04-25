import kivy
import string
import random
import csv
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.config import Config

class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class MainApp(App):
    password = StringProperty()
    fullTxtValue = StringProperty()
    def passwordCreate(self, user, serviceName, wordOne, wordTwo, number):
        nonAlphabet = string.digits + string.punctuation
        borders = random.choice(nonAlphabet)
        spaces = random.choice (string.punctuation)
        wordOneUpper = random.choice([True, False])
        wordTwoUpper = random.choice([True, False])

        if wordOneUpper:
            wordOne = wordOne.upper()
        else:
            wordOne = wordOne.lower()
            
        if wordTwoUpper:
            wordTwo = wordTwo.upper()
        else:
            wordTwo = wordTwo.lower()

        self.password = (borders + spaces + wordOne + spaces + wordTwo + spaces + number + spaces + borders)
        print (self.password)
    
        csvValue = (serviceName + "," + user + "," + self.password + "\n")
        txtValue = (serviceName + ": \n" + "Username: " + user + "          Password: " + self.password + "\n\n")

        with open('passwords.csv','a') as fd:
            fd.write(csvValue)
        with open('passwords.txt','a') as fd:
            fd.write(txtValue)

    with open('passwords.txt', 'r') as file:
        fullTxtValue = file.read()

    def build(self):
        self.title = "Personalized Password Generator"
        self.icon = "icon.png"
        return WindowManager()
        

if __name__ == "__main__":
    MainApp().run()