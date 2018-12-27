int Sense=A0;
int outPin=13;
void setup(){
pinMode(outPin,OUTPUT);
pinMode(Sense,INPUT);
Serial.begin(9600);
}
unsigned int data;
void loop(){
data=analogRead(Sense);
Serial.println(data);
if(data>850)
digitalWrite(outPin,HIGH);
else
digitalWrite(outPin,LOW);
delay(400);
}
