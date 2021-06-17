// C++ code
//
int buzzer = 3; // Buzzerı d3 pinine ve gnd ye bağlamamız gerekiyor.
int rasgelesayi;
int minHz = 300;
int maxHz = 1200;
void setup()
{
  Serial.begin(9600);
  pinMode(3,OUTPUT);
  randomSeed(analogRead(A0)); // A0 pinine birşey bağlamayın randomSeed üretmesi için 0-1024 arası değer geliyor
  
  
}

void loop()
{
  rasgelesayi = random(minHz,maxHz);// Cihaza zarar vermemesi için 200 Hz ile 2000 Hz arasında ses önerilir. İnsan kulağı 20 ile 20k hz aralığını duyabilir.
  Serial.println(rasgelesayi);
  tone(3,rasgelesayi);// D3 Pinine ve GND ye buzzer bağlarsanız ses üretecektir
  delay(1000);
  noTone(3);
  delay(500);
 
}
