
int x;
void setup() {
 Serial.begin(9600);
 Serial.setTimeout(1);
}
void loop() {
 while (Serial.available());
 x = Serial.readString();
 
}
#include <AFMotor.h>


// Connect motors to M3-M4 output
AF_DCMotor motor1(3);
AF_DCMotor motor2(4);

void setup() {
  motor1.setSpeed(255);  // Set the speed to maximum (0-255)
  motor2.setSpeed(255);  // Set the speed to maximum (0-255)
}

void loop() {
  if x == forward.lower():
  motor1.run(FORWARD);   // Turn motor1 in one direction
  motor2.run(BACKWARD); 
  // Turn motor2 in the same direction
  /*delay(5000); // Run for 5 seconds
  
  motor1.run(RELEASE); // Stop motor1
  motor2.run(RELEASE); // Stop motor2*/
}
