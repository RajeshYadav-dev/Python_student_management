import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
    


# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Set voice to female
engine.setProperty('rate', 150)

 
def speak(message):
    """Speak the given message."""
    engine.say(message)
    engine.runAndWait()

def greet_user():
    """Greet the user based on the current time."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good Morning dear sir"
    elif hour < 18:
        greeting = "Good Afternoon dear sir"
    else:
        greeting = "Good Evening dear sir"
    
    speak(greeting)
    speak("I am your Virtual Assistant Sapna, How may I help you ?")

def take_command():
    """Listen for a command from the user and return it as a string."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        try:
            print("Listening...")
            recognizer.pause_threshold = 0.5
            recognizer.energy_threshold = 100  # Adjusted energy threshold
            audio = recognizer.listen(mic)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="hin-in")
            print("User  said:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

def search_wikipedia(query):
    """Search Wikipedia for the given query and speak the results."""
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "").strip()
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia") 
    print(results)
    speak(results)

def open_website(url):
    """Open the specified website in a web browser."""
    webbrowser.open(url)

def play_music(music_dir):
    """Play the first song from the specified music directory."""
    try:
        songs = os.listdir(music_dir)
        if songs:
            song_path = os.path.join(music_dir, songs[0])
            print(f"Playing: {song_path}")
            os.startfile(song_path)
        else:
            speak("No songs found in the music directory.")
    except Exception as e:
        print(f"Error accessing music directory: {str(e)}")

def tell_time():
    """Speak the current time."""
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak(f"Sir, the time is {current_time}")

def main():
    """Main function to run the virtual assistant."""
    greet_user()

    music_dir = "F:\music"  # Replace with your actual music folder path
    
    while True:
        query = take_command()
        if query is None:
            continue  # Skip to the next iteration if no command was recognized
        elif "how are you" in query:
            speak("I am owesome, how about you") 
        elif "what is your name" in query:
            speak("My Name is ayush,what is your name") 
        elif "where do you live" in query:
            speak("I live in Rajesh Yadav home,where do you live") 
        elif "how old are you" in query:
            speak("I am a girl and born today ,How old are you")             
        elif "wikipedia" in query:
            search_wikipedia(query)
        elif "youtube" in query:
            open_website("https://www.youtube.com")
        elif "facebook" in query:
            open_website("https://www.facebook.com")
        elif "play" in query and "song" in query:
            # Extract the song name from the query
            song_name = query.replace("play", "").replace("song", "").strip()
            if song_name:
                speak(f"Playing {song_name} on YouTube")
                webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
            else:
                speak("Please specify the song name.")    
        elif "google" in query:
            search_query = query.replace("google", "").replace("search", "").strip()
            open_website(f"http://google.com/search?q={search_query}")
        elif "music" in query or "song" in query:
            play_music(music_dir)
        elif "time" in query:
            tell_time()
        elif "sleep" in query:
            speak("Thank You Sir")
            break  # Exit the loop

if __name__ == "__main__":
    main()