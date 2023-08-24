const int NUM_SLIDERS = 3;
const int analogInputs[NUM_SLIDERS] = {9, 8, 7};

int analogSliderValues[NUM_SLIDERS];
float coefficient;

void setup() { 
  for (int i = 0; i < NUM_SLIDERS; i++) {
    pinMode(analogInputs[i], INPUT);
  }

  coefficient = 0.000977517106549;

//  testing on board LED
//  pinMode(13, OUTPUT);
//  digitalWrite(13, LOW);
    
  Serial.begin(9600);
}

void loop() {
  updateSliderValues();
  sendSliderValues(); // Actually send data (all the time)
//  printSliderValues(); // For debug
  delay(10);
}



void valueFunction(int value) {
  return (coefficient * pow(value,2));
}

void updateSliderValues() {
  for (int i = 0; i < NUM_SLIDERS; i++) {
     analogSliderValues[i] = valueFunction(analogRead(analogInputs[i]));
  }
}

void sendSliderValues() {
  String builtString = String("");

  for (int i = 0; i < NUM_SLIDERS; i++) {
    builtString += String((int)analogSliderValues[i]);

    if (i < NUM_SLIDERS - 1) {
      builtString += String("|");
    }
  }
  
  Serial.println(builtString);
}

void printSliderValues() {
  for (int i = 0; i < NUM_SLIDERS; i++) {
    String printedString = String("Slider #") + String(i + 1) + String(": ") + String(analogSliderValues[i]) + String(" mV");
    Serial.write(printedString.c_str());

    if (i < NUM_SLIDERS - 1) {
      Serial.write(" | ");
    } else {
      Serial.write("\n");
    }
  }
}
