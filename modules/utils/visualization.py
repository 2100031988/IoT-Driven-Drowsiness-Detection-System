"""Visualization utilities for drowsiness detection"""
import cv2
import numpy as np
from .constants import FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS

def draw_eye_landmarks(frame, eye_points, color=(0, 255, 0)):
    """Draw landmarks for an eye"""
    for x, y in eye_points:
        cv2.circle(frame, (x, y), 1, color, -1)
    
    hull = cv2.convexHull(np.array(eye_points))
    cv2.drawContours(frame, [hull], -1, color, 1)

def draw_drowsiness_info(frame, ear):
    """Draw EAR value on frame"""
    cv2.putText(frame, f"EAR: {ear:.2f}", (300, 30),
                getattr(cv2, FONT), FONT_SCALE, FONT_COLOR, FONT_THICKNESS)