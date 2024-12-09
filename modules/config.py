class Config:
    def __init__(self):
        # Drowsiness detection parameters
        self.DROWSINESS_THRESHOLD = 0.7
        self.BLINK_THRESHOLD = 0.3
        self.HEAD_TILT_THRESHOLD = 0.4
        
        # System parameters
        self.SAMPLING_RATE = 1.0  # seconds
        self.ALERT_COOLDOWN = 5.0  # seconds
        
        # Alert settings
        self.ALERT_LEVELS = {
            'LOW': 0.7,
            'MEDIUM': 0.8,
            'HIGH': 0.9
        }