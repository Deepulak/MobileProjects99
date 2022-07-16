import speech_recognition as sr
import webbrowser

sr.Micrpphone(device_index=1)
r = sr.Recognizer()
r.energy_threshold = 5000

with sr.Micrpphone as source:
	print("Speak!")
	audio = r.listen(source)
	try:
		text = r.recognize_google(audio)
		print("You said : {}".format(text))
		url = "htpps://duckduckgo.com/search?q="
		search_url = url + text
		webbrowser.open(search_url)
	except:
		print("Can't recognize")
