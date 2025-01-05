from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test


Window.clearcolor = (.87, 0.54, 0.8, 0.3)
btn_color = (0.98, 0.31, 0.8, 1)

age = 7
name = ""
p1, p2, p3 = 0,0,0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False