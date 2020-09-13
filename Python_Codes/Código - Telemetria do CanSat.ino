//Made by: Vinícius Azevedo
//Instagram: instagram.com/v.mazevedo
//Twitter: twitter.com/vmeazevedo

//CANSAT - CUBESAT

// Pontos de Ligação dos módulos:
// - BMP180 = ( 1=SDA (A4), 2=SCI(A5), 3=GND, 4=VCC )
// - DHT11 = ( 1=VCC, 2=SIGNAL (A1), 3=X, 4=GND)
// - RTC DS1302 = ( 1=VCC, 2=GND , 3=CLK (D6), 4=DATA (D7), 5=RST (D8)

//Bibliotecas
#include <Wire.h>
#include <Adafruit_BMP085.h>
#include <DHT.h>
#include <virtuabotixRTC.h>
#include <SD.h>
File myFile;
 
#define DHTPIN A1 // pino que estamos conectado
#define DHTTYPE DHT11 // DHT 11
int pinCS = 10;

DHT dht(DHTPIN, DHTTYPE);
Adafruit_BMP085 bmp;
virtuabotixRTC myRTC(6, 7, 8);


void setup() {
 
  pinMode(pinCS, OUTPUT);
  
  // SD Card Initialization
  
  if (SD.begin())
  {
    Serial.println("SD card is ready to use.");
  } else
  {
    Serial.println("SD card initialization failed");
    return;
  }
  myFile = SD.open("test.txt", FILE_WRITE);
  if (myFile) {
    myFile.println("Dia,Temperatura,Pressao,Altitude,Pressao ao nivel do mar,Umidade ");
    myFile.close(); // close the file
  }
  
  // Configuração do DS1302 (segundos, minutos, hora, dia da semana, dia do mes, mes, ano)
  myRTC.setDS1302Time(00, 02, 14, 7, 17, 03, 2018);
  

  Serial.begin(9600);
  dht.begin();
  Wire.begin();
  //Wire.beginTransmission(MPU);
  Wire.write(0x6B); 
  Wire.write(0); 
  Wire.endTransmission(true);
  if (!bmp.begin()) {
	Serial.println("Erro no sensor BMP085, checar fiacao!");
	while (1) {}
  }
}
  
void loop() {

  // Le as informacoes do CI
  myRTC.updateTime(); 

  // Imprime as informacoes no serial monitor
  Serial.print("Data : ");
  // Chama a rotina que imprime o dia da semana 
  imprime_dia_da_semana(myRTC.dayofweek);
  Serial.print(", ");
  Serial.print(myRTC.dayofmonth);
  Serial.print("/");
  Serial.print(myRTC.month);
  Serial.print("/");
  Serial.print(myRTC.year);
  Serial.print("  ");
  Serial.print("Hora : ");
  // Adiciona um 0 caso o valor da hora seja <10
  if (myRTC.hours < 10)
  {
  Serial.print("0");
  }
  Serial.print(myRTC.hours);
  Serial.print(":");
  // Adiciona um 0 caso o valor dos minutos seja <10
  if (myRTC.minutes < 10)
  {
  Serial.print("0");
  }
  Serial.print(myRTC.minutes);
  Serial.print(":");
  // Adiciona um 0 caso o valor dos segundos seja <10
  if (myRTC.seconds < 10)
  {
  Serial.print("0");
  }
  Serial.println(myRTC.seconds);

  delay(100);

  //Inicia a rotina do DHT11
   float h = dht.readHumidity();
  Serial.print("Temperatura = ");
  Serial.print(bmp.readTemperature());
  Serial.println(" ºC");

   //Inicia a rotina do BMP180
  Serial.print("Pressao = ");
  Serial.print(bmp.readPressure());
  Serial.println(" Pa");
    
  Serial.print("Altitude = ");
  Serial.print(bmp.readAltitude());
  Serial.println(" metros");

  Serial.print("Pressao/nivel do mar (calc.) = ");
  Serial.print(bmp.readSealevelPressure());
  Serial.println(" Pa");

  Serial.print("Altitude real = ");
  Serial.print(bmp.readAltitude(101500));
  Serial.println(" metros");

  Serial.println();
  Serial.print("Umidade: ");
  Serial.print(h);
  Serial.print(" %   ");
  Serial.println();
  delay(500);
  
  myFile = SD.open("test.txt", FILE_WRITE);
  if (myFile) {    
    grava_dia_da_semana(myRTC.dayofweek);
    myFile.print("_");
    myFile.print(myRTC.dayofmonth);
    myFile.print("/");
    myFile.print(myRTC.month);
    myFile.print("/");
    myFile.print(myRTC.year);
    myFile.print("  ");
    myFile.print("Hora : ");
    // Adiciona um 0 caso o valor da hora seja <10
    if (myRTC.hours < 10)
    {
      myFile.print("0");
    }
    myFile.print(myRTC.hours);
    myFile.print(":");
    // Adiciona um 0 caso o valor dos minutos seja <10
    if (myRTC.minutes < 10)
    {
      myFile.print("0");
    }
    myFile.print(myRTC.minutes);
    myFile.print(":");
    // Adiciona um 0 caso o valor dos segundos seja <10
    if (myRTC.seconds < 10)
    {
      myFile.print("0");
    }
    myFile.print(myRTC.seconds);
    myFile.print(","); 
    myFile.print(bmp.readTemperature());
    myFile.print(",");    
    myFile.print(bmp.readPressure());
    myFile.print(",");   
    myFile.print(bmp.readAltitude());
    myFile.print(",");   
    myFile.print(bmp.readSealevelPressure());
    myFile.print(",");  
    myFile.print(h);
    myFile.println(" ");
    myFile.close(); // close the file
  }
  // if the file didn't open, print an error:
  else {
    Serial.println("error opening test.txt");
  }
  delay(500);
}

//Indicação dos dias da semana para o DS1302
void imprime_dia_da_semana(int dia)
{
  switch (dia)
  {
    case 1:
    Serial.print("Domingo");
    break;
    case 2:
    Serial.print("Segunda");
    break;
    case 3:
    Serial.print("Terca");
    break;
    case 4:
    Serial.print("Quarta");
    break;
    case 5:
    Serial.print("Quinta");
    break;
    case 6:
    Serial.print("Sexta");
    break;
    case 7:
    Serial.print("Sabado");
    break;
  }
}

void grava_dia_da_semana(int dia)
{
  switch (dia)
  {
    case 1:
    myFile.print("Domingo");
    break;
    case 2:
    myFile.print("Segunda");
    break;
    case 3:
    myFile.print("Terca");
    break;
    case 4:
    myFile.print("Quarta");
    break;
    case 5:
    myFile.print("Quinta");
    break;
    case 6:
    myFile.print("Sexta");
    break;
    case 7:
    myFile.print("Sabado");
    break;   
  }
}
