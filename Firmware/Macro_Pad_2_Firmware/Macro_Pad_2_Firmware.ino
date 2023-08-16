/*

  Macro_Keypad_2.0 Firmware

  Michael Stickels
  
  Last Updated: *#*#*#*#

  GPL-3.0 License

*/

// Import Libraries
#include <Keypad_Matrix.h>
#include <Keyboard.h>
#include <Adafruit_NeoPixel.h>
#include <AceButton.h>


// Deej setup
const int NUM_SLIDERS = 3;
const int analogInputs[NUM_SLIDERS] = {7, 8, 9};
int analogSliderValues[NUM_SLIDERS];


// Keypad setup
const byte ROWS = 3;
const byte COLS = 3;
const char keys[ROWS][COLS] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};
const byte rowPins[ROWS] = {4, 5, 6};
const byte colPins[COLS] = {0, 1, 2};


// Button setup
const int buttonPin = 10;


// RGB setup
#define DATA_PIN      10
#define PIXEL_COUNT   16



//
void setup() { 

  // 10s delay for interrupting setup with programming if needed
  delay(10000);


  // Initiate Deej sliders
  for (int i = 0; i < NUM_SLIDERS; i++) {
    pinMode(analogInputs[i], INPUT);
  }
  Serial.begin(9600);


  // Initiate keypad
  Keypad_Matrix kpd = Keypad_Matrix( makeKeymap (keys), rowPins, colPins, ROWS, COLS );
  kpd.begin ();
  kpd.setKeyDownHandler (keyDown);
//  kpd.setKeyUpHandler   (keyUp);
  Keyboard.begin();


  // Initiate button
  AceButton button(BUTTON_PIN);
  pinMode(BUTTON_PIN, INPUT);
  ButtonConfig* buttonConfig = button.getButtonConfig();
  buttonConfig->setEventHandler(handleEvent);
  buttonConfig->setFeature(ButtonConfig::kFeatureClick);        // enable short and long single click
  buttonConfig->setFeature(ButtonConfig::kFeatureLongPress);


  // Initiate RGB
  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
  strip.begin();
  strip.show();
  
}


//
void loop() {

  // Deej tick
  updateSliderValues();
  sendSliderValues();


  // Keypad tick
  kpd.scan ();


  // Button tick
  button.check();


  // RGB tick

  
  delay(10);
  
}




// Deej helper functions

void updateSliderValues() {
  for (int i = 0; i < NUM_SLIDERS; i++) {
     analogSliderValues[i] = analogRead(analogInputs[i]);
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

// =====================




// Keypad helper functions

// Handler for keyDown event (key pressed down)
void keyDown (const char which)
  {
  switch (which) {

  // Key 1 press
  case '1':
    Keyboard.press(KEY1);
    break;

  // Key 2 press
  case '2':
    Keyboard.press(KEY2);
    break;

  // Key 3 press
  case '3':
    Keyboard.press(KEY3);
    break;

  // Key 4 press
  case '4':
    Keyboard.press(KEY4);
    break;

  // Key 5 press
  case '5':
    Keyboard.press(ALT);
    Keyboard.press(KEY5);
    break;

   case '6':
   // Key 6 press
    Keyboard.press(KEY_LEFT_CTRL);
    Keyboard.press(KEY_LEFT_ALT);
    Keyboard.press(206); // print screen
    break;

  case '7':
  // Key 7 press
    Keyboard.press(KEY_LEFT_ALT);
    Keyboard.press(KEY7);
    break;

  // Key 8 press
  case '8':
    Keyboard.press(KEY8);
    break;
}
  }

// =====================




// Button helper functions

void handleEvent(AceButton* /* button */, uint8_t eventType, uint8_t buttonState) {

  switch (eventType) {
    case AceButton::kEventPressed:      // short press
      // cycle LED brightness/off
      break;
    case AceButton::kEventLongPressed:  // long press
      // change LED mode
      break;
  }
}

// =====================
