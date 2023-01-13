#include <ros.h>
#include <util/atomic.h>

//Motor pin setup
//Front right
#define M1PIN1 23
#define M1PIN2 25
#define ENC1A 46
#define ENC1B 47
#define PWM1 2
//Front left
#define M2PIN1 27
#define M2PIN2 29
#define ENC2A 48
#define ENC2B 49
#define PWM2 3
//Rear right
#define M3PIN1 31
#define M3PIN2 33
#define ENC3A 50
#define ENC3B 51
#define PWM3 4
//Rear left
#define M4PIN1 35
#define M4PIN2 37
#define ENC4A 52
#define ENC4B 53
#define PWM4 5

volatile int pos_i = 0;
volatile float vel_i = 0;
volatile long prevT_i = 0;

long prevT = 0;
int prevpos = 0;

float v1filt = 0;
float v1prev = 0;
float v2filt = 0;
float v2prev = 0;

float eintegral = 0;


void setup() {
  Serial.begin(115200);

  pinMode(M1PIN1, OUTPUT);
  pinMode(M1PIN2, OUTPUT);
  pinMode(ENC1A, INPUT);
  pinMode(ENC1B, INPUT);
  pinMode(PWM1, OUTPUT);

  pinMode(M2PIN1, OUTPUT);
  pinMode(M2PIN2, OUTPUT);
  pinMode(ENC2A, INPUT);
  pinMode(ENC2B, INPUT);
  pinMode(PWM2, OUTPUT);

  pinMode(M3PIN1, OUTPUT);
  pinMode(M3PIN2, OUTPUT);
  pinMode(ENC3A, INPUT);
  pinMode(ENC3B, INPUT);
  pinMode(PWM3, OUTPUT);

  pinMode(M4PIN1, OUTPUT);
  pinMode(M4PIN2, OUTPUT);
  pinMode(ENC4A, INPUT);
  pinMode(ENC4B, INPUT);
  pinMode(PWM4, OUTPUT);

  attachInterrupt(digitalPinToInterrupt(ENC1A),readEncoder,RISING);
  attachInterrupt(digitalPinToInterrupt(ENC2A),readEncoder,RISING);
  attachInterrupt(digitalPinToInterrupt(ENC3A),readEncoder,RISING);
  attachInterrupt(digitalPinToInterrupt(ENC4A),readEncoder,RISING);
}

void loop() {
  int pos = 0;
  float velocity2 = 0;
  ATOMIC_BLOCK(ATOMIC_RESTORESTATE) {
    pos = pos_i;
    velocity2 = vel_i;
  }

  setMotor(-1, 255, PWM1, M1PIN1, M1PIN2);
  setMotor(-1, 255, PWM2, M2PIN1, M2PIN2);
  setMotor(-1, 255, PWM3, M3PIN1, M3PIN2);
  setMotor(-1, 255, PWM4, M4PIN1, M4PIN2);
  delay(2500);
  setMotor(1, 255, PWM1, M1PIN1, M1PIN2);
  setMotor(1, 255, PWM2, M2PIN1, M2PIN2);
  setMotor(1, 255, PWM3, M3PIN1, M3PIN2);
  setMotor(1, 255, PWM4, M4PIN1, M4PIN2);
  delay(2500);
  setMotor(1, 255, PWM1, M1PIN1, M1PIN2);
  setMotor(-1, 255, PWM2, M2PIN1, M2PIN2);
  setMotor(1, 255, PWM3, M3PIN1, M3PIN2);
  setMotor(-1, 255, PWM4, M4PIN1, M4PIN2);
  delay(2500);

}

void setMotor(int dir, int pwmVal, int pwm, int in1, int in2){
  analogWrite(pwm, pwmVal);
  if(dir == 1){
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
  }
  else if(dir == -1){
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
  }
  else{
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
  }
}

void readEncoder(int enc){
  int b;
  switch (enc){
    case 1:
      b = digitalRead(ENC1B); //check status of ENCB when interrupt is triggered
      break;
    case 2:
      b = digitalRead(ENC2B);
      break;
    case 3:
      b = digitalRead(ENC3B);
      break;
    case 4:
      b = digitalRead(ENC4B);
      break;
  }
    

  int dir = 0;
  if(b > 0){ //increase position
    dir = 1;
  }
  else{
    dir = -1; //decrease position
  }
  pos_i = pos_i + dir;
/*
  long currT = micros();
  float deltaT = ((float) (currT - prevT_i)) / 1.0e6;
  vel_i = dir/deltaT;
  prevT_i = currT;
*/
}