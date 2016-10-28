void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if(Serial.available() > 0) {
    String value = Serial.readStringUntil('\n');
    Serial.println(" Bonjourno Simon ");
  }
}
