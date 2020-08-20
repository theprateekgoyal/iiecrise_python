import pyttsx3
import os

print("Hello I am Toothless. Please first type your name and then hit enter")
pyttsx3.speak("Hello I am Toothless. Please first type your name and then hit enter")
print("Type your name:" , end=' ')
q=input()
print("Hello  " + q +" type which application you want to open, run or execute")
print("Or simply type quit, stop, exit or close to end")
pyttsx3.speak("Hello  " + q + "  type which application you want to open, run or execute")
pyttsx3.speak("Or simply type quit, stop, exit or close to end")
print("Applications you can open")
print("-> Notepad or text editor")
print("-> Windows media player")
print("-> Pot Player")
print("-> Google chrome browser")
print("-> Mozilla firefox browser")
print("-> Dev C++")
print("-> Turbo C++")
print("-> Microsoft Word")
print("-> Microsoft Powerpoint")
print("-> MS Paint")
print("-> Open Office")
while True:
	print("Type your application you want to open: ", end=' ')
	p=input()
	if("run" in p) or ("open"in p) or ("execute" in p):
			if("notepad"in p) or (("editor"in p) and ("text" in p)):
				pyttsx3.speak("Opening notepad")
				print("Opening notepad") 
				os.system("notepad")
			elif(("windows" in p) or ("media" in p)) and ("player" in p):
				pyttsx3.speak("Opening Windows media player")
				print("Opening windows media player") 
				os.system("wmplayer")
			elif("pot" in p) and ("player" in p):
				pyttsx3.speak("Opening Pot Player")
				print("Opening Pot player") 
				os.system("PotPlayerMini64")
			elif("chrome"in p) or (("google" in p) and ("chrome" in p))  or (("browser" in p) and ("chrome" in p)):
				pyttsx3.speak("Opening Google Chrome")
				print("Opening Google chrome") 
				os.system("chrome")
			elif("mozilla"in p) or ("firefox" in p) or ("browser" in p):
				pyttsx3.speak("Opening Mozilla Firefox")
				print("Opening Mozilla firefox") 
				os.system("firefox")
			elif("dev c++"in p):
				pyttsx3.speak("Opening dev c++ compiler")
				print("Opening Dev c++ compiler") 
				os.system("devcpp")
			elif("turbo c++"in p):
				pyttsx3.speak("Opening turbo c++ compiler")
				print("Opening Turbo c++ compiler") 
				os.system("Turboc8")
			elif("word"in p):
				pyttsx3.speak("Opening Microsoft word")
				print("Opening Microsoft Word") 
				os.system("WINWORD")
			elif("powerpoint"in p) or ("presentation" in p):
				pyttsx3.speak("Opening Microsoft Powerpoint Presentation")
				print("Opening Microsoft Powerpoint Presentation") 
				os.system("POWERPNT")
			elif("paint" in p):
				pyttsx3.speak("Opening MS paint")
				print("Opening MS paint")
				os.system("mspaint")
			elif("open office" in p) or ("office" in p):
				pyttsx3.speak("Opening Apache Open Office")
				print("Opening Apache Open Office")
				os.system("soffice")
			else:
				print("Don't support")
				print("Please try again!")
				pyttsx3.speak("Please try again!")
	elif("close"in p) or ("stop"in p) or ("exit"in p) or ("quit" in p):
		print("Thank You")
		pyttsx3.speak("Thank you")
		exit()
	else:
		pyttsx3.speak("Not got. Please repeat.")