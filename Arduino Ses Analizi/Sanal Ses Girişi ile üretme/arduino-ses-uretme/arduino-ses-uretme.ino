// C++ code
//

int rasgelesayi;
int minHz = 50;
int maxHz = 1500;
void setup()
{
  Serial.begin(9600);
  randomSeed(analogRead(A0));// A0 pinine birşey bağlamayın randomSeed üretmesi için 0-1024 arası değer geliyor
}

void loop()
{
 
  rasgelesayi = random(minHz,maxHz);// Cihaza zarar vermemesi için 200 Hz ile 2000 Hz arasında ses önerilir. İnsan kulağı 20 ile 20k hz aralığını duyabilir.
  Serial.println(rasgelesayi,HEX);
  delay(500);

  
  
}
