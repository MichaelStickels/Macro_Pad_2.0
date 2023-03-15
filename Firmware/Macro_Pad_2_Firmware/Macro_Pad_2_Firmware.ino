/*

  Macro_Keypad_2.0 Firmware

  Michael Stickels
  
  Last Updated: *#*#*#*#

  GPL-3.0 License

*/

// Import Libraries
#include <Keypad_Matrix.h>
#include <Keyboard.h>


// Define keypress for keys 1-8
#define KEY1 KEY_F13
#define KEY2 KEY_F14
#define KEY3 KEY_F15
#define KEY4 KEY_F16
#define KEY5 KEY_F8
#define KEY6 KEY_F18
#define KEY7 KEY_F9
#define KEY8 KEY_F20
#define ALT KEY_LEFT_ALT
// Define keypad size and layout
const byte ROWS = 3;
const byte COLS = 3;
const char keys[ROWS][COLS] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};
// Define keypad pins
const byte rowPins[ROWS] = {10, 16};
const byte colPins[COLS] = {14, 15, 18, 19};

// Initialize keypad object
Keypad_Matrix kpd = Keypad_Matrix(makeKeymap (keys), rowPins, colPins, ROWS, COLS);


/*

  To set custom macros, edit the case for the desired button in *BOTH* keyDown and keyUp.
  Ensure that each Keyboard.press() is accompanied by a Keyboard.release() statement, or
  the key will get "stuck down". Any reasonable combination of keys can be set, including
  modifiers and multiple keypresses.

  See https://www.arduino.cc/en/Reference/KeyboardModifiers for modifier keys 

*/


// Deej setup
const int NUM_SLIDERS = 3;
const int analogInputs[NUM_SLIDERS] = {7, 8, 9};
int analogSliderValues[NUM_SLIDERS];

// Keypad setup


void setup() { 

  // Small delay for interrupting setup via programming if needed
  delay(8000);

  // Initiate keypad
  kpd.begin ();
  kpd.setKeyDownHandler (keyDown);
  kpd.setKeyUpHandler   (keyUp);
  Keyboard.begin();
  
  for (int i = 0; i < NUM_SLIDERS; i++) {
    pinMode(analogInputs[i], INPUT);
  }

  Serial.begin(9600);
  
}

void loop() {
  
  updateSliderValues();
  sendSliderValues(); // Actually send data (all the time)
  // printSliderValues(); // For debug

  kpd.scan ();
  
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

// Handler for keyUp event (key unpressed)
void keyUp (const char which)
  {
  switch (which) {

  // Key 1 release
  case '1':
    Keyboard.release(KEY1);
    break;

  // Key 2 release
  case '2':
    Keyboard.release(KEY6);
    break;

  // Key 3 release
  case '3':
    Keyboard.release(KEY3);
    break;

  // Key 4 release
  case '4':
    Keyboard.release(KEY4);
    break;

  // Key 5 release
  case '5':
    Keyboard.release(ALT);
    Keyboard.release(KEY5);
    break;

  // Key 6 release
  case '6':
    Keyboard.release(KEY_LEFT_CTRL);
    Keyboard.release(KEY_LEFT_ALT);
    Keyboard.release(206);
    break;

  // Key 7 release
  case '7':
    Keyboard.release(KEY_LEFT_ALT);
    Keyboard.release(KEY7);
    break;
    
  // Key 8 release
  case '8':
    Keyboard.release(KEY8);
    break;
  }
}

// =====================
