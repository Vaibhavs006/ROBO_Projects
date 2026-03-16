#include <Arduino.h>

#define LPWM_PIN 12
#define RPWM_PIN 13
#define LIMIT_SWITCH_PIN 15
#define CONSTANT_SPEED 200
#define PWM_FREQ 1000
#define PWM_RESOLUTION 8

volatile bool limit_triggered = false;

void limitSwitchISR() {
  limit_triggered = true;
}

void forward() {
  ledcWrite(0, CONSTANT_SPEED);
  ledcWrite(1, 0);
}

void reverse() {
  ledcWrite(0, 0);
  ledcWrite(1, CONSTANT_SPEED);
}

void stop_motor() {
  ledcWrite(0, 0);
  ledcWrite(1, 0);
}

void process_command(String cmd) {
  cmd.trim();

  if (cmd == "FWD") {
    forward();
  }
  else if (cmd == "REV") {
    reverse();
  }
  else if (cmd == "STOP") {
    stop_motor();
  }
  else if (cmd == "STATUS") {
    Serial.print("LIMIT:");
    Serial.println(limit_triggered ? "1" : "0");
  }
  else {
    Serial.println("ERROR:Invalid command");
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(LPWM_PIN, OUTPUT);
  pinMode(RPWM_PIN, OUTPUT);
  pinMode(LIMIT_SWITCH_PIN, INPUT_PULLUP);

  ledcSetup(0, PWM_FREQ, PWM_RESOLUTION);
  ledcSetup(1, PWM_FREQ, PWM_RESOLUTION);
  ledcAttachPin(LPWM_PIN, 0);
  ledcAttachPin(RPWM_PIN, 1);

  attachInterrupt(digitalPinToInterrupt(LIMIT_SWITCH_PIN), limitSwitchISR, FALLING);
}

void loop() {
  if (limit_triggered) {
    stop_motor();
    Serial.println("LIMIT_SWITCH_TRIGGERED");
    limit_triggered = false;
  }

  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    process_command(cmd);
  }
}
