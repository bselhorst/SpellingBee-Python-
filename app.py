from gtts import gTTS
def speak(text):
    filename = f"{text}.mp3"
    spelling = ''
    for letter in word:
        spelling += letter+' '
    tts = gTTS(text= spelling, lang="en")
    tts.save(filename)

word = input("word to spelling: ")
speak(word)