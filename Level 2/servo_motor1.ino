// C++ code
//https://www.tinkercad.com/things/3R80aYqtg1p-servo-motor?sharecode=t80PSd2s-uqAS-Sd6-jinmVwV4xdZ3xofr_esWhZcUw

#include <Servo.h>
Servo myServo;
// Initialising potentiometer pin as poPin and led pin as ledPin
const int poPin = A0;
const int ledPin = 13;
void setup()
{
  // Attaching the servo motor to pin 9
  myServo.attach(9);
  // Setting the led pin as output and starting the serial communication
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  // Reading the potentiometer value 
  int poValue = analogRead(poPin);
  //Mapping potentiometer value to the servo motor angle
  int angle = map(poValue,0,1023,0,180);
  //Adding the restraint to the servo motor angle and controlling the led
  if (angle >68){
    myServo.write(68);
    digitalWrite(ledPin, HIGH);
  }
  // If the angle is less than or equal to 68, the servo motor will move to the corresponding angle and the led will be turned off
  else{
    myServo.write(angle);
    digitalWrite(ledPin, LOW);
  }
  // Printing the potentiometer angle and the servo motor angle to the serial monitor
  Serial.print("Potentiometer angle:");
  Serial.print(angle);
  Serial.print("| Servo motor angle");
  Serial.print(angle>68? 68:angle);
  delay(20);
 
}