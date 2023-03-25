#include <cvzone.h>

SerialData serialData(2, 1); //(numOfValsRec,digitsPerValRec)
int valsRec[2]; // array of int with size numOfValsRec 

void setup() { 
  pinMode(8, OUTPUT); //pin for LED indicating that a face has been detected (green LED)
  pinMode(13, OUTPUT); // pin for LED indicating that a face has been detected (red LED)
  serialData.begin();
}

void loop() {

  serialData.Get(valsRec);
  digitalWrite(8, valsRec[0]);
  digitalWrite(13, valsRec[1]);
  delay(1000);
}
