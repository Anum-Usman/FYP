import google.generativeai as palm
import speech_recognition as sr
import pyttsx3
import os
recognizer = sr.Recognizer()
engine = pyttsx3.init()
API_KEY = 'AIzaSyDzj8yESjjCS6vWNIFAAnjaKVtjGTNsl8g'
palm.configure(api_key=API_KEY)


# propmpt = '''Write something about Pakistan'''
# prompt = input('''What do you want from me?''')


def recognizeSpeech():
    model_id = "models/text-bison-001"
    while True:
        with sr.Microphone() as source:
            print("Listening....")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio).lower()
                prompt = text
                completion = palm.generate_text(
                    model=model_id,
                    prompt=prompt,
                    temperature=0.99,
                    max_output_tokens=800
                )
                text_to_speak = completion.result
                print(completion.result)
                engine.setProperty('rate', 150)
                engine.say(text_to_speak)
                engine.runAndWait()
            except Exception as e:
                print(e)


if __name__ == '__main__':
    recognizeSpeech()
