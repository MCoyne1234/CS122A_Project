
#include <Wire.h>
#include <Adafruit_MotorShield.h>

#define left_sense A0 
#define right_sense A1 

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

// Select which 'port' M1, M2, M3 or M4. In this case, M1
Adafruit_DCMotor *myMotor_L = AFMS.getMotor(1);
// Select which 'port' M1, M2, M3 or M4. In this case, M4
Adafruit_DCMotor *myMotor_R = AFMS.getMotor(4);

void setup() {
  // put your setup code here, to run once:

  // Set the speed to start, from 0 (off) to 255 (max speed)
  //myMotor_L->setSpeed(50);
  //myMotor_R->setSpeed(50);

  pinMode(left_sense,INPUT);
  pinMode(right_sense,INPUT);

  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
  
  // set up Serial library at 9600 bps
  Serial.begin(9600); 
  Serial.print("START");
}

void loop() {
  // put your main code here, to run repeatedly:  
  /*
  Serial.print("LEFT ");
  Serial.println(digitalRead(left_sense));
  Serial.print("RIGHT ");
  Serial.println(digitalRead(right_sense));  
  delay(250);
  */ 
  myMotor_L->setSpeed(255);
  myMotor_R->setSpeed(255);
  //myMotor_L->run(RELEASE);
  //myMotor_R->run(RELEASE);
  //delay(100);
  
  //line detected by both
  if(digitalRead(left_sense)==1 && digitalRead(right_sense)==1){
    //stop
    myMotor_L->run(RELEASE);
    myMotor_R->run(RELEASE);
  }
  //line detected by left sensor
  else if(digitalRead(left_sense)==1 && !digitalRead(right_sense)==1){
    //turn left
    myMotor_L->run(BACKWARD);
    myMotor_R->run(FORWARD);

  }
  //line detected by right sensor
  else if(!digitalRead(left_sense)==1 && digitalRead(right_sense)==1){
    //turn right
    myMotor_L->run(FORWARD);
    myMotor_R->run(BACKWARD);

  }
  //line detected by none
  else if(!digitalRead(left_sense)==1 && !digitalRead(right_sense)==1){
    //stop
    myMotor_L->run(FORWARD);
    myMotor_R->run(FORWARD);

  }
}
