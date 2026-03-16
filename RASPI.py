#!/usr/bin/env python3

import argparse, sys, time, serial, threading

import RPi.GPIO as GPIO

class BTS7960Controller:
    def __init__(self, port: str = "/dev/ttyUSB0", baudrate: int = 115200, timeout: float = 1.0):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        self.limit_triggered = False
        self.listening = True
        
        time.sleep(2)
        self.ser.flushInput()
        self.ser.flushOutput()
        
        self.reader_thread = threading.Thread(target=self._read_responses, daemon=True)
        self.reader_thread.start()
    
    def _read_responses(self):
        while self.listening:
            try:
                if self.ser.in_waiting > 0:
                    response = self.ser.readline().decode('utf-8').strip()
                    if response:
                        if "LIMIT_SWITCH_TRIGGERED" in response:
                            self.limit_triggered = True
                            print(f"[ALERT] {response}")
            except Exception as e:
                print(f"[ERROR] Read failed: {e}")
            time.sleep(0.05)
    
    def _send_command(self, cmd: str):
        try:
            self.ser.write((cmd + "\n").encode('utf-8'))
            self.ser.flush()
            time.sleep(0.05)
        except Exception as e:
            print(f"[ERROR] Send failed: {e}")
    
    def forward(self):
        self._send_command("FWD")
    
    def reverse(self):
        self._send_command("REV")
    
    def stop(self):
        self._send_command("STOP")
    
    def status(self):
        self._send_command("STATUS")
    
    def cleanup(self):
        self.listening = False
        if self.ser and self.ser.is_open:
            self.stop()
            time.sleep(0.1)
            self.ser.close()

def main():
    p = argparse.ArgumentParser(description="Control Orange planetary gear motor via ESP32+BTS7960")
    p.add_argument("--port", type=str, default="/dev/ttyUSB0", help="Serial port (default: /dev/ttyUSB0)")
    p.add_argument("--baudrate", type=int, default=115200, help="Baud rate (default: 115200)")
    
    p.add_argument("--action", choices=["forward", "reverse", "stop", "status"], default="forward")
    p.add_argument("--duration", type=float, default=2.0, help="Duration in seconds")
    args = p.parse_args()

    try:
        motor = BTS7960Controller(port=args.port, baudrate=args.baudrate)
    except Exception as e:
        print(f"error: failed to connect to ESP32 on {args.port}: {e}", file=sys.stderr)
        return 1

    try:
        if args.action == "forward":
            motor.forward()
        elif args.action == "reverse":
            motor.reverse()
        elif args.action == "status":
            motor.status()
        else:
            motor.stop()
        
        if args.duration > 0:
            time.sleep(args.duration)
            motor.stop()
    except KeyboardInterrupt:
        print("\nStopped by user")
    finally:
        motor.cleanup()

if __name__ == "__main__":
    raise SystemExit(main())