"""Alert system for drowsiness detection"""
import time
import cv2
from .utils.constants import WINDOW_NAME, FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS

class AlertSystem:
    def __init__(self):
        self.alert_count = 0
        self.last_alert_time = 0
        
    def trigger_alert(self, drowsiness_level):
        """Trigger an alert when drowsiness is detected"""
        current_time = time.time()
        if current_time - self.last_alert_time >= 3.0:  # Alert cooldown
            self.alert_count += 1
            self.last_alert_time = current_time
            
            # Display alert on frame
            message = f"DROWSINESS ALERT! Level: {drowsiness_level:.2f}"
            print(f"\n[ALERT] {message}")
            return message
        return None