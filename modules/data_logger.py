import time
from datetime import datetime

class DataLogger:
    def __init__(self):
        self.log_file = f"drowsiness_log_{int(time.time())}.txt"
        self._initialize_log()
    
    def _initialize_log(self):
        """Creates and initializes the log file."""
        with open(self.log_file, 'w') as f:
            f.write("Drowsiness Detection System Log\n")
            f.write(f"Started at: {datetime.now()}\n")
            f.write("-" * 50 + "\n")
    
    def log_drowsiness_level(self, level):
        """Logs the detected drowsiness level."""
        with open(self.log_file, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - Drowsiness Level: {level:.2f}\n")
    
    def log_alert_triggered(self):
        """Logs when an alert is triggered."""
        with open(self.log_file, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - ALERT TRIGGERED!\n")
    
    def close(self):
        """Closes the log file and performs cleanup."""
        with open(self.log_file, 'a') as f:
            f.write("\nSession ended at: {}\n".format(datetime.now()))
            f.write("-" * 50 + "\n")