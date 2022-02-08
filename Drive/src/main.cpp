#include <Arduino.h>

int mq3 = 0;
int buzzer = 2;
int redled = 3;
int yellowled = 4;
int greenled = 5;
int reading ;

void lightbuzz(int compteur){
  int i ;
  for (i = 0; i < compteur; i++)
  {
  
  digitalWrite(buzzer,HIGH);
  digitalWrite(redled, HIGH);
  delay(500);
  digitalWrite(buzzer, LOW);
  digitalWrite(redled, LOW);
  delay(500);
  }
}

void flashyellow(int compteur){
  int i ;
  for (i = 0; i < compteur; i++)
  {
  
  digitalWrite(yellowled,HIGH);
  delay(500);
  digitalWrite(yellowled, LOW);
  delay(500);
  }
}


void setup() {
  Serial.begin(9600);
  pinMode(mq3,INPUT);
  pinMode(redled, OUTPUT);
  pinMode(yellowled, OUTPUT);
  pinMode(greenled,OUTPUT);

}

void loop() {
  reading = analogRead(mq3);
  Serial.println(reading);
  if (reading > 500)
  {
    lightbuzz(4);

  }
  else if (150 >reading <400)
  {
    flashyellow(4);

  }
  else
  {
    digitalWrite(greenled, HIGH);
  }
  

  
  

}