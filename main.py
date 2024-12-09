#!/usr/bin/env python3
"""Main module for drowsiness detection system"""

import cv2
from modules.eye_detector import EyeDetector
from modules.camera_manager import CameraManager
from modules.alert_system import AlertSystem
from modules.data_logger import DataLogger
from modules.utils.constants import WINDOW_NAME


def main():
    """Main function to run the drowsiness detection system"""
    camera = CameraManager()
    eye_detector = EyeDetector()  # Closing parenthesis added here
    alert_system = AlertSystem()
    data_logger = DataLogger()

    try:
        print("Starting Drowsiness Detection System...")
        print("Press 'q' to exit")

        camera.start()

        while True:
            frame = camera.read_frame()
            ear, is_drowsy = eye_detector.detect_eyes(frame)

            if ear is not None:
                data_logger.log_drowsiness_level(ear)
                if is_drowsy:
                    alert_system.trigger_alert(ear)
                    data_logger.log_alert_triggered()

            cv2.imshow(WINDOW_NAME, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\nShutting down the system...")
    finally:
        camera.release()
        data_logger.close()


if __name__ == "__main__":
    main()
