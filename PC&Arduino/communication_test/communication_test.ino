char line[500] = "";
int ret = 0;

void setup() { 
    Serial.begin(9600);
}

void loop() { 
    if(Serial.available()>0){
        ret = Serial.readBytesUntil('\n',line,500); 
        Serial.print("I receive: ");
        Serial.print(line);
    }
    delay(2000);
    Serial.println("waiting..."); 
}
