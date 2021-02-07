from gtts import gTTS 
import os 
mytext = 'Telemetry or cyber spying? Just for a minute imagine yourself  being a developer who’s rolled out a device or application. Of course, now you want to learn what functions users will be using and how often, what issues and errors they will encounter. Such information will allow you to enhance your solution and drive up sales. To accomplish that task, you have several choices. You can survey your users and collect their answers. In this event a user provides only the data he wants to share. We use this method collecting information about Panic Button. You can take a look at our survey at https://panicbutton.pw/survey/. However, this method has obvious disadvantages: first, users share their information reluctantly, second, they are often unable to objectively assess the information about the functionality they use. Third, many errors are unseen and unclear to users, and they can be discovered only using software.'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("output.mp3") 
os.system("mpg321 output.mp3") 
