import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Head.Speak import speak
from Data.dlg_data.dlg import *
import random

def welcome():
    welcome = random.choice(welcomedlg)
    speak(welcome)