import requests
import speech_recognition as sr
import pyttsx3

API_KEY = "c5bb17a95707c83d5507a72b953d37bf"

engine = pyttsx3.Engine()
r = sr.Recognizer()

with sr.Microphone() as mic:
	engine.say("What is the name of city?")
	engine.runAndWait()
	print("What is the name of city?")
	city_name = r.recognize_google(r.listen(mic))
	engine.say("What is the country code?")
	engine.runAndWait()
	print("What is the country code?")
	country_code = r.recognize_google(r.listen(mic))
	engine.say("What units, metric or imperial?")
	engine.runAndWait()
	print("What units, metric or imperial?")
	units = r.recognize_google(r.listen(mic))

res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_KEY}&units={units}")

jsonRes = res.json()
print(jsonRes["main"]["temp"])
print(jsonRes["weather"][0]["main"])
