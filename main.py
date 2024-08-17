import speech_recognition as sr
import webbrowser  
import pyttsx3 
import requests
import pyjokes
from datetime import datetime
import random
import music

r = sr.Recognizer()
engine = pyttsx3.init()
news_api = "8dfafcfc00df410688efe705f148a764"

def speak(word):
    engine.say(word)
    engine.runAndWait()


#Using for Generating funfacts
fun_facts = [
    "Honey never spoils.",
    "A group of flamingos is called a 'flamboyance'.",
    "There are more stars in the universe than grains of sand on all the beaches on Earth.",
    "Octopuses have three hearts.",
    "Octopuses have blue blood.",
    "The shortest war in history lasted only 38 to 45 minutes.",
    "Honey never spoils.",
    "A group of owls is called a parliament.",
    "Sharks have been around longer than trees."
]

def tell_fun_fact():                       
    fact = random.choice(fun_facts)
    print(f"Here's a fun fact: {fact}")
    speak(f"Here's a fun fact: {fact}")


#Using for generating quotes
def motivational_quote():
    quotes = [
        "The only way to do great work is to love what you do",
        "Success is not final, failure is not fatal: It is the courage to continue that counts",
        "Believe you can and you're halfway there",
        "The only way to do great work is to love what you do."
        "Success is not final, failure is not fatal: It is the courage to continue that counts."
        "Believe you can and you're halfway there."
        "Your time is limited, don't waste it living someone else's life."
        "The best way to predict the future is to create it."
]

    quote = random.choice(quotes)
    print(f"Here's a motivational quote: {quote}")
    speak(f"Here's a motivational quote: {quote}")

#Using For generating Anime Recommendedations
anime_recommendations = [
    "Naruto",
    "One Piece",
    "Attack on Titan",
    "My Hero Academia",
    "Demon Slayer",
    "Death Note",
    "Fullmetal Alchemist: Brotherhood",
    "Steins;Gate",
    "Cowboy Bebop",
    "Sword Art Online",
    "Tokyo Ghoul",
    "Hunter x Hunter",
    "Bleach",
    "Black Clover",
    "Mob Psycho 100",
    "Fairy Tail",
    "Code Geass",
    "Hellsing",
    "Parasyte: The Maxim"
]

def recommend_anime():
    anime = random.choice(anime_recommendations)
    print(f"How about watching {anime}?")    
    speak(f"How about watching {anime}?")



def processcommand(c):
    print("Processing command")
    print("--------------------------------")
    if c.lower() == "open google" :
        webbrowser.open("https://www.google.com")
        speak("Google opened")
    elif c.lower() == "open Github" :
        webbrowser.open("https://github.com/")
        speak("Github opened")
    elif c.lower() == "open instagram" :
        webbrowser.open("https://instagram.com/")
        speak("Instagram opened")
    elif c.lower() == "open linkedin" :
        webbrowser.open("https://linkedin.com/")
        speak("Linkedin opened")
    elif c.lower() == "open youtube" :
        webbrowser.open("https://youtube.com/")
        speak("Youtube opened")
    elif c.lower().startswith("play"):
        speak("Playing music...")
        print(c)
        song = c.lower().split(" ")[1]
        link = music.songs[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        
        print("Getting latest news...")
        speak("Getting latest news...")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles:
                # print(article['title'])
                speak(article['title'])
        else:
            speak("Sorry, I couldn't get the news.")

    elif "joke"in c.lower():
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
        
    elif "weather" in c.lower():
        try:
            city = c.lower().split("in")[1].strip() 
            # Use your actual API key
            api_key = "0e4abf016a524f12a79182237241508"  
            base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
            response = requests.get(base_url)
            if response.status_code == 200:
                data = response.json()
                weather = data['current']['condition']['text']
                temp = data['current']['temp_c']
                print(f"The weather in {city} is {weather} with a temperature of {temp} degrees Celsius.")
                speak(f"The weather in {city} is {weather} with a temperature of {temp} degrees Celsius.")
            else:
                speak("Sorry, I couldn't get the weather details.")
        except IndexError:
            speak("Please specify a city to get the weather information.")
        except Exception as e:
            speak("Sorry, something went wrong while fetching the weather details.")


    elif "date" in c.lower():
        today_date = datetime.now().strftime("%Y-%m-%d")
        print(f"Today's date is {today_date}")        
        speak(f"Today's date is {today_date}")

    elif "time" in c.lower():
        now = datetime.now().strftime("%H:%M:%S")
        print(f"The current time is {now}")
        speak(f"The current time is {now}")

    elif "fun fact" in c:
        tell_fun_fact()

    elif "motivation" in c.lower():

        motivational_quote()

    elif "anime" in c.lower():
        recommend_anime()

    elif "exit" in c:
        speak("Goodbye!")
        exit()

if __name__ == "__main__":
        speak("Intializing Lucy....")

        while True:
            r = sr.Recognizer()
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                text = r.recognize_google(audio)
                if(text.lower() =="lucy"):
                    speak("Hello,What Can I do for you?")
                    with  sr.Microphone() as source:
                        print("Lucy Activated...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                    processcommand(command)
            except Exception as e:  
                print("Say something...")
