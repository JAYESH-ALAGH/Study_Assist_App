def speech_to_text():
    from subprocess import call
    import speech_recognition as sr
    import os, time

    r= sr.Recognizer()
    text = {}
    text1 = {}
    def listen1():
        with sr.Microphone(device_index = 2) as source:
                   r.adjust_for_ambient_noise(source)
                   #print("Say Something");
                   audio = r.listen(source)
                   #print("got it");
        return audio
    def voice(audio1):
           try:
             text1 = r.recognize_google(audio1)
    ##         call('espeak '+text, shell=True)
             #print ("you said: " + text1);
             return text1;
           except sr.UnknownValueError:


              return "Sorry! Could not understand\nPlease try again"
           except sr.RequestError as e:

              return "Please check your Internet connection"

    audio1 = listen1()
    text = voice(audio1)
    return text
    text = {}



'''
    if __name__ == '__main__':
     while True:
         audio1 = listen1()
         text = voice(audio1)
         return

         if text == 'hello':
             text = {}
             print("hi")
         else:
             print("could not detect")'''
