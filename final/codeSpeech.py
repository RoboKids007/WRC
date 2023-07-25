import speech_recognition as sr
import serial
import time
arduino = serial.Serial(port='/dev/ttyACM2', baudrate=9600, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
    
    

def startSerialCmd():
    print("in StartSerialCmd")
    while True:
        num = 'f' # Taking input from user
        value = write_read(num)
        s1 = value.decode("utf-8") 
       	print(value)
        #print(s1)
        if "arduino" in s1:
            print(s1) # printing the value
            break


def IdentifySpeech():
	with mic as source:
		try:
			r.adjust_for_ambient_noise(source);
			print("ok go on");
			audio = r.listen(source)
			print("ok got audio");

			speech=r.recognize_google(audio)
			#print(r.recognize_google(audio)+"sdsdfsdf")
		
			#print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
			print(speech+"value")
			if speech == "forward":
				print("f")
				while True:
					num = 'f' # Taking input from user
					#value = write_read(num)
					startSerialCmd()

			else:
				print("unkown")
		except Exception as e:
			print("Could not understand audio")

r = sr.Recognizer()
mic = sr.Microphone()
while True:
	IdentifySpeech()
