import time 
from Head.Speak import *
from Head.Listen import *
from Training_model.model import mind
from Head.brain import *
from Function.wish import wish
from Function.welcome import welcome
from Data.dlg_data.dlg import *
import random


def zero():
    wish()
    while True:
        text=listen().lower()
        if text in wake_key_word:
            welcome()
        elif text in goodbye_phrases:
            res_random=random.choice(goodbye_responses)
            speak(res_random)
            break
        elif text.startswith(("zero","buddy","ze")):
            text=text.strip()
            text=mind(text)
            speak(text) 
        else:
            pass


zero() 