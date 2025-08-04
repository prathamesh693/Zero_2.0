import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Head.Speak import speak

from datetime import date
import datetime
import random
from Data.dlg_data.dlg import *
from Function.welcome import welcome

today = date.today()
formatted_date = today.strftime("%d %b %y")
nowx = datetime.datetime.now()

def wish():
    current_hour = nowx.hour
    if 5 <= current_hour < 12:
        gd_dlg = random.choice(good_morningdlg)
        speak(gd_dlg)
    elif 12 <= current_hour < 17:
        ga_dlg = random.choice(good_afternoondlg)
        speak(ga_dlg)
    elif 17 <= current_hour < 22:
        ge_dlg = random.choice(good_eveningdlg)
        speak(ge_dlg)
    else:
        gn_dlg = random.choice(good_nightdlg)
        speak(gn_dlg)