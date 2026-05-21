#include <IRremote.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>


const int RECV_PIN = 2;
const int BUZZER_PIN = 8;


IRrecv irrecv(RECV_PIN);
decode_results results;
LiquidCrystal_I2C lcd(0x27, 16, 2); 

unsigned long lastDetectionTime = 0;
unsigned long currentDetectionTime = 0;

void setup() {
  
  Serial.begin(9600);

 
  irrecv.enableIRIn();

 
  lcd.begin();
  lcd.backlight();

  
  pinMode(BUZZER_PIN, OUTPUT);

 
  lcd.setCursor(0, 0);
  lcd.print("IR Receiver Ready");
  delay(2000);
  lcd.clear();
}

void loop() {
  if (irrecv.decode(&results)) {
   
    currentDetectionTime = millis();
    unsigned long delayTime = currentDetectionTime - lastDetectionTime;
   
    digitalWrite(BUZZER_PIN, HIGH);
    delay(100); 
    digitalWrite(BUZZER_PIN, LOW);

   
    lcd.setCursor(0, 0);
    lcd.print("Code: ");
    lcd.print(results.value, HEX); 
    
    lcd.setCursor(0, 1);
    lcd.print("Delay: ");
    lcd.print(delayTime);
    lcd.print(" ms   "); 
    
    Serial.print("Code: ");
    Serial.println(results.value, HEX);
    Serial.print("Delay: ");
    Serial.println(delayTime);

   
    lastDetectionTime = currentDetectionTime;

    
    irrecv.resume();
  }
}
