import pyrebase
import datetime
import time as tt
import RPi.GPIO as GPIO
config={ 'apiKey': "AIzaSyCNHAr9HExx40a3nSivhE09_1tP2W7i9J8",
    'authDomain': "autowiper-49401.firebaseapp.com",
    'databaseURL': "https://autowiper-49401.firebaseio.com",
    'projectId': "autowiper-49401",
    'storageBucket': "autowiper-49401.appspot.com",
    'messagingSenderId': "931139541498"

}
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
firebase = pyrebase.initialize_app(config)
db=firebase.database()
while True:
	time=str(datetime.datetime.now().time())
	colonCount=0
	for i in range(len(time)):
		if colonCount>0:
			real=(time[i:i+2])
			print(real)
			db.child("Car 1  ").child('Time').set(str(real))
			if int(real) %2==0:
				db.child("Car 1  ").child('Light').set('ON')
				GPIO.output(7,GPIO.HIGH)
			else:
				db.child("Car 1  ").child('Light').set('OFF')
				GPIO.output(7,GPIO.LOW)
			break
		elif time[i]==':':
			colonCount=colonCount+1
	tt.sleep(60)
