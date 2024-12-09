"""Configuration settings for the drowsiness detection system"""
from dataclasses import dataclass

@dataclass
class DetectionConfig:
    """Detection-related configuration"""
    EYE_AR_THRESH: float = 0.25
    EYE_AR_CONSEC_FRAMES: int = 20
    LEFT_EYE_START: int = 36
    LEFT_EYE_END: int = 42
    RIGHT_EYE_START: int = 42
    RIGHT_EYE_END: int = 48

@dataclass
class DisplayConfig:
    """Display-related configuration"""
    WINDOW_NAME: str = "Drowsiness Detection"
    FONT: int = 0  # cv2.FONT_HERSHEY_SIMPLEX
    FONT_SCALE: float = 0.7
    FONT_COLOR: tuple = (0, 0, 255)
    FONT_THICKNESS: int = 2

class Config:
    """Global configuration container"""
    def __init__(self):
        self.detection = DetectionConfig()
        self.display = DisplayConfig()
        self.model_path = "shape_predictor_68_face_landmarks.dat"