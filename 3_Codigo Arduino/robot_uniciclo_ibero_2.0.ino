const int wl_pwm_pin = 9;
const int wl_a_pin = 7;
const int wl_b_pin = 8;

const int wr_pwm_pin = 3;
const int wr_a_pin = 4;
const int wr_b_pin = 2;

const int stby_pin=5;
const int led_pin=6;

bool wrNeg,wlNeg;
int16_t wr=0,wl=0;

#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 14); // TX, RX

void setup()
{
  mySerial.begin(9600); //Iniciamos Software Serial
  Serial.begin(9600);
  pinMode(wr_pwm_pin,OUTPUT);
  pinMode(wr_a_pin,OUTPUT);
  pinMode(wr_b_pin,OUTPUT);
  pinMode(wl_pwm_pin,OUTPUT);
  pinMode(wl_a_pin,OUTPUT);
  pinMode(wl_b_pin,OUTPUT);
  pinMode(stby_pin,OUTPUT);
  pinMode(led_pin,OUTPUT);
  digitalWrite(stby_pin,HIGH);
}

void loop()
{  
  digitalWrite(led_pin,HIGH);
  
    if(mySerial.available()>=5){
      if(mySerial.read()=='H'){
        wr=((int16_t)mySerial.read())|(((int16_t)mySerial.read())<<8);
        wl=((int16_t)mySerial.read())|(((int16_t)mySerial.read())<<8);

        Serial.print("wl= ");
        Serial.println(wl);
        Serial.print("wd= ");
        Serial.println(wr);
  
        if(wr<0){
          wrNeg=true;
        }else{
          wrNeg=false;
        }
        
        wr=abs(wr);
        if(wrNeg){
          digitalWrite(wr_a_pin,HIGH);
          digitalWrite(wr_b_pin,LOW);
        }else{
          digitalWrite(wr_a_pin,LOW);
          digitalWrite(wr_b_pin,HIGH);
        }//else
        analogWrite(wr_pwm_pin,wr);
  
        if(wl<0){
          wlNeg=true;
        }else{
          wlNeg=false;
        }//else
        
        wl=abs(wl);
        if(wlNeg){
          digitalWrite(wl_a_pin,HIGH);
          digitalWrite(wl_b_pin,LOW);
        }else{
          digitalWrite(wl_a_pin,LOW);
          digitalWrite(wl_b_pin,HIGH);
        }//else
        analogWrite(wl_pwm_pin,wl);
  
      }else{
        Serial.read();
      }
    }
    digitalWrite(led_pin,LOW);
}
