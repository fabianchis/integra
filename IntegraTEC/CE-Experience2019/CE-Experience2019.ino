
//ESTOS SON LOS LEDS
int ledRojo = 10;
int ledAzul = 13;
int ledVerde = 11;
int ledAmarillo = 12;

//ESTOS SON LOS BOTONES
int botonRojo = 8;
int botonAzul = 9;
int botonVerde = 7;
int botonAmarillo = 6;

//ESTOS SON LOS CABLES
int cable1 = 3;
int cable2 = 5;
int cable3 = 2;
int cable4 = 4;



int contCorrectos = 0;


void setup() {
  Serial.begin(9600);
  Serial.setTimeout(50);
  pinMode(ledRojo,OUTPUT);
  pinMode(ledAzul,OUTPUT);
  pinMode(ledVerde,OUTPUT);
  pinMode(ledAmarillo,OUTPUT);

  pinMode(botonRojo,INPUT);
  pinMode(botonAzul,INPUT);
  pinMode(botonVerde,INPUT);
  pinMode(botonAmarillo,INPUT);

  pinMode(cable1,INPUT);
  pinMode(cable2,INPUT);
  pinMode(cable3,INPUT);
  pinMode(cable4,INPUT);



}



void loop() {    
  //ACA SOLO RECIBE UNA DE LAS DOS INSTRUCCIONES "cables" o "simon"
  
  if (Serial.available())
   {
      //String data = Serial.readStringUntil('\n');
      //String data = "cables";
      //clasificar(data);
      
   }


   else{
      String data = "simon";
      clasificar(data);
      
    }
  
}


void clasificar(String accion){
  
  if(accion == "simon"){
    digitalWrite(ledAmarillo,HIGH);
    simonDice();
    }
  if(accion == "cables"){
    funcionCables();
    }  
  else{
     loop();
    }
  }


void funcionCables(){
  if (digitalRead(cable1)==LOW){    
      Serial.println("correcto");
      delay(500);
      loop(); 
           
    }
  if (digitalRead(cable2)==LOW){    
      Serial.println("Incorrecto");
      delay(500);     
    }
  if (digitalRead(cable3)==LOW){    
      Serial.println("Incorrecto");
      delay(500);     
    }
  if (digitalRead(cable4)==LOW){    
      Serial.println("Incorrecto");
      delay(500);     
    }
  else{   
    funcionCables(); 
           
    }
  }


void simonDice(){
  
  if (digitalRead(ledRojo)==HIGH && digitalRead(botonAzul) == HIGH){
    contCorrectos++;
    digitalWrite(ledAmarillo,HIGH);
    digitalWrite(ledVerde,LOW);
    digitalWrite(ledAzul,LOW);
    digitalWrite(ledRojo,LOW);
    simonDice();
    }
  if (digitalRead(ledAmarillo)==HIGH && digitalRead(botonVerde)==HIGH){
    contCorrectos++;
    digitalWrite(ledAzul,HIGH);
    digitalWrite(ledVerde,LOW);
    digitalWrite(ledAmarillo,LOW);
    digitalWrite(ledRojo,LOW);
    simonDice();
    }
  if(digitalRead(ledVerde)==HIGH && digitalRead(botonAmarillo)==HIGH){
    contCorrectos++;
    digitalWrite(ledRojo,HIGH);
    digitalWrite(ledAmarillo,LOW);
    digitalWrite(ledAzul,LOW);
    digitalWrite(ledVerde,LOW);
    simonDice();
    }
  if(digitalRead(ledAzul)==HIGH && digitalRead(botonRojo)==HIGH){
    contCorrectos++;
    digitalWrite(ledVerde,HIGH);
    digitalWrite(ledRojo,LOW);
    digitalWrite(ledAzul,LOW);
    digitalWrite(ledAmarillo,LOW);
    simonDice();
      }
   if (contCorrectos == 5){
      Serial.println("correcto");
      contCorrectos=0;
      digitalWrite(ledVerde,LOW);
      digitalWrite(ledRojo,LOW);
      digitalWrite(ledAzul,LOW);
      digitalWrite(ledAmarillo,LOW);
      loop();
      }
   else{
        simonDice();     
        }
      
  }
