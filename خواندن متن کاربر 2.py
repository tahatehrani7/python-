from gtts import gTTS


input_text = input("enter txt: ")


speech = gTTS(text=input_text, lang='en', slow=False)

a = input ("enter name: ")
speech.save(a)