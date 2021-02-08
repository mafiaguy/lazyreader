import PyPDF2 
import pyttsx3 
from gtts import gTTS 
import os 
#book = open('/home/mafiaguy/testingpdftext2speach/file.pdf', 'rb')
#pdfReader = PyPDF2.PdfFileReader(book)
#paged = pdfReader.numPages
#print(paged)
#language = 'en'
#myobj = gTTS(text=book, lang=language, slow=False) 
#myobj.save("output.mp3") 
#os.system("mpg321 output.mp3") 

 class Reading:
     book = open('/home/file.pdf', 'rb')
     pdfReader = PyPDF2.PdfFileReader(book)
     paged = pdfReader.numPages
     print(paged)
     speak = pyttsx3.getPage(20)
     text = from_page.extractText() 
     speak = pyttsx3.init() 
     speak.say(text) 
     speak.runAndWait()
