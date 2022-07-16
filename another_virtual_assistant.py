import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

# Speak Function
def speak(audio):
	engine = pyttsx3.init()
	voices = engine.getProperty("voices")
	engine.setProperty("voice", voices[0].id)
	engine.say(audio)
	engine.runAndWait()

def Hello():
	speak(""" Hello sir I am your desktop assistant.
		Tell me how may I help you""")

# Recognize Voice
def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening")
		r.pause_threshold = 0.7
		audio = r.listen(source)
		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language="en")
			print("the command is printed=", Query)
		except Exception as e:
			print(e)
			print("Say that again Sir")
			return "None"
		return Query

# Take query
def Take_query():
	Hello()
	while(True):
		query = takeCommand().lower()
		if "Helllo how are you" in query:
			speak("I am fine")
		elif "open duck" in query:
			speak("Opening DuckDuckgo")
			webbrowser.open("https://duckduckgo.com")
		# This will exit and terminate the program
		elif "bye" in query:
			speak("Okay Bye Sir")
			exit()
		elif "from wikipedia" in query:
			speak("Checking the wikipedia")
			query = query.replace("wikipedia", "")
			result = wikipedia.summary(query, sentences=2)
			speak("According to wikipedia")
			speak(result)
		elif "what is your name" in query:
			speak("I am D. Your Desktop Assistant")

# Start virtual assistant
if __name__ == "__main__":
	# main method for executing
	# The function
	Take_query()