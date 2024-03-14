import pyttsx3
input_text = input("Enter the text you want to convert to speech: ")
engine = pyttsx3.init()
engine.setProperty('rate', 150)  
engine.setProperty('volume', 0.9)  
engine.say(input_text)
engine.runAndWait()
