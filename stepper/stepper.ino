/***
 * modified from
 * https://github.com/BretStateham/28BYJ-48
 */


#include <AccelStepper.h>
#define HALFSTEP 8
#define FULLSTEP 4

#define blue 8
#define pink 9
#define yellow 10
#define orange 11
#define oneStep 4096
bool clockwise = true;
bool go = true;

 int targetPosition = 2048 * 2;  //2049 steps per rotation when wave or full stepping
//int targetPosition = 4096 * 2;  //4096 steps per rotation when half stepping

int dataIn;
boolean newData = false;


AccelStepper stepper1(FULLSTEP, blue, yellow, pink, orange);
void setup() {
  
  Serial.begin(9600);
  Serial.write("<Arduino is ready>");

  
  //Set the initial speed (read the AccelStepper docs on what "speed" means
  stepper1.setSpeed(500.0);         
  //Tell it how fast to accelerate
  stepper1.setAcceleration(70.0); 
  //Set a maximum speed it should exceed 
  stepper1.setMaxSpeed(500.0);      
  //Tell it to move to the target position
  stepper1.moveTo(targetPosition);   
}

void loop() {
  if(go){

    if(stepper1.distanceToGo() == 0){
    if(clockwise == true){
      clockwise = false;  //Go counterclockwise now
      stepper1.moveTo(0); //Go back to the "home" (original) position
    } else {
      clockwise = true;   //Go clockwise now
      stepper1.moveTo(targetPosition);  //Go to the target position
    }
  }  

  if(stepper1.distanceToGo() != 0)
    stepper1.run();    
  }

  //check for new data
  recvOneChar();

  //use new data if it exists
  if(newData){  
    int data = getNewData();
    
    if(data == 0){
      go = false;
      Serial.write("go = false");
    }
    else if(data == 1){
      go = true;
      Serial.write("go = true");
    }
    else
      Serial.write("test failed");

  }
    
}

void recvOneChar() {
 if (Serial.available() > 0) {
 dataIn = Serial.read();
 newData = true;
 }
}

void showNewData() {
 if (newData == true) {
  Serial.write(dataIn);
  newData = false;
 }
}

int getNewData() {
  
  int dataOut = -1;
 if (newData == true) {
  Serial.write(dataIn);
  dataOut = dataIn;
  newData = false;
 }

 return dataIn;
}



