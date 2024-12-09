import time
from random import random

class DrowsinessDetector:
    def __init__(self, config):
        self.config = config
        self.last_detection_time = time.time()
        self.last_alert_time = 0
        
    def detect_drowsiness(self):
        """
        Simulates drowsiness detection using various parameters.
        In a real IoT system, this would use actual sensor data.
        Returns a drowsiness score between 0 and 1.
        """
        # Simulate various sensor readings
        blink_rate = self._simulate_blink_rate()
        head_position = self._simulate_head_position()
        reaction_time = self._simulate_reaction_time()
        
        # Calculate overall drowsiness score
        drowsiness_score = (
            blink_rate * 0.4 +
            head_position * 0.3 +
            reaction_time * 0.3
        )
        
        return min(1.0, max(0.0, drowsiness_score))
    
    def should_alert(self, drowsiness_level):
        """Determines if an alert should be triggered based on drowsiness level."""
        if drowsiness_level >= self.config.DROWSINESS_THRESHOLD:
            current_time = time.time()
            if current_time - self.last_alert_time >= self.config.ALERT_COOLDOWN:
                self.last_alert_time = current_time
                return True
        return False
    
    def wait_interval(self):
        """
        Maintains consistent sampling rate using busy waiting instead of sleep.
        """
        while (time.time() - self.last_detection_time) < self.config.SAMPLING_RATE:
            pass  # Busy wait
        self.last_detection_time = time.time()
    
    def _simulate_blink_rate(self):
        """Simulates blink rate measurement."""
        return random() * 0.5 + 0.5  # Higher values indicate slower blink rate
    
    def _simulate_head_position(self):
        """Simulates head position measurement."""
        return random() * 0.6 + 0.4  # Higher values indicate more head tilting
    
    def _simulate_reaction_time(self):
        """Simulates reaction time measurement."""
        return random() * 0.7 + 0.3  # Higher values indicate slower reactions
    
    def cleanup(self):
        """Cleanup resources if needed."""
        pass