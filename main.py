import os
import speech_recognition as sr
import win32com.client
import webbrowser
import openai
from config import apikey
import datetime
import random

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr +=f"harry:{query}\njarvis"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    mic(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
def ai(prompt):
    openai.api_key = apikey
    text = f"openai response for promt:{prompt}\n **********\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    """try:
        print(response["choice"][0]["text"])
    except:
        return "error"""""
    text += response["choice"][0]["text"]
    if not os.path.exists("openai"):
        os.mkdir("openai")

    with open(".join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def mic(text):
    os.system((f"mic {text}"))
def tackcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.5
        try:
            audio = r.listen(source,timeout=1)
            query = r.recognize_google(audio, language="en-in".lower())
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred."


while True:
    print("Listening...")
    query = tackcommand()
    s = tackcommand()
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.speak(s)
    sites = [["youtube", "https://youtube.com"], ["Wikipedia", "https://Wikipedia.com"], ["google", "https://google.com"], ["instagram","https://www.instagram.com/"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            p = (f"opening{site[0]} sir")
            webbrowser.open(site[1])
            speaker1 = win32com.client.Dispatch("SAPI.SpVoice")
            speaker1.speak(p)
    if "play music" in query.lower():
        musicPath = "Spotify"
        os.startfile(musicPath)
        p = (f"playing music on spotify sir")
        speaker1 = win32com.client.Dispatch("SAPI.SpVoice")
        speaker1.speak(p)
    elif "the time" in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        p = (f"sir time is {strTime}")
        speaker1 = win32com.client.Dispatch("SAPI.SpVoice")
        speaker1.speak(p)
    elif "ai".lower() in query.lower():
        ai(prompt=query)

    elif "Jarvis Quit".lower() in query.lower():
        exit()

    elif "reset chat".lower() in query.lower():
        chatStr = ""
    else:
        print("Chatting...")
        chat(query)