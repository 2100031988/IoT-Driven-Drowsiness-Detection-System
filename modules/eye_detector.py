"""Eye detection and drowsiness analysis module"""
import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist
from .utils.constants import (
    EYE_AR_THRESH, EYE_AR_CONSEC_FRAMES,
    LEFT_EYE_START, LEFT_EYE_END,
    RIGHT_EYE_START, RIGHT_EYE_END,
    SHAPE_PREDICTOR_PATH
)
from .utils.visualization import draw_eye_landmarks, draw_drowsiness_info

class EyeDetector:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(SHAPE_PREDICTOR_PATH)
        self.frame_counter = 0
        self.blink_counter = 0
    
    def _get_eye_aspect_ratio(self, eye_points):
        """Calculate eye aspect ratio"""
        A = dist.euclidean(eye_points[1], eye_points[5])
        B = dist.euclidean(eye_points[2], eye_points[4])
        C = dist.euclidean(eye_points[0], eye_points[3])
        return (A + B) / (2.0 * C)
    
    def _extract_eye_points(self, landmarks, start, end):
        """Extract eye points from facial landmarks"""
        points = []
        for n in range(start, end):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            points.append((x, y))
        return points
    
    def detect_eyes(self, frame):
        """Detect eyes and calculate eye aspect ratio"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray, 0)
        
        for face in faces:
            landmarks = self.predictor(gray, face)
            
            left_eye = self._extract_eye_points(landmarks, LEFT_EYE_START, LEFT_EYE_END)
            right_eye = self._extract_eye_points(landmarks, RIGHT_EYE_START, RIGHT_EYE_END)
            
            draw_eye_landmarks(frame, left_eye)
            draw_eye_landmarks(frame, right_eye)
            
            left_ear = self._get_eye_aspect_ratio(left_eye)
            right_ear = self._get_eye_aspect_ratio(right_eye)
            ear = (left_ear + right_ear) / 2.0
            
            draw_drowsiness_info(frame, ear)
            
            if ear < EYE_AR_THRESH:
                self.frame_counter += 1
            else:
                if self.frame_counter >= EYE_AR_CONSEC_FRAMES:
                    self.blink_counter += 1
                self.frame_counter = 0
            
            return ear, self.frame_counter >= EYE_AR_CONSEC_FRAMES
        
        return None, False