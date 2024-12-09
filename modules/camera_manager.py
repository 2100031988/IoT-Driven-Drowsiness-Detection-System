"""Camera management module for video capture"""
import cv2

class CameraManager:
    def __init__(self):
        self.cap = None
        
    def start(self):
        """Start the camera capture"""
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("Could not open camera")
        
    def read_frame(self):
        """Read a frame from the camera"""
        if self.cap is None:
            raise RuntimeError("Camera not started")
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Could not read frame")
        return frame
    
    def release(self):
        """Release the camera"""
        if self.cap is not None:
            self.cap.release()
            cv2.destroyAllWindows()