import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import threading
import wikipedia
from Training_model.model import mind
from Head.Speak import speak
import time
import webbrowser

def load_qa_data(file_path):
    qa_dict = {}
    with open (file_path, "r", encoding = "utf-8", errors="replace") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) !=2:
                continue
            q, a = parts
            qa_dict[q] = a
    return qa_dict

qa_file_path = r"C:\Users\ratho\OneDrive\Desktop\ZERO_2.0\Data\Brain_data\qna_data.txt"
qa_dict=load_qa_data(qa_file_path)

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075) # adjust the sleep duration for the animation speed
    print()

def save_qa_data(file_path,qa_dict):
    with open(file_path,"w",encoding="utf-8") as f:
        for q,a in qa_dict.items():
            f.write(f"{q}:{a}\n")

def wiki_search(prompt):
    search_prompt = prompt.replace("Zero", "")
    search_prompt = search_prompt.replace("wikipedia", "")

    try:
        wiki_summary = wikipedia.summary(search_prompt, sentences =1)
        animate_thread = threading.Thread(target=print_animated_message,args=(wiki_summary,))
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))

        animate_thread.start()
        speak_thread.start()

        animate_thread.join()
        speak_thread.join()

        qa_dict[search_prompt] = wiki_summary # Store in qa_dict
        save_qa_data(qa_file_path,qa_dict) # save updated qa_dict
    
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There is a disambiguation page for the given query. Please provide more specific information.")
        print("There is a disambiguation page for the given query. Please provide more specific information.")
    except wikipedia.exceptions.PageError:
        google_search(prompt)

def google_search(query):
    query = query.replace("who is ", "")
    query = query.strip()

    if query:
        url = "https://www.google.com/search?q="+query
        webbrowser.open_new_tab(url)
        speak("You can see search results for "+query+" in google on your screen.")
        # Commenting out the speak function as it's not provided here
        print("You can see search results for "+query+" in google on your screen.")
    else:
        speak("I didn't catch what you said.")
        # Commenting out the speak function as it's not pro vided here
        print("I didn't catch what you said.")

def brain(text):

    try:
        response = mind(text)

        if not response:
            wiki_search(text) # If AI response is empty or not confident, pass to wiki-search
            return
        
        # Start animation and speaking concurrently
        animate_thread = threading.Thread(target=print_animated_message,args=(response,))
        speak_thread = threading.Thread(target=speak,args=(response,))
        
        animate_thread.start()
        speak_thread.start()
        
        animate_thread.join()
        speak_thread.join()

        qa_dict[text] = response # Store in qa_dict
        save_qa_data(qa_file_path,qa_dict) # save updated qa_dict
    
    except Exception as e:
        print(f"An error occured: {str(e)}")
        wiki_search(text) # Pass to wiki_search on error