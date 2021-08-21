def Text_To_Speech(text):
        import pyttsx3

        nurse = pyttsx3.init()

        rate = nurse.getProperty("rate")
        nurse.setProperty("rate",150)

        volume = nurse.getProperty('volume')
        nurse.setProperty('volume',1.0)

        voices = nurse.getProperty('voices')
        nurse.setProperty('voice', voices[1].id)

        nurse.say(text)
        nurse.runAndWait()
